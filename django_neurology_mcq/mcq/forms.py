"""
Forms for the MCQ application.
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import Q
from .models import QuestionReport, MCQ
import json

class CaseInsensitiveUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password, with case-insensitive username validation.
    """
    
    def clean_username(self):
        """
        Validate that the username is case-insensitively unique.
        """
        username = self.cleaned_data.get('username')
        if username and User.objects.filter(username__iexact=username).exists():
            self.add_error('username', 'A user with this username already exists (case-insensitive match).')
        return username
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username",)


class CaseInsensitiveAuthenticationForm(AuthenticationForm):
    """
    A form for authenticating users using the CaseInsensitiveModelBackend.
    This doesn't actually need any special logic since the authentication
    backend handles the case-insensitivity, but it's good to have for completeness.
    """
    pass


class QuestionReportForm(forms.ModelForm):
    """Form for users to report issues with questions."""
    
    class Meta:
        model = QuestionReport
        fields = ['suggested_correct_answer', 'reason']
        widgets = {
            'suggested_correct_answer': forms.RadioSelect(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')]),
            'reason': forms.Textarea(attrs={
                'rows': 6,
                'placeholder': 'Please explain why you think the current answer is wrong. Include any references or reasoning that supports your suggested answer.',
                'class': 'form-control'
            })
        }
        labels = {
            'suggested_correct_answer': 'What do you think is the correct answer?',
            'reason': 'Why do you think the current answer is wrong?'
        }


class MCQQuestionEditForm(forms.ModelForm):
    """Form for inline editing of MCQ question text."""
    
    class Meta:
        model = MCQ
        fields = ['question_text']
        widgets = {
            'question_text': forms.Textarea(attrs={
                'rows': 4,
                'class': 'form-control',
                'placeholder': 'Enter the question text...'
            })
        }
        labels = {
            'question_text': 'Question Text'
        }


class MCQOptionsEditForm(forms.Form):
    """Form for inline editing of MCQ options and correct answer."""
    
    option_a = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={
            'rows': 2,
            'class': 'form-control option-input',
            'placeholder': 'Option A'
        }),
        label='Option A'
    )
    
    option_b = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={
            'rows': 2,
            'class': 'form-control option-input',
            'placeholder': 'Option B'
        }),
        label='Option B'
    )
    
    option_c = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={
            'rows': 2,
            'class': 'form-control option-input',
            'placeholder': 'Option C'
        }),
        label='Option C'
    )
    
    option_d = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={
            'rows': 2,
            'class': 'form-control option-input',
            'placeholder': 'Option D'
        }),
        label='Option D'
    )
    
    correct_answer = forms.ChoiceField(
        choices=[
            ('A', 'A'),
            ('B', 'B'),
            ('C', 'C'),
            ('D', 'D'),
            ('A, B', 'A, B'),
            ('A, C', 'A, C'),
            ('A, D', 'A, D'),
            ('B, C', 'B, C'),
            ('B, D', 'B, D'),
            ('C, D', 'C, D'),
            ('A, B, C', 'A, B, C'),
            ('A, B, D', 'A, B, D'),
            ('A, C, D', 'A, C, D'),
            ('B, C, D', 'B, C, D'),
            ('A, B, C, D', 'A, B, C, D')
        ],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Correct Answer'
    )
    
    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance', None)
        super().__init__(*args, **kwargs)
        
        if instance and instance.options:
            # Pre-populate form with existing options
            for key, option in zip(['option_a', 'option_b', 'option_c', 'option_d'], instance.options[:4]):
                self.fields[key].initial = option
            
            # Set correct answer
            if instance.correct_answer:
                self.fields['correct_answer'].initial = instance.correct_answer
    
    def save(self, instance):
        """Save the form data to the MCQ instance."""
        # Update options
        options = [
            self.cleaned_data['option_a'],
            self.cleaned_data['option_b'],
            self.cleaned_data['option_c'],
            self.cleaned_data['option_d']
        ]
        instance.options = options
        
        # Update correct answer and correct answer text
        instance.correct_answer = self.cleaned_data['correct_answer']
        
        # Set correct answer text based on selected answer(s)
        correct_answer_letters = [letter.strip() for letter in instance.correct_answer.split(',')]
        correct_texts = []
        for letter in correct_answer_letters:
            index = ord(letter) - ord('A')
            if 0 <= index < len(options):
                correct_texts.append(options[index])
        instance.correct_answer_text = ', '.join(correct_texts) if correct_texts else ''
        
        instance.save()
        return instance


class MCQExplanationEditForm(forms.ModelForm):
    """Form for inline editing of MCQ explanation sections."""
    
    conceptual_foundation = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 3,
            'class': 'form-control',
            'placeholder': 'Core concepts about the topic...'
        }),
        required=False,
        label='1. Conceptual Foundation'
    )
    
    pathophysiology = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 3,
            'class': 'form-control',
            'placeholder': 'Brief concise review of pathophysiology or mechanism of action...'
        }),
        required=False,
        label='2. Pathophysiology'
    )
    
    clinical_correlation = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 3,
            'class': 'form-control',
            'placeholder': 'Deep analysis of the clinical presentation...'
        }),
        required=False,
        label='3. Clinical Correlation'
    )
    
    diagnostic_approach = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 3,
            'class': 'form-control',
            'placeholder': 'According to the latest guidelines...'
        }),
        required=False,
        label='4. Diagnostic Approach'
    )
    
    classification_neurology = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 3,
            'class': 'form-control',
            'placeholder': 'Brief updated classification and relation to similar disorders...'
        }),
        required=False,
        label='5. Classification and Neurology'
    )
    
    management_principles = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 3,
            'class': 'form-control',
            'placeholder': 'Brief concise updated management principles...'
        }),
        required=False,
        label='6. Management Principles'
    )
    
    option_analysis = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 3,
            'class': 'form-control',
            'placeholder': 'Compare options and explain why wrong answers are incorrect...'
        }),
        required=False,
        label='7. Option Analysis'
    )
    
    clinical_pearls = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 3,
            'class': 'form-control',
            'placeholder': 'Very high yield information related to the question...'
        }),
        required=False,
        label='8. Clinical Pearls'
    )
    
    current_evidence = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 3,
            'class': 'form-control',
            'placeholder': 'Latest guidelines and brief quotes related to the question...'
        }),
        required=False,
        label='9. Current Evidence'
    )
    
    class Meta:
        model = MCQ
        fields = []  # We'll handle the sections manually
    
    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance', None)
        super().__init__(*args, **kwargs)
        
        if instance and instance.explanation_sections:
            # Pre-populate form with existing explanation sections
            sections = instance.explanation_sections
            if isinstance(sections, str):
                try:
                    sections = json.loads(sections)
                except json.JSONDecodeError:
                    sections = {}
            
            self.fields['conceptual_foundation'].initial = sections.get('conceptual_foundation', '')
            self.fields['pathophysiology'].initial = sections.get('pathophysiological_mechanisms', sections.get('pathophysiology', ''))
            self.fields['clinical_correlation'].initial = sections.get('clinical_correlation', '')
            self.fields['diagnostic_approach'].initial = sections.get('diagnostic_approach', '')
            self.fields['classification_neurology'].initial = sections.get('classification_and_nosology', sections.get('classification_neurology', ''))
            self.fields['management_principles'].initial = sections.get('management_principles', '')
            self.fields['option_analysis'].initial = sections.get('option_analysis', '')
            self.fields['clinical_pearls'].initial = sections.get('clinical_pearls', '')
            self.fields['current_evidence'].initial = sections.get('current_evidence', '')
    
    def save(self, commit=True):
        """Save the form data to the MCQ instance."""
        instance = super().save(commit=False)
        
        # Update explanation sections with all 9 fields
        instance.explanation_sections = {
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
        
        if commit:
            instance.save()
        
        return instance


class MCQImageEditForm(forms.ModelForm):
    """Form for inline editing of MCQ image URL."""
    
    class Meta:
        model = MCQ
        fields = ['image_url']
        widgets = {
            'image_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://example.com/image.jpg or Google Drive URL'
            })
        }
        labels = {
            'image_url': 'Image URL'
        }
        help_texts = {
            'image_url': 'Enter a direct image URL or a Google Drive sharing link. Google Drive links will be automatically converted.'
        }
    
    def clean_image_url(self):
        """Validate the image URL."""
        url = self.cleaned_data.get('image_url')
        if url:
            # Basic URL validation
            if not (url.startswith('http://') or url.startswith('https://')):
                raise forms.ValidationError('Please enter a valid URL starting with http:// or https://')
        return url


class MCQFullEditForm(forms.ModelForm):
    """Comprehensive form for editing all MCQ fields at once."""
    
    # Override options field to use individual text inputs
    option_a = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
        label='Option A'
    )
    option_b = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
        label='Option B'
    )
    option_c = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
        label='Option C'
    )
    option_d = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
        label='Option D'
    )
    
    class Meta:
        model = MCQ
        fields = [
            'question_text', 'correct_answer', 'subspecialty', 
            'exam_type', 'exam_year', 'explanation', 'image_url'
        ]
        widgets = {
            'question_text': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'correct_answer': forms.Select(attrs={'class': 'form-control'}),
            'subspecialty': forms.TextInput(attrs={'class': 'form-control'}),
            'exam_type': forms.Select(attrs={'class': 'form-control'}),
            'exam_year': forms.TextInput(attrs={'class': 'form-control'}),
            'explanation': forms.Textarea(attrs={'rows': 6, 'class': 'form-control'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control'})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Set up correct answer choices
        self.fields['correct_answer'].widget = forms.Select(
            choices=[
                ('A', 'A'),
                ('B', 'B'),
                ('C', 'C'),
                ('D', 'D'),
                ('A, B', 'A, B'),
                ('A, C', 'A, C'),
                ('A, D', 'A, D'),
                ('B, C', 'B, C'),
                ('B, D', 'B, D'),
                ('C, D', 'C, D'),
                ('A, B, C', 'A, B, C'),
                ('A, B, D', 'A, B, D'),
                ('A, C, D', 'A, C, D'),
                ('B, C, D', 'B, C, D'),
                ('A, B, C, D', 'A, B, C, D')
            ],
            attrs={'class': 'form-control'}
        )
        
        # Pre-populate options if instance exists
        if self.instance and self.instance.options:
            for key, option in zip(['option_a', 'option_b', 'option_c', 'option_d'], self.instance.options[:4]):
                self.fields[key].initial = option
    
    def save(self, commit=True):
        """Save the form data including options."""
        instance = super().save(commit=False)
        
        # Update options
        instance.options = [
            self.cleaned_data['option_a'],
            self.cleaned_data['option_b'],
            self.cleaned_data['option_c'],
            self.cleaned_data['option_d']
        ]
        
        # Update correct answer text
        correct_answer_letters = [letter.strip() for letter in instance.correct_answer.split(',')]
        correct_texts = []
        for letter in correct_answer_letters:
            index = ord(letter) - ord('A')
            if 0 <= index < len(instance.options):
                correct_texts.append(instance.options[index])
        instance.correct_answer_text = ', '.join(correct_texts) if correct_texts else ''
        
        if commit:
            instance.save()
        
        return instance