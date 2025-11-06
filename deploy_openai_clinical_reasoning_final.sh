#!/bin/bash

echo "================================================"
echo "Deploying Final OpenAI Clinical Reasoning System"
echo "================================================"

# Add all modified files to git
echo "Adding modified files to git..."
git add django_neurology_mcq/mcq/cognitive_analysis_openai.py
git add django_neurology_mcq/mcq/clinical_reasoning_prompt.py
git add django_neurology_mcq/mcq/views.py

# Check if there are changes to commit
if git diff --cached --quiet; then
    echo "No changes to commit. Checking if already deployed..."
else
    # Commit changes
    echo "Committing changes..."
    git commit -m "Fix OpenAI clinical reasoning implementation

- Updated import to use existing OpenAI client from openai_integration.py
- Changed model to gpt-4o-mini for cost-effectiveness
- Fixed client initialization in CognitiveAnalyzerOpenAI
- Maintained fallback to rule-based system if OpenAI fails"
fi

# Push to Heroku
echo "Deploying to Heroku..."
git push heroku stable_version:main

echo "================================================"
echo "Deployment complete!"
echo "================================================"
echo ""
echo "IMPORTANT REMINDERS:"
echo "1. Ensure OPENAI_API_KEY is set on Heroku:"
echo "   heroku config:set OPENAI_API_KEY=your_key_here --app radiant-gorge-35079"
echo ""
echo "2. To verify the deployment:"
echo "   - Test clinical reasoning on a question"
echo "   - Check logs: heroku logs --tail --app radiant-gorge-35079"
echo ""
echo "3. The system now provides:"
echo "   - GPT-4o mini powered analysis"
echo "   - Professional medical education feedback"
echo "   - Structured 6-step analysis framework"
echo "   - Automatic fallback to rule-based system if needed"