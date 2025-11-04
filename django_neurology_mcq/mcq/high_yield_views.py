"""
Views for High-yield Reviews functionality.
"""

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from .high_yield_models import (
    HighYieldSpecialty,
    HighYieldTopic,
    TopicSectionImage
)


@login_required
def high_yield_home(request):
    """Display all specialties for high-yield reviews"""
    specialties = HighYieldSpecialty.objects.all().order_by('name')
    
    context = {
        'specialties': specialties,
        'page_title': 'High-Yield Reviews'
    }
    return render(request, 'mcq/high_yield/home.html', context)


@login_required
def high_yield_specialty(request, specialty_slug):
    """Display a specialty with its topics"""
    specialty = get_object_or_404(HighYieldSpecialty, slug=specialty_slug)
    
    # Get all topics for this specialty, ordered by their display order
    topics = specialty.topics.all().order_by('order', 'title')
    
    # Get the selected topic (first one by default)
    selected_topic_slug = request.GET.get('topic')
    
    if selected_topic_slug:
        selected_topic = get_object_or_404(
            HighYieldTopic, 
            specialty=specialty, 
            slug=selected_topic_slug
        )
    else:
        # Default to the first topic if available
        selected_topic = topics.first()
    
    # If we have a selected topic, prefetch its images organized by section
    if selected_topic:
        section_images = {}
        for image in selected_topic.section_images.all().order_by('section', 'order'):
            section = image.section
            if section not in section_images:
                section_images[section] = []
            section_images[section].append(image)
    else:
        section_images = {}
    
    context = {
        'specialty': specialty,
        'topics': topics,
        'selected_topic': selected_topic,
        'section_images': section_images,
        'page_title': f'{specialty.name} - High-Yield Review'
    }
    
    return render(request, 'mcq/high_yield/specialty.html', context)


@login_required
def high_yield_topic(request, specialty_slug, topic_slug):
    """Display a specific topic with all its content"""
    specialty = get_object_or_404(HighYieldSpecialty, slug=specialty_slug)
    topic = get_object_or_404(
        HighYieldTopic, 
        specialty=specialty, 
        slug=topic_slug
    )
    
    # Get all topics for the sidebar
    topics = specialty.topics.all().order_by('order', 'title')
    
    # Get images organized by section
    section_images = {}
    for image in topic.section_images.all().order_by('section', 'order'):
        section = image.section
        if section not in section_images:
            section_images[section] = []
        section_images[section].append(image)
    
    # Define sections with their display names
    sections = [
        ('introduction_classification', 'Introduction and Classification'),
        ('pathology_pathophysiology', 'Pathology and Pathophysiology'),
        ('epidemiology', 'Epidemiology'),
        ('clinical_presentation', 'Clinical Presentation'),
        ('paraclinical_testing', 'Para Clinical Testing'),
        ('diagnostic_criteria', 'Diagnostic Criteria'),
        ('differential_diagnosis', 'Differential Diagnosis'),
        ('management_guidelines', 'Management Guidelines'),
        ('prognosis', 'Prognosis'),
        ('common_pitfalls', 'Common Pitfalls'),
        ('latest_guidelines', 'Latest Guidelines and Evidence'),
    ]
    
    context = {
        'specialty': specialty,
        'topic': topic,
        'topics': topics,
        'section_images': section_images,
        'sections': sections,
        'page_title': f'{topic.title} - {specialty.name}'
    }
    
    return render(request, 'mcq/high_yield/topic.html', context)