from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import MCQ, Bookmark, Flashcard, Note, UserProfile, HiddenMCQ, QuestionReport
from django import forms
from django.utils import timezone
from django.db.models import Count, Q
from ckeditor.widgets import CKEditorWidget
import json

# Import High-yield Review admin
from .high_yield_admin import (
    HighYieldSpecialtyAdmin,
    HighYieldTopicAdmin,
    TopicSectionImageAdmin
)

# Register inline admin for UserProfile
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'
    fk_name = 'user'

# Extend the UserAdmin to include UserProfile inline and custom actions
class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_expiration', 'is_account_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    actions = ['extend_account_30_days', 'extend_account_90_days', 'extend_account_365_days', 'deactivate_accounts']
    
    def get_expiration(self, obj):
        try:
            if obj.profile.expiration_date:
                return obj.profile.expiration_date.strftime('%Y-%m-%d')
            return 'No expiration'
        except UserProfile.DoesNotExist:
            return 'No profile'
    get_expiration.short_description = 'Expires on'
    
    def is_account_active(self, obj):
        try:
            return obj.profile.is_active
        except UserProfile.DoesNotExist:
            return obj.is_active
    is_account_active.boolean = True
    is_account_active.short_description = 'Active'
    
    def extend_account_30_days(self, request, queryset):
        for user in queryset:
            try:
                profile, created = UserProfile.objects.get_or_create(user=user)
                profile.extend_expiration(30)
            except Exception as e:
                self.message_user(request, f"Error extending {user.username}: {str(e)}")
        self.message_user(request, f"Extended {queryset.count()} accounts by 30 days")
    extend_account_30_days.short_description = "Extend selected accounts by 30 days"
    
    def extend_account_90_days(self, request, queryset):
        for user in queryset:
            try:
                profile, created = UserProfile.objects.get_or_create(user=user)
                profile.extend_expiration(90)
            except Exception as e:
                self.message_user(request, f"Error extending {user.username}: {str(e)}")
        self.message_user(request, f"Extended {queryset.count()} accounts by 90 days")
    extend_account_90_days.short_description = "Extend selected accounts by 90 days"
    
    def extend_account_365_days(self, request, queryset):
        for user in queryset:
            try:
                profile, created = UserProfile.objects.get_or_create(user=user)
                profile.extend_expiration(365)
            except Exception as e:
                self.message_user(request, f"Error extending {user.username}: {str(e)}")
        self.message_user(request, f"Extended {queryset.count()} accounts by 365 days")
    extend_account_365_days.short_description = "Extend selected accounts by 1 year"
    
    def deactivate_accounts(self, request, queryset):
        for user in queryset:
            try:
                profile, created = UserProfile.objects.get_or_create(user=user)
                profile.is_active_override = False
                profile.save()
            except Exception as e:
                self.message_user(request, f"Error deactivating {user.username}: {str(e)}")
        self.message_user(request, f"Deactivated {queryset.count()} accounts")
    deactivate_accounts.short_description = "Deactivate selected accounts"
    
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super().get_inline_instances(request, obj)

# Unregister the default User admin and register our custom admin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

class MCQAdminForm(forms.ModelForm):
    """Custom form for MCQ admin with improved options input."""

    # Text area for options with simplified format
    options_text = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 6, 'cols': 60}),
        required=False,
        help_text="Enter options in format: A. Option text<br>B. Option text<br>C. Option text<br>D. Option text"
    )
    
    # Main explanation field (hidden, we'll manage it through individual sections)
    explanation = forms.CharField(
        widget=forms.HiddenInput(),
        required=False
    )
    
    # Individual section fields for comprehensive medical explanation
    conceptual_foundation = forms.CharField(
        widget=CKEditorWidget(),
        required=False,
        label="1. Conceptual Foundation",
        help_text="Core concepts about the topic"
    )
    
    pathophysiology = forms.CharField(
        widget=CKEditorWidget(),
        required=False,
        label="2. Pathophysiology",
        help_text="Brief concise and updated review of the pathophysiology of the condition/disorder. For therapy/medication questions, discuss mechanism of action."
    )
    
    clinical_correlation = forms.CharField(
        widget=CKEditorWidget(),
        required=False,
        label="3. Clinical Correlation",
        help_text="Deep analysis of the clinical presentation and how it relates to the correct answer"
    )
    
    diagnostic_approach = forms.CharField(
        widget=CKEditorWidget(),
        required=False,
        label="4. Diagnostic Approach",
        help_text="According to the latest and updated guidelines"
    )
    
    classification_neurology = forms.CharField(
        widget=CKEditorWidget(),
        required=False,
        label="5. Classification and Neurology",
        help_text="Brief updated classification of the disorder/condition and how it relates to other similar disorders"
    )
    
    management_principles = forms.CharField(
        widget=CKEditorWidget(),
        required=False,
        label="6. Management Principles",
        help_text="Brief concise updated management principles and guidelines based on latest evidence with tiered approach (first line > second line etc.)"
    )
    
    option_analysis = forms.CharField(
        widget=CKEditorWidget(),
        required=False,
        label="7. Option Analysis",
        help_text="Compare the options and explain why the wrong answers are incorrect"
    )
    
    clinical_pearls = forms.CharField(
        widget=CKEditorWidget(),
        required=False,
        label="8. Clinical Pearls",
        help_text="Very high yield information related to the question and answers"
    )
    
    current_evidence = forms.CharField(
        widget=CKEditorWidget(),
        required=False,
        label="9. Current Evidence",
        help_text="List the latest guidelines and brief quotes related to the question"
    )

    # Dropdown for subspecialty
    SUBSPECIALTIES = (
        ('Critical Care Neurology', 'Critical Care Neurology'),
        ('Dementia', 'Dementia'),
        ('Epilepsy', 'Epilepsy'),
        ('Headache', 'Headache'),
        ('Movement Disorders', 'Movement Disorders'),
        ('Neuro-infectious', 'Neuro-infectious'),
        ('Neuro-oncology', 'Neuro-oncology'),
        ('Neuro-otology', 'Neuro-otology'),
        ('Neuroanatomy', 'Neuroanatomy'),
        ('Neurogenetics', 'Neurogenetics'),
        ('Neuroimmunology', 'Neuroimmunology'),
        ('Neuromuscular', 'Neuromuscular'),
        ('Neuroophthalmology', 'Neuroophthalmology'),
        ('Neuropsychiatry', 'Neuropsychiatry'),
        ('Neurotoxicology', 'Neurotoxicology'),
        ('Other/Unclassified', 'Other/Unclassified'),
        ('Pediatric Neurology', 'Pediatric Neurology'),
        ('Sleep Neurology', 'Sleep Neurology'),
        ('Vascular Neurology/Stroke', 'Vascular Neurology/Stroke'),
    )

    subspecialty = forms.ChoiceField(choices=SUBSPECIALTIES)

    class Meta:
        model = MCQ
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # If editing an existing MCQ, convert JSON options to text format
        if self.instance and self.instance.pk and self.instance.options:
            options_dict = self.instance.get_options_dict()
            options_lines = []
            for key, value in options_dict.items():
                options_lines.append(f"{key}. {value}")
            self.fields['options_text'].initial = "\n".join(options_lines)
        
        # If editing an existing MCQ, parse the explanation sections
        if self.instance and self.instance.pk:
            # First check for explanation_sections field (the proper JSON field)
            if self.instance.explanation_sections:
                sections = self.instance.explanation_sections
                
                # Map database keys to form fields, handling various formats
                field_mappings = {
                    'conceptual_foundation': [
                        'conceptual foundation',
                        'conceptual_foundation',
                        'Conceptual Foundation',
                    ],
                    'pathophysiology': [
                        'pathophysiology',
                        'Pathophysiology',
                        'pathophysiological_mechanisms',
                        'pathophysiological mechanisms',
                        'Pathophysiological Mechanisms',
                    ],
                    'clinical_correlation': [
                        'clinical correlation',
                        'clinical_correlation',
                        'Clinical Correlation',
                        'clinical context',
                        'clinical_context',
                        'Clinical Context',
                    ],
                    'diagnostic_approach': [
                        'diagnostic approach',
                        'diagnostic_approach',
                        'Diagnostic Approach',
                    ],
                    'classification_neurology': [
                        'classification and neurology',
                        'classification_neurology',
                        'Classification and Neurology',
                        'classification_and_nosology',
                        'classification and nosology',
                        'Classification and Nosology',
                    ],
                    'management_principles': [
                        'management principles',
                        'management_principles',
                        'Management Principles',
                    ],
                    'option_analysis': [
                        'option analysis',
                        'option_analysis',
                        'Option Analysis',
                        'options analysis',
                        'answer analysis',
                    ],
                    'clinical_pearls': [
                        'clinical pearls',
                        'clinical_pearls',
                        'Clinical Pearls',
                        'key insight',
                        'key_insight',
                        'Key Insight',
                    ],
                    'current_evidence': [
                        'current evidence',
                        'current_evidence',
                        'Current Evidence',
                        'quick reference',
                        'quick_reference',
                        'Quick Reference',
                        'application and recall',
                        'application_and_recall',
                        'Application and Recall',
                    ]
                }
                
                # Populate fields using the mappings
                for field_name, possible_keys in field_mappings.items():
                    value = None
                    for key in possible_keys:
                        if key in sections and sections[key]:
                            value = sections[key]
                            break
                    if value:
                        self.fields[field_name].initial = value
            # If no explanation_sections, try to parse the explanation field
            elif self.instance.explanation:
                try:
                    explanation_data = json.loads(self.instance.explanation)
                    
                    # Populate individual section fields from parsed JSON
                    if isinstance(explanation_data, dict):
                        # Handle both underscore and space formats for all fields
                        self.fields['conceptual_foundation'].initial = (
                            explanation_data.get('conceptual foundation', '') or
                            explanation_data.get('conceptual_foundation', '') or
                            explanation_data.get('Conceptual Foundation', '')
                        )
                        self.fields['pathophysiology'].initial = (
                            explanation_data.get('pathophysiology', '') or
                            explanation_data.get('Pathophysiology', '') or
                            explanation_data.get('pathophysiological_mechanisms', '')
                        )
                        self.fields['clinical_correlation'].initial = (
                            explanation_data.get('clinical correlation', '') or
                            explanation_data.get('clinical_correlation', '') or
                            explanation_data.get('Clinical Correlation', '') or
                            explanation_data.get('clinical context', '') or
                            explanation_data.get('clinical_context', '') or
                            explanation_data.get('Clinical Context', '')
                        )
                        self.fields['diagnostic_approach'].initial = (
                            explanation_data.get('diagnostic approach', '') or
                            explanation_data.get('diagnostic_approach', '') or
                            explanation_data.get('Diagnostic Approach', '')
                        )
                        self.fields['classification_neurology'].initial = (
                            explanation_data.get('classification and neurology', '') or
                            explanation_data.get('classification_neurology', '') or
                            explanation_data.get('Classification and Neurology', '')
                        )
                        self.fields['management_principles'].initial = (
                            explanation_data.get('management principles', '') or
                            explanation_data.get('management_principles', '') or
                            explanation_data.get('Management Principles', '')
                        )
                        self.fields['option_analysis'].initial = (
                            explanation_data.get('option analysis', '') or
                            explanation_data.get('option_analysis', '') or
                            explanation_data.get('Option Analysis', '')
                        )
                        self.fields['clinical_pearls'].initial = (
                            explanation_data.get('clinical pearls', '') or
                            explanation_data.get('clinical_pearls', '') or
                            explanation_data.get('Clinical Pearls', '') or
                            explanation_data.get('key insight', '') or
                            explanation_data.get('key_insight', '') or
                            explanation_data.get('Key Insight', '')
                        )
                        self.fields['current_evidence'].initial = (
                            explanation_data.get('current evidence', '') or
                            explanation_data.get('current_evidence', '') or
                            explanation_data.get('Current Evidence', '') or
                            explanation_data.get('quick reference', '') or
                            explanation_data.get('quick_reference', '') or
                            explanation_data.get('Quick Reference', '') or
                            explanation_data.get('application and recall', '') or
                            explanation_data.get('application_and_recall', '') or
                            explanation_data.get('Application and Recall', '')
                        )
                    else:
                        # If explanation is not a JSON dict, try to parse it as structured text
                        self._parse_text_explanation(self.instance.explanation)
                except json.JSONDecodeError:
                    # If explanation is not valid JSON, try to parse it as structured text
                    self._parse_text_explanation(self.instance.explanation)
    
    def _parse_text_explanation(self, text):
        """Parse a text explanation into sections"""
        import re
        
        # Define patterns for common section headers
        patterns = {
            'conceptual_foundation': r'(?:^|\n)(Conceptual Foundation)(.*?)(?=\n[A-Z][^a-z]*:|\n\n[A-Z]|$)',
            'pathophysiology': r'(?:^|\n)(Pathophysiology)(.*?)(?=\n[A-Z][^a-z]*:|\n\n[A-Z]|$)',
            'clinical_correlation': r'(?:^|\n)(Clinical Correlation|Clinical Context)(.*?)(?=\n[A-Z][^a-z]*:|\n\n[A-Z]|$)',
            'diagnostic_approach': r'(?:^|\n)(Diagnostic Approach)(.*?)(?=\n[A-Z][^a-z]*:|\n\n[A-Z]|$)',
            'classification_neurology': r'(?:^|\n)(Classification and Neurology)(.*?)(?=\n[A-Z][^a-z]*:|\n\n[A-Z]|$)',
            'management_principles': r'(?:^|\n)(Management Principles)(.*?)(?=\n[A-Z][^a-z]*:|\n\n[A-Z]|$)',
            'option_analysis': r'(?:^|\n)(Option Analysis)(.*?)(?=\n[A-Z][^a-z]*:|\n\n[A-Z]|$)',
            'clinical_pearls': r'(?:^|\n)(Clinical Pearls|Key Insight)(.*?)(?=\n[A-Z][^a-z]*:|\n\n[A-Z]|$)',
            'current_evidence': r'(?:^|\n)(Current Evidence|Quick Reference|Application and Recall)(.*?)(?=\n[A-Z][^a-z]*:|\n\n[A-Z]|$)',
        }
        
        # Try to extract sections
        for field_name, pattern in patterns.items():
            match = re.search(pattern, text, re.DOTALL | re.MULTILINE | re.IGNORECASE)
            if match:
                content = match.group(2).strip()
                if content:
                    self.fields[field_name].initial = content
        
        # If no sections found, put everything in conceptual foundation
        if not any(self.fields[field].initial for field in patterns.keys()):
            self.fields['conceptual_foundation'].initial = text

    def clean(self):
        cleaned_data = super().clean()
        options_text = cleaned_data.get('options_text', '')

        # Convert options text to JSON format
        if options_text:
            options_dict = {}
            for line in options_text.split('\n'):
                line = line.strip()
                if not line:
                    continue

                # Handle both "A. Text" and "A Text" formats
                if '. ' in line[:3]:
                    key, value = line.split('. ', 1)
                else:
                    key, value = line[:1], line[1:].strip()

                key = key.strip().upper()
                options_dict[key] = value.strip()

            cleaned_data['options'] = options_dict

        return cleaned_data
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # Start with existing explanation_sections if they exist
        if instance.explanation_sections:
            existing_sections = instance.explanation_sections.copy()
        else:
            existing_sections = {}
        
        # Combine individual sections back into JSON format using standardized keys
        new_sections = {
            'conceptual_foundation': self.cleaned_data.get('conceptual_foundation', ''),
            'pathophysiological_mechanisms': self.cleaned_data.get('pathophysiology', ''),
            'clinical_correlation': self.cleaned_data.get('clinical_correlation', ''),
            'diagnostic_approach': self.cleaned_data.get('diagnostic_approach', ''),
            'classification_and_nosology': self.cleaned_data.get('classification_neurology', ''),
            'management_principles': self.cleaned_data.get('management_principles', ''),
            'option_analysis': self.cleaned_data.get('option_analysis', ''),
            'clinical_pearls': self.cleaned_data.get('clinical_pearls', ''),
            'current_evidence': self.cleaned_data.get('current_evidence', '')
        }
        
        # Update existing sections with new values
        for key, value in new_sections.items():
            if value:  # Only update if there's a value
                existing_sections[key] = value
        
        # Save to the proper field and also maintain the old field for compatibility
        instance.explanation_sections = existing_sections
        instance.explanation = json.dumps(existing_sections, indent=2)
        
        if commit:
            instance.save()
        return instance

class QuestionReportInline(admin.TabularInline):
    """Inline for viewing reports on an MCQ"""
    model = QuestionReport
    extra = 0
    readonly_fields = ('user', 'status', 'suggested_correct_answer', 'reason', 'created_at')
    can_delete = False
    
    def has_add_permission(self, request, obj=None):
        return False

class HasImageFilter(admin.SimpleListFilter):
    title = 'has image'
    parameter_name = 'has_image'
    
    def lookups(self, request, model_admin):
        return (
            ('yes', 'Yes'),
            ('no', 'No'),
        )
    
    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.exclude(image_url='').exclude(image_url__isnull=True)
        if self.value() == 'no':
            return queryset.filter(Q(image_url='') | Q(image_url__isnull=True))

class HasReportsFilter(admin.SimpleListFilter):
    title = 'has reports'
    parameter_name = 'has_reports'
    
    def lookups(self, request, model_admin):
        return (
            ('yes', 'Yes (Pending)'),
            ('no', 'No Reports'),
            ('any', 'Any Reports'),
        )
    
    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.filter(reports__status='pending').distinct()
        if self.value() == 'no':
            return queryset.exclude(reports__isnull=False)
        if self.value() == 'any':
            return queryset.filter(reports__isnull=False).distinct()

@admin.register(MCQ)
class MCQAdmin(admin.ModelAdmin):
    form = MCQAdminForm
    list_display = ('question_number', 'subspecialty', 'exam_type', 'exam_year', 'correct_answer', 'has_image', 'get_report_count')
    list_filter = ('subspecialty', 'exam_type', 'exam_year', HasImageFilter, HasReportsFilter)
    search_fields = ('question_text', 'question_number', 'source_file')
    ordering = ('subspecialty', 'exam_year', 'question_number')
    inlines = [QuestionReportInline]
    
    class Media:
        css = {
            'all': ('admin/css/mcq_admin.css',)
        }
        js = ('admin/js/mcq_admin.js',)
    
    fieldsets = (
        ('Question Content', {
            'fields': ('question_text', 'options_text', 'correct_answer', 'image_url'),
            'description': '⚠️ IMPORTANT: For images, use Imgur.com or similar. Google Drive does NOT work! URL must end in .jpg/.png/.gif'
        }),
        ('Metadata', {
            'fields': ('subspecialty', 'exam_type', 'exam_year', 'question_number'),
        }),
        ('Source Information', {
            'fields': ('source_file',),
            'classes': ('collapse',),
        }),
        ('Explanation Sections', {
            'fields': (
                'conceptual_foundation',
                'pathophysiology',
                'clinical_correlation',
                'diagnostic_approach',
                'classification_neurology',
                'management_principles',
                'option_analysis',
                'clinical_pearls',
                'current_evidence',
                'explanation'
            ),
            'description': 'Edit each section of the explanation individually. Leave sections empty if not needed.',
            'classes': ('wide',)
        }),
        ('Advanced Fields', {
            'fields': ('verification_confidence', 'primary_category', 'secondary_category', 'key_concept', 'difficulty_level'),
            'classes': ('collapse',),
        }),
    )
    
    def get_report_count(self, obj):
        """Display the number of reports for this MCQ"""
        count = obj.reports.filter(status='pending').count()
        if count > 0:
            return f"{count} pending"
        return "0"
    get_report_count.short_description = 'Reports'
    get_report_count.admin_order_field = 'pending_report_count'
    
    def has_image(self, obj):
        """Display whether this MCQ has an image"""
        return bool(obj.image_url)
    has_image.boolean = True
    has_image.short_description = 'Has Image'
    has_image.admin_order_field = 'image_url'

    def get_queryset(self, request):
        """Annotate queryset with report count for sorting"""
        qs = super().get_queryset(request)
        return qs.annotate(pending_report_count=Count('reports', filter=Q(reports__status='pending')))
    
    def save_model(self, request, obj, form, change):
        # Set options from the processed form data
        if 'options' in form.cleaned_data:
            obj.options = form.cleaned_data['options']
        super().save_model(request, obj, form, change)

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('user', 'mcq', 'created_at')
    list_filter = ('user', 'created_at')
    search_fields = ('user__username', 'mcq__question_text')
    ordering = ('-created_at',)

@admin.register(Flashcard)
class FlashcardAdmin(admin.ModelAdmin):
    list_display = ('user', 'mcq', 'interval', 'next_review', 'last_reviewed')
    list_filter = ('user', 'next_review', 'last_reviewed')
    search_fields = ('user__username', 'mcq__question_text')
    ordering = ('next_review',)

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'mcq', 'created_at', 'updated_at')
    list_filter = ('user', 'created_at')
    search_fields = ('user__username', 'mcq__question_text', 'note_text')
    ordering = ('-updated_at',)

@admin.register(HiddenMCQ)
class HiddenMCQAdmin(admin.ModelAdmin):
    list_display = ('user', 'mcq', 'hidden_at')
    list_filter = ('user', 'hidden_at')
    search_fields = ('user__username', 'mcq__question_text')
    ordering = ('-hidden_at',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'expiration_date', 'is_active_override', 'is_expired', 'is_active', 'created_by')
    list_filter = ('is_active_override', 'expiration_date')
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('is_expired', 'is_active')
    actions = ['extend_30_days', 'extend_90_days', 'extend_365_days', 'deactivate_profiles', 'activate_profiles']
    
    def is_expired(self, obj):
        return obj.is_expired
    is_expired.boolean = True
    is_expired.short_description = 'Expired'
    
    def is_active(self, obj):
        return obj.is_active
    is_active.boolean = True
    is_active.short_description = 'Active'
    
    def extend_30_days(self, request, queryset):
        for profile in queryset:
            profile.extend_expiration(30)
        self.message_user(request, f"Extended {queryset.count()} profiles by 30 days")
    extend_30_days.short_description = "Extend selected profiles by 30 days"
    
    def extend_90_days(self, request, queryset):
        for profile in queryset:
            profile.extend_expiration(90)
        self.message_user(request, f"Extended {queryset.count()} profiles by 90 days")
    extend_90_days.short_description = "Extend selected profiles by 90 days"
    
    def extend_365_days(self, request, queryset):
        for profile in queryset:
            profile.extend_expiration(365)
        self.message_user(request, f"Extended {queryset.count()} profiles by 365 days")
    extend_365_days.short_description = "Extend selected profiles by 1 year"
    
    def deactivate_profiles(self, request, queryset):
        queryset.update(is_active_override=False)
        self.message_user(request, f"Deactivated {queryset.count()} profiles")
    deactivate_profiles.short_description = "Deactivate selected profiles"
    
    def activate_profiles(self, request, queryset):
        queryset.update(is_active_override=True)
        self.message_user(request, f"Activated {queryset.count()} profiles")
    activate_profiles.short_description = "Activate selected profiles"


@admin.register(QuestionReport)
class QuestionReportAdmin(admin.ModelAdmin):
    list_display = ('get_question_number', 'user', 'status', 'suggested_correct_answer', 'created_at')
    list_filter = ('status', 'created_at', 'suggested_correct_answer')
    search_fields = ('question__question_text', 'question__question_number', 'user__username', 'reason')
    readonly_fields = ('user', 'created_at', 'updated_at', 'get_question_display', 'get_options_display', 'get_current_answer', 'get_explanation_display')
    ordering = ('-created_at',)
    
    actions = ['mark_as_reviewed', 'mark_as_resolved', 'mark_as_rejected']
    
    def get_question_number(self, obj):
        from django.urls import reverse
        from django.utils.html import format_html
        
        url = reverse('admin:mcq_mcq_change', args=[obj.question.id])
        question_num = obj.question.question_number or f"ID: {obj.question.id}"
        
        return format_html('<a href="{}">{}</a>', url, question_num)
    get_question_number.short_description = 'Question #'
    get_question_number.allow_tags = True
    
    def get_question_display(self, obj):
        """Display the full question text"""
        return obj.question.question_text
    get_question_display.short_description = 'Question Text'
    
    def get_options_display(self, obj):
        """Display all answer options"""
        options = obj.question.get_options_dict()
        options_html = "<ul>"
        for key, value in sorted(options.items()):
            if key == obj.question.correct_answer:
                options_html += f"<li><strong>{key}.</strong> {value} <span style='color: green;'>(Current Answer)</span></li>"
            elif key == obj.suggested_correct_answer:
                options_html += f"<li><strong>{key}.</strong> {value} <span style='color: blue;'>(Suggested Answer)</span></li>"
            else:
                options_html += f"<li><strong>{key}.</strong> {value}</li>"
        options_html += "</ul>"
        return options_html
    get_options_display.short_description = 'Answer Options'
    get_options_display.allow_tags = True
    
    def get_current_answer(self, obj):
        """Display the current correct answer"""
        return obj.question.correct_answer
    get_current_answer.short_description = 'Current Correct Answer'
    
    def get_explanation_display(self, obj):
        """Display the current explanation if available"""
        if obj.question.explanation_sections:
            sections = obj.question.explanation_sections
            if 'option_analysis' in sections:
                return sections['option_analysis'][:500] + "..." if len(sections['option_analysis']) > 500 else sections['option_analysis']
        elif obj.question.explanation:
            return obj.question.explanation[:500] + "..." if len(obj.question.explanation) > 500 else obj.question.explanation
        return "No explanation available"
    get_explanation_display.short_description = 'Current Explanation'
    
    def mark_as_reviewed(self, request, queryset):
        updated = queryset.update(status='reviewed', reviewed_by=request.user)
        self.message_user(request, f"Marked {updated} reports as reviewed")
    mark_as_reviewed.short_description = "Mark selected reports as reviewed"
    
    def mark_as_resolved(self, request, queryset):
        updated = queryset.update(status='resolved', reviewed_by=request.user)
        self.message_user(request, f"Marked {updated} reports as resolved")
    mark_as_resolved.short_description = "Mark selected reports as resolved"
    
    def mark_as_rejected(self, request, queryset):
        updated = queryset.update(status='rejected', reviewed_by=request.user)
        self.message_user(request, f"Marked {updated} reports as rejected")
    mark_as_rejected.short_description = "Mark selected reports as rejected"
    
    def get_fieldsets(self, request, obj=None):
        fieldsets = [
            ('Report Information', {
                'fields': ('user', 'status', 'reviewed_by', 'created_at', 'updated_at')
            }),
            ('Question Details', {
                'fields': ('get_question_display', 'get_options_display', 'get_current_answer', 'get_explanation_display')
            }),
            ('User Report', {
                'fields': ('suggested_correct_answer', 'reason')
            }),
            ('Admin Notes', {
                'fields': ('admin_notes',)
            })
        ]
        return fieldsets
    
    def has_delete_permission(self, request, obj=None):
        # Only allow superusers to delete reports
        return request.user.is_superuser
    
    def save_model(self, request, obj, form, change):
        # Automatically set reviewed_by when status changes
        if change and 'status' in form.changed_data:
            obj.reviewed_by = request.user
        super().save_model(request, obj, form, change)