"""
Admin interface for High-yield Reviews.
"""

from django.contrib import admin
from django.utils.html import format_html
from django import forms
from .high_yield_models import (
    HighYieldSpecialty, 
    HighYieldTopic, 
    TopicSectionImage
)


class TopicInline(admin.TabularInline):
    """Inline admin for topics within a specialty"""
    model = HighYieldTopic
    extra = 1
    fields = ['title', 'order']
    show_change_link = True


@admin.register(HighYieldSpecialty)
class HighYieldSpecialtyAdmin(admin.ModelAdmin):
    """Admin interface for High-yield Specialties"""
    
    list_display = ['name', 'topic_count', 'created_by', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name', 'introduction']
    prepopulated_fields = {"slug": ("name",)}
    inlines = [TopicInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'created_by'),
            'classes': ('wide', 'high-yield-section'),
            'description': 'Title the specialty just as you would a Word document. Slug is generated automatically.'
        }),
        ('Overview Content', {
            'fields': ('introduction', 'introduction_image'),
            'classes': ('wide', 'high-yield-section'),
            'description': 'Use the ribbon above the editor to format your overview, insert images, or embed videos.'
        }),
        ('Historical & Current', {
            'fields': ('historical_overview',),
            'classes': ('wide', 'high-yield-section'),
        }),
        ('Concepts & Anatomy', {
            'fields': ('important_concepts', 'related_anatomy', 'anatomy_image'),
            'classes': ('wide', 'high-yield-section'),
        }),
    )
    
    def topic_count(self, obj):
        """Display number of topics in this specialty"""
        return obj.topics.count()
    topic_count.short_description = 'Number of Topics'
    
    def save_model(self, request, obj, form, change):
        if not change:  # If creating new object
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

    class Media:
        css = {
            'all': (
                'admin/css/high_yield_admin.css',
            )
        }
        js = (
            'admin/js/high_yield_admin.js',
        )


class TopicSectionImageInline(admin.TabularInline):
    """Inline admin for images within topic sections"""
    model = TopicSectionImage
    extra = 0
    fields = ['section', 'image_url', 'caption', 'order', 'preview']
    readonly_fields = ['preview']
    
    def preview(self, obj):
        """Show image preview"""
        if obj.image_url:
            return format_html(
                '<img src="{}" style="max-height: 100px; max-width: 150px;" />',
                obj.image_url
            )
        return "No image"
    preview.short_description = 'Preview'


class HighYieldTopicForm(forms.ModelForm):
    """Custom form for High-yield Topics"""
    
    class Meta:
        model = HighYieldTopic
        fields = '__all__'


@admin.register(HighYieldTopic)
class HighYieldTopicAdmin(admin.ModelAdmin):
    """Admin interface for High-yield Topics"""
    
    form = HighYieldTopicForm
    list_display = ['title', 'specialty', 'order', 'image_count', 'created_by', 'updated_at']
    list_filter = ['specialty', 'created_at', 'updated_at']
    search_fields = ['title', 'introduction_classification', 'specialty__name']
    prepopulated_fields = {"slug": ("title",)}
    inlines = [TopicSectionImageInline]
    list_editable = ['order']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('specialty', 'title', 'slug', 'order', 'created_by'),
            'classes': ('wide', 'high-yield-section'),
            'description': 'Give the topic a clear name. Slug and order are generated like Word headings.'
        }),
        ('Content Sections', {
            'fields': (
                'introduction_classification',
                'pathology_pathophysiology',
                'epidemiology',
                'clinical_presentation',
                'paraclinical_testing',
                'diagnostic_criteria',
                'differential_diagnosis',
                'management_guidelines',
                'prognosis',
                'common_pitfalls',
                'latest_guidelines',
            ),
            'classes': ('wide', 'high-yield-section'),
            'description': 'Each section behaves like a page in Word—use the toolbar to add tables, media, and formatting.'
        }),
    )
    
    def image_count(self, obj):
        """Display number of images in this topic"""
        return obj.section_images.count()
    image_count.short_description = 'Images'
    
    def save_model(self, request, obj, form, change):
        if not change:  # If creating new object
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

    class Media:
        css = {
            'all': (
                'admin/css/high_yield_admin.css',
            )
        }
        js = (
            'admin/js/high_yield_admin.js',
        )


@admin.register(TopicSectionImage)
class TopicSectionImageAdmin(admin.ModelAdmin):
    """Admin interface for Topic Section Images"""
    
    list_display = ['topic', 'section', 'caption', 'order', 'preview', 'created_at']
    list_filter = ['section', 'topic__specialty', 'created_at']
    search_fields = ['caption', 'topic__title', 'topic__specialty__name']
    list_editable = ['order']
    
    fieldsets = (
        ('Topic & Section', {
            'fields': ('topic', 'section')
        }),
        ('Image Details', {
            'fields': ('image_url', 'caption', 'order'),
            'description': 'Use Google Drive share links. They will be automatically converted to direct links.'
        }),
    )
    
    def preview(self, obj):
        """Show image preview"""
        if obj.image_url:
            return format_html(
                '<img src="{}" style="max-height: 80px; max-width: 120px;" />',
                obj.image_url
            )
        return "No image"
    preview.short_description = 'Preview'
