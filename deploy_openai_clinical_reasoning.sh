#!/bin/bash

echo "================================================"
echo "Deploying OpenAI-powered Clinical Reasoning"
echo "================================================"

# Add files to git
echo "Adding new files to git..."
git add django_neurology_mcq/mcq/clinical_reasoning_prompt.py
git add django_neurology_mcq/mcq/cognitive_analysis_openai.py
git add django_neurology_mcq/mcq/views.py

# Commit changes
echo "Committing changes..."
git commit -m "Implement OpenAI GPT-4.1 mini for clinical reasoning analysis

- Created professional medical education prompt based on OpenAI best practices
- Implemented structured prompt with system/user separation
- Added few-shot examples for better performance
- Integrated Chain-of-Thought prompting for clinical reasoning
- Maintained fallback to rule-based system if OpenAI fails
- Optimized temperature and parameters for medical content
- Added specific neurological context and evidence-based feedback"

# Push to Heroku
echo "Deploying to Heroku..."
git push heroku stable_version:main

echo "================================================"
echo "Deployment complete!"
echo "================================================"
echo ""
echo "IMPORTANT: The system will now use OpenAI GPT-4.1 mini for clinical reasoning analysis."
echo "Make sure your OPENAI_API_KEY environment variable is set on Heroku."
echo ""
echo "To verify the deployment:"
echo "1. Test a clinical reasoning analysis on the live site"
echo "2. Check Heroku logs: heroku logs --tail --app radiant-gorge-35079"
echo ""
echo "The new system provides:"
echo "- Personalized, context-aware feedback"
echo "- Evidence-based neurological insights"
echo "- Structured learning points"
echo "- Professional medical education quality"