# Manual Testing Guide for MCQ-Case Session Fix

## Quick Test Steps

### 1. Deploy the Fix
```bash
./deploy_session_fix.sh
```

### 2. Run Automated Test on Heroku
```bash
heroku run python test_session_fix_heroku.py
```

### 3. Manual Browser Test

#### Test MCQ #100480663 (Coup Contrecoup Issue)
1. Go to: https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/mcq/100480663/
2. Select any answer and click "Check Answer"
3. Click "Turn into Case-Based Learning"
4. Verify the case is about **coup contrecoup brain injury**, NOT stroke/TIA

#### Test MCQ #100484440 (Essential Tremor Issue)
1. Go to: https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/mcq/100484440/
2. Select any answer and click "Check Answer"
3. Click "Turn into Case-Based Learning"
4. Verify the case is about **essential tremor**, NOT arm/leg weakness

### 4. Check Debug Console (Admin Only)

When viewing any MCQ as admin:
1. Open the Admin Debug Console (top right)
2. Look for the case conversion section
3. Check that session keys show format: `case_session_mcq_XXXXX_YY_Z`

### 5. Monitor Real-time Logs
```bash
heroku logs --tail --source app
```

Look for:
- "💬 Case conversion response" messages
- Session key format in logs
- Any error messages

## Expected Results

✅ **Before Fix:**
- URL showed: `?session_id=45` (just the number)
- Cases showed wrong medical conditions

✅ **After Fix:**
- URL shows: `?session_id=case_session_mcq_100480663_45_1` (full format)
- Cases match the original MCQ topic correctly

## Troubleshooting

If cases still show wrong content:
1. Clear browser cache and cookies
2. Try incognito/private browsing mode
3. Check if old sessions are being reused:
   ```bash
   heroku run python manage.py shell
   # Then run:
   from mcq.models import MCQCaseConversionSession
   MCQCaseConversionSession.objects.filter(mcq_id=100480663).delete()
   ```

## Success Criteria

The fix is working if:
1. ✅ Session URLs contain full session keys
2. ✅ Case content matches MCQ topics
3. ✅ No "session not found" errors
4. ✅ Debug console shows proper session key format