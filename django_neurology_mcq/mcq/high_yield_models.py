"""
Models for High-yield Reviews functionality.
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField
import re

def convert_google_drive_url(url):
    """Convert Google Drive share URL to direct image URL"""
    if not url:
        return url
    
    # Pattern for Google Drive share links
    pattern = r'https://drive\.google\.com/file/d/([a-zA-Z0-9_-]+)/view'
    match = re.match(pattern, url)
    
    if match:
        file_id = match.group(1)
        return f'https://drive.google.com/uc?export=view&id={file_id}'
    
    # If it's already a direct link or not a Google Drive link, return as is
    return url


class HighYieldSpecialty(models.Model):
    """Model for neurological specialties in high-yield reviews"""
    
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    
    # Overview content
    introduction = RichTextField(
        help_text="General overview of this specialty and its disorders",
        config_name='specialty_overview'
    )
    historical_overview = RichTextField(
        help_text="Brief historical overview and current nosology",
        config_name='specialty_overview'
    )
    important_concepts = RichTextField(
        help_text="Most important concepts",
        config_name='specialty_overview'
    )
    related_anatomy = RichTextField(
        help_text="Related anatomy",
        config_name='specialty_overview'
    )
    
    # Optional image fields
    introduction_image = models.URLField(
        blank=True,
        help_text="Google Drive URL for introduction image"
    )
    anatomy_image = models.URLField(
        blank=True,
        help_text="Google Drive URL for anatomy image"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True,
        related_name='created_specialties'
    )
    
    class Meta:
        verbose_name = "High-Yield Specialty"
        verbose_name_plural = "High-Yield Specialties"
        ordering = ['name']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        
        # Convert Google Drive URLs to direct links
        self.introduction_image = convert_google_drive_url(self.introduction_image)
        self.anatomy_image = convert_google_drive_url(self.anatomy_image)
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class HighYieldTopic(models.Model):
    """Model for topics within a specialty"""
    
    specialty = models.ForeignKey(
        HighYieldSpecialty,
        on_delete=models.CASCADE,
        related_name='topics'
    )
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, blank=True)
    order = models.IntegerField(default=0, help_text="Order in which topic appears")
    
    # Content sections
    introduction_classification = RichTextField(
        blank=True,
        help_text="Introduction and classification",
        config_name='default'
    )
    pathology_pathophysiology = RichTextField(
        blank=True,
        help_text="Pathology and pathophysiology",
        config_name='default'
    )
    epidemiology = RichTextField(
        blank=True,
        help_text="Epidemiology",
        config_name='default'
    )
    clinical_presentation = RichTextField(
        blank=True,
        help_text="Clinical presentation and physical exam",
        config_name='default'
    )
    paraclinical_testing = RichTextField(
        blank=True,
        help_text="Para clinical testing",
        config_name='default'
    )
    diagnostic_criteria = RichTextField(
        blank=True,
        help_text="Diagnostic criteria",
        config_name='default'
    )
    differential_diagnosis = RichTextField(
        blank=True,
        help_text="Differential diagnosis",
        config_name='default'
    )
    management_guidelines = RichTextField(
        blank=True,
        help_text="Management guidelines",
        config_name='default'
    )
    prognosis = RichTextField(
        blank=True,
        help_text="Prognosis",
        config_name='default'
    )
    common_pitfalls = RichTextField(
        blank=True,
        help_text="Common pitfalls",
        config_name='default'
    )
    latest_guidelines = RichTextField(
        blank=True,
        help_text="Latest guidelines and evidence",
        config_name='default'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_topics'
    )
    
    class Meta:
        verbose_name = "High-Yield Topic"
        verbose_name_plural = "High-Yield Topics"
        ordering = ['specialty', 'order', 'title']
        unique_together = [['specialty', 'slug']]
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.specialty.name} - {self.title}"


class TopicSectionImage(models.Model):
    """Model for images within topic sections"""
    
    SECTION_CHOICES = [
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
        ('latest_guidelines', 'Latest Guidelines'),
    ]
    
    topic = models.ForeignKey(
        HighYieldTopic,
        on_delete=models.CASCADE,
        related_name='section_images'
    )
    section = models.CharField(
        max_length=50,
        choices=SECTION_CHOICES,
        help_text="Which section this image belongs to"
    )
    image_url = models.URLField(
        help_text="Google Drive URL for the image"
    )
    caption = models.CharField(
        max_length=500,
        blank=True,
        help_text="Caption for the image"
    )
    order = models.IntegerField(
        default=0,
        help_text="Order within the section"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Topic Section Image"
        verbose_name_plural = "Topic Section Images"
        ordering = ['topic', 'section', 'order']
    
    def save(self, *args, **kwargs):
        # Convert Google Drive URL to direct link
        self.image_url = convert_google_drive_url(self.image_url)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.topic.title} - {self.get_section_display()} - Image {self.order}"