#!/bin/bash
# Test MCQ conversion on the website

echo "Testing MCQ conversion on https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com"
echo "Please ensure user login is temporarily disabled for this test"
echo "=" 
echo ""
echo "1. First, let's check if the site is accessible:"
curl -s -o /dev/null -w "%{http_code}" https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/mcq/
echo ""
echo ""
echo "2. To test the conversion:"
echo "   - Navigate to: https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/mcq/"
echo "   - Click on any MCQ (e.g., MCQ 100420848 if available)"
echo "   - Click 'Convert to Case-Based Learning'"
echo "   - Check if the conversion completes without JSON serialization errors"
echo ""
echo "3. Monitor the logs with:"
echo "   heroku logs --tail --app radiant-gorge-35079"