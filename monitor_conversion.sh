#!/bin/bash
# Monitor MCQ conversion in real-time

echo "Monitoring MCQ conversions on Heroku..."
echo "Please manually test an MCQ conversion on the website while this runs"
echo "=" 
echo ""
echo "Monitoring for:"
echo "- Conversion start/completion"
echo "- Validation results"  
echo "- Any errors"
echo ""
echo "Press Ctrl+C to stop monitoring"
echo ""

heroku logs --tail --app radiant-gorge-35079 | grep -E --line-buffered "Starting conversion|Case generation|Validation completed|Conversion successful|ERROR|error|Failed|JSON serializable|ValidationStatus|MCQ [0-9]+|score:|clinical_presentation|patient_demographics"