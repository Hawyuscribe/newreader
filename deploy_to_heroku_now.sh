#!/bin/bash

echo "==============================================="
echo "Deploying Enhanced Case-Based Learning to Heroku"
echo "==============================================="

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "Error: Not in a git repository"
    exit 1
fi

# Check if heroku remote exists
if ! git remote | grep -q "heroku"; then
    echo "Error: Heroku remote not found"
    echo "Please add Heroku remote: heroku git:remote -a radiant-gorge-35079"
    exit 1
fi

echo "Current git status:"
git status --short

echo ""
echo "Adding enhanced case-based learning files..."

# Add the new files
git add django_neurology_mcq/mcq/case_bot_enhanced.py
git add django_neurology_mcq/templates/mcq/case_based_learning_enhanced.html
git add django_neurology_mcq/mcq/urls_enhanced.py

# Check if urls.py needs to be updated
echo ""
echo "Updating urls.py to include enhanced endpoints..."

# Create a temporary updated urls.py
cat > django_neurology_mcq/mcq/urls_temp.py << 'EOF'
from django.urls import path
from . import views
from .case_bot import case_based_learning, neurology_bot, transcribe_audio
# Import enhanced version
try:
    from .case_bot_enhanced import (
        case_based_learning_enhanced, 
        neurology_bot_enhanced, 
        transcribe_audio_enhanced
    )
    enhanced_available = True
except ImportError:
    enhanced_available = False
    
from .high_yield_views import high_yield_home, high_yield_specialty, high_yield_topic

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('search/', views.search, name='search'),
    path('subspecialty/<path:subspecialty>/', views.subspecialty_view, name='subspecialty'),
    path('mcq/<int:mcq_id>/', views.view_mcq, name='view_mcq'),
    path('mcq/<int:mcq_id>/test_image/', views.test_image_display, name='test_image_display'),
    path('mcq/<int:mcq_id>/check_answer/', views.check_answer, name='check_answer'),
    path('mcq/<int:mcq_id>/toggle_bookmark/', views.toggle_bookmark, name='toggle_bookmark'),
    path('mcq/<int:mcq_id>/save_note/', views.save_note, name='save_note'),
    path('mcq/<int:mcq_id>/create_flashcard/', views.create_flashcard, name='create_flashcard'),
    path('mcq/<int:mcq_id>/reclassify/', views.reclassify_mcq, name='reclassify_mcq'),
    path('mcq/<int:mcq_id>/create_explanation/', views.create_explanation, name='create_explanation'),
    path('mcq/<int:mcq_id>/check_explanation/', views.check_explanation, name='check_explanation'),
    path('mcq/<int:mcq_id>/improve/', views.improve_mcq_view, name='improve_mcq'),
    path('mcq/<int:mcq_id>/new_options/', views.new_options_view, name='new_options'),
    path('mcq/<int:mcq_id>/ask_gpt/', views.ask_gpt, name='ask_gpt'),
    path('review_flashcards/', views.review_flashcards, name='review_flashcards'),
    path('review_bookmarked/', views.review_bookmarked, name='review_bookmarked'),
    path('diagnostics/', views.diagnostics_view, name='diagnostics'),
    path('import/', views.import_mcqs_form, name='import_mcqs_form'),
    path('mcq/<int:mcq_id>/reasoning_pal/', views.reasoning_pal, name='reasoning_pal'),
    path('mcq/<int:mcq_id>/check_reasoning/', views.check_reasoning, name='check_reasoning'),
    path('reasoning_session/<int:session_id>/feedback/', views.reasoning_feedback, name='reasoning_feedback'),
    path('mcq/<int:mcq_id>/generate_test_question/', views.generate_test_question, name='generate_test_question'),
    path('mcq/<int:mcq_id>/analyze_test_reasoning/', views.analyze_test_reasoning, name='analyze_test_reasoning'),
    path('mcq/<int:mcq_id>/hide/', views.hide_mcq, name='hide_mcq'),
    path('mcq/<int:mcq_id>/unhide/', views.unhide_mcq, name='unhide_mcq'),
    path('hidden_mcqs/', views.view_hidden_mcqs, name='view_hidden_mcqs'),
    path('submit_exam/', views.submit_exam, name='submit_exam'),
    path('test_weakness/', views.test_weakness, name='test_weakness'),
    path('mcq/<int:mcq_id>/check_weakness_answer/', views.check_weakness_answer, name='check_weakness_answer'),
    path('mcq/<int:mcq_id>/report/', views.show_report_form, name='show_report_form'),
    path('mcq/<int:mcq_id>/submit_report/', views.report_question, name='report_question'),
    
    # Original Case-Based Learning URLs
    path('case-based-learning/', case_based_learning, name='case_based_learning'),
    path('api/neurology-bot/', neurology_bot, name='neurology_bot'),
    path('api/transcribe-audio/', transcribe_audio, name='transcribe_audio'),
    
    # High-Yield Reviews URLs
    path('high-yield/', high_yield_home, name='high_yield_home'),
    path('high-yield/<slug:specialty_slug>/', high_yield_specialty, name='high_yield_specialty'),
    path('high-yield/<slug:specialty_slug>/<slug:topic_slug>/', high_yield_topic, name='high_yield_topic'),
    
    # Admin Export URLs
    path('admin-export/', views.admin_export_page, name='admin_export_page'),
    path('export/vascular-mcqs/', views.export_vascular_mcqs, name='export_vascular_mcqs'),
    path('export/subspecialty/<path:subspecialty>/', views.export_subspecialty_mcqs, name='export_subspecialty_mcqs'),
]

# Add enhanced URLs if available
if enhanced_available:
    urlpatterns += [
        path('case-based-learning-enhanced/', case_based_learning_enhanced, name='case_based_learning_enhanced'),
        path('api/neurology-bot-enhanced/', neurology_bot_enhanced, name='neurology_bot_enhanced'),
        path('api/transcribe-audio-enhanced/', transcribe_audio_enhanced, name='transcribe_audio_enhanced'),
    ]
EOF

# Backup original urls.py
cp django_neurology_mcq/mcq/urls.py django_neurology_mcq/mcq/urls_backup.py

# Replace with updated version
mv django_neurology_mcq/mcq/urls_temp.py django_neurology_mcq/mcq/urls.py

echo "Updated urls.py with enhanced endpoints"

# Add urls.py to git
git add django_neurology_mcq/mcq/urls.py

# Show what will be committed
echo ""
echo "Files to be committed:"
git status --short

echo ""
read -p "Do you want to commit these changes? (y/n) " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    # Commit the changes
    git commit -m "Add enhanced case-based learning with GPT-4.1-mini

- Integrated GPT-4.1-mini model
- Added 40-50 unique cases per specialty with difficulty levels
- Implemented skip case functionality
- Added critical history/exam element feedback
- Standardized screening neurological examination
- Enhanced UI with difficulty selection
- Improved case generation algorithm
- Better error handling and retry logic"

    echo ""
    echo "Changes committed successfully!"
    
    # Push to Heroku
    echo ""
    read -p "Do you want to push to Heroku now? (y/n) " -n 1 -r
    echo ""
    
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "Pushing to Heroku..."
        git push heroku main
        
        echo ""
        echo "Deployment complete!"
        echo ""
        echo "Your enhanced case-based learning system is now available at:"
        echo "https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/case-based-learning-enhanced/"
        echo ""
        echo "The original version remains available at:"
        echo "https://radiant-gorge-35079-2b52ba172c1e.herokuapp.com/case-based-learning/"
    else
        echo "Commit created but not pushed. To push later, run: git push heroku main"
    fi
else
    echo "Commit cancelled. Restoring original urls.py..."
    mv django_neurology_mcq/mcq/urls_backup.py django_neurology_mcq/mcq/urls.py
    git reset HEAD django_neurology_mcq/mcq/urls.py
fi

echo ""
echo "==============================================="