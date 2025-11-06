#\!/bin/bash
python import_all_mcqs.py > import_log.txt 2>&1 &
echo Import started with PID: $\!
