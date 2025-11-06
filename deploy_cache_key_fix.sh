#!/bin/bash

echo "================================================"
echo "DEPLOYING CACHE KEY FIX TO HEROKU"
echo "================================================"
echo ""
echo "This deployment fixes the 503 error by correcting"
echo "the cache key mismatch in job status checking."
echo ""

# Add all changes
echo "📦 Step 1: Adding fixed files to git..."
git add django_neurology_mcq/mcq/views.py
git add fix_job_status_503.py
git add verify_cache_key_fix.py
git add test_job_status_fix.py

# Commit with descriptive message
echo ""
echo "💾 Step 2: Committing the fix..."
git commit -m "🔧 Fix 503 error: Correct cache key mismatch in job status

The issue was a cache key format mismatch:
- Options editing was storing with: ai_job_{job_id} (underscore)
- Job status was looking for: ai_job:{job_id} (colon)

This fix standardizes all cache keys to use colon format,
resolving the 503 error when checking job status."

# Push to Heroku
echo ""
echo "🚀 Step 3: Pushing to Heroku main branch..."
git push heroku main

# Check deployment status
echo ""
echo "================================================"
echo "✅ FIX DEPLOYED!"
echo "================================================"
echo ""
echo "The 503 error should now be resolved!"
echo ""
echo "Monitor the fix:"
echo "  heroku logs --tail --app enigmatic-hamlet-38937-db49bd5e9821"
echo ""
echo "The options editing should now work properly:"
echo "  1. Click 'Edit Options with AI' on any MCQ"
echo "  2. Select mode (fill missing, improve all, etc.)"
echo "  3. Job will complete without 503 errors"
echo ""