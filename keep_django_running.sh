#!/bin/bash
# Script to keep Django server running continuously
# Restarts server if it crashes

PROJECT_DIR="$(dirname "$0")"
DJANGO_DIR="$PROJECT_DIR/django_neurology_mcq"
LOG_DIR="$PROJECT_DIR/logs"
VENV_PATH="$PROJECT_DIR/venv"
PID_FILE="$DJANGO_DIR/django_server.pid"
LOG_FILE="$LOG_DIR/django_server.log"
RESTART_LOG="$LOG_DIR/django_restart.log"

# Create logs directory if it doesn't exist
mkdir -p "$LOG_DIR"

log_message() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$RESTART_LOG"
}

kill_existing_server() {
  if [ -f "$PID_FILE" ]; then
    local pid=$(cat "$PID_FILE")
    if ps -p $pid > /dev/null; then
      log_message "Stopping existing Django server (PID: $pid)..."
      kill $pid
      sleep 2
      if ps -p $pid > /dev/null; then
        log_message "Server didn't stop gracefully, forcing..."
        kill -9 $pid
      fi
    else
      log_message "PID file exists but process is not running"
    fi
    rm -f "$PID_FILE"
  fi
}

start_server() {
  cd "$DJANGO_DIR"
  source "$VENV_PATH/bin/activate"
  log_message "Starting Django server..."
  
  # Load environment variables
  python "$PROJECT_DIR/load_env.py" >> "$LOG_FILE" 2>&1
  
  # Start the Django server
  nohup python manage.py runserver 127.0.0.1:8000 > "$LOG_FILE" 2>&1 &
  
  # Save PID
  echo $! > "$PID_FILE"
  local new_pid=$(cat "$PID_FILE")
  log_message "Django server started with PID: $new_pid"
  
  # Wait a moment to ensure the server started correctly
  sleep 5
  if ! ps -p $new_pid > /dev/null; then
    log_message "Server failed to start properly!"
    return 1
  fi
  
  return 0
}

check_server() {
  # Check if server responds to HTTP requests
  if curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8000/ | grep -q "200\|302\|301\|304"; then
    return 0
  else
    log_message "Server not responding to HTTP requests"
    return 1
  fi
}

# Kill any existing Django server
kill_existing_server

# Start server initially
start_server

# Main loop to keep server running
log_message "Entering monitoring loop..."
while true; do
  # Is the process running?
  if [ -f "$PID_FILE" ]; then
    pid=$(cat "$PID_FILE")
    if ! ps -p $pid > /dev/null; then
      log_message "Django server process died. Restarting..."
      start_server
    else
      # Process is running, but is it responsive?
      if ! check_server; then
        log_message "Django server not responsive. Restarting..."
        kill_existing_server
        start_server
      else
        # Optional: log that server is healthy
        # log_message "Server is healthy"
        :
      fi
    fi
  else
    log_message "PID file missing. Restarting server..."
    start_server
  fi
  
  # Sleep before checking again (30 seconds)
  sleep 30
done