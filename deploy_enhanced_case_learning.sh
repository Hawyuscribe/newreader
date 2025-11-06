#!/bin/bash

echo "==============================================="
echo "Deploying Enhanced Case-Based Learning to Heroku"
echo "==============================================="

# Create backup directory
BACKUP_DIR="backup_before_enhanced_$(date +%Y%m%d_%H%M%S)"
mkdir -p $BACKUP_DIR

# Backup current files
echo "Creating backup of current files..."
cp django_neurology_mcq/mcq/case_bot.py $BACKUP_DIR/ 2>/dev/null
cp django_neurology_mcq/mcq/urls.py $BACKUP_DIR/ 2>/dev/null
cp django_neurology_mcq/templates/mcq/case_based_learning.html $BACKUP_DIR/ 2>/dev/null

echo "Backup created in $BACKUP_DIR"

# Deploy steps
echo ""
echo "To deploy the enhanced case-based learning:"
echo ""
echo "1. First, test locally:"
echo "   - Copy case_bot_enhanced.py to django_neurology_mcq/mcq/"
echo "   - Copy case_based_learning_enhanced.html to django_neurology_mcq/templates/mcq/"
echo "   - Update urls.py to import from case_bot_enhanced"
echo "   - Run: python manage.py runserver"
echo "   - Test at: http://localhost:8000/case-based-learning-enhanced/"
echo ""
echo "2. If testing is successful, deploy to Heroku:"
echo "   - git add django_neurology_mcq/mcq/case_bot_enhanced.py"
echo "   - git add django_neurology_mcq/templates/mcq/case_based_learning_enhanced.html"
echo "   - git add django_neurology_mcq/mcq/urls.py"
echo "   - git commit -m 'Add enhanced case-based learning with GPT-4.1-mini'"
echo "   - git push heroku main"
echo ""
echo "3. Alternatively, replace the original files:"
echo "   - Rename case_bot.py to case_bot_original.py"
echo "   - Rename case_bot_enhanced.py to case_bot.py"
echo "   - Update imports in urls.py"
echo "   - Rename templates similarly"
echo ""

# Create a summary of changes
cat > ENHANCED_CASE_LEARNING_FEATURES.md << 'EOF'
# Enhanced Case-Based Learning Features

## Implemented Features:

### 1. GPT-4.1-mini Model Integration
- Updated to use the latest GPT-4.1-mini model
- Improved response quality and speed
- Enhanced retry logic with exponential backoff

### 2. Comprehensive Case Pools
- 40-50 unique cases per specialty
- Each specialty has easy, moderate, and hard cases
- Total of 600+ unique case scenarios

### 3. Difficulty Selection
- Users can choose: Easy, Moderate, Hard, or Random
- Each difficulty level has appropriate cases
- Visual indicators for difficulty

### 4. Skip Case Functionality
- Users can skip cases they don't like
- System tracks skipped cases
- Generates new unique cases

### 5. Critical Element Feedback
- Tracks critical history elements
- Tracks critical examination elements
- Prompts users when important elements are missed
- Option to provide missing information

### 6. Standardized Screening Exam
- Every case includes basic neurological screening
- Consistent format across all cases
- Additional detailed exams on request

### 7. Enhanced UI
- Modern, responsive design
- Better visual feedback
- Keyboard shortcuts
- Voice recording support

### 8. Improved Case Generation
- Unique case hashing
- User history tracking
- Avoids repetition
- Age-appropriate cases

### 9. Better Error Handling
- API retry logic
- Rate limiting with burst protection
- Session management
- Graceful error recovery

### 10. State Management
- Clear phase transitions
- Feedback states for missing elements
- Visual state indicators
- Quick navigation buttons

## Usage:
- Access at: /case-based-learning-enhanced/
- Or replace original at: /case-based-learning/
EOF

echo ""
echo "Feature summary created in ENHANCED_CASE_LEARNING_FEATURES.md"
echo ""
echo "==============================================="