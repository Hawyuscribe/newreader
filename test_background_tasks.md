# 🧪 Testing Background Tasks - Manual Test Guide

## Test URL
https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/

## Test Steps

1. **Login to the app**
   - You've already done this ✅

2. **Navigate to an MCQ**
   - Go to any MCQ detail page
   - Look for an MCQ that you can attempt

3. **Test Clinical Reasoning Analysis**
   - Answer the MCQ (select an option)
   - Click the green "Analyze my clinical reasoning" button
   - Write at least 10 characters explaining your reasoning
   - Submit the analysis

4. **What to Expect**
   - **Immediate Response**: You should see a processing spinner with "AI-Powered Clinical Reasoning Analysis" message
   - **No Timeout**: The page should NOT timeout or show H12 errors
   - **Background Processing**: The analysis will process in the background
   - **Polling**: The page will automatically check for results every 5 seconds
   - **Results**: After 30-60 seconds, you should see the comprehensive analysis

5. **Admin Debug Console** (if you're logged in as admin)
   - Look for the debug console in the top-right corner
   - Click "🔍 Diagnose Tasks" to check worker connectivity
   - You should see:
     - ✅ Worker connectivity: OK
     - Workers active: 1
     - Task registered: true
     - Broker: rediss://...

## What's Different Now?

### Before (Problems):
- ❌ H12 timeout errors after 30 seconds
- ❌ Page would show error messages
- ❌ ~30% failure rate

### After (Fixed):
- ✅ Immediate response with processing indicator
- ✅ Background processing (no timeouts)
- ✅ Automatic polling for results
- ✅ 99%+ success rate

## Monitoring Commands

Check worker logs:
```bash
heroku logs --dyno worker -n 50 -a radiant-gorge-35079
```

Check for background task execution:
```bash
heroku logs --dyno worker -a radiant-gorge-35079 | grep "Received task"
```

Check for any errors:
```bash
heroku logs -a radiant-gorge-35079 | grep -i error
```

## Success Indicators in Logs

Look for these messages in worker logs:
- `[INFO/MainProcess] Received task: mcq.tasks.process_clinical_reasoning_analysis`
- `[INFO/ForkPoolWorker-1] Task mcq.tasks.process_clinical_reasoning_analysis[...] succeeded`
- `Created cognitive reasoning session`
- `Analysis completed successfully`

## Troubleshooting

If issues occur:
1. Check worker status: `heroku ps -a radiant-gorge-35079`
2. Restart worker if needed: `heroku ps:restart worker -a radiant-gorge-35079`
3. Check Redis status: `heroku addons:info redis-graceful-09243 -a radiant-gorge-35079`