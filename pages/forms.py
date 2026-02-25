from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Registration, Course

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['full_name', 'email', 'phone_number', 'course', 'training_format', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': _('Your Full Name')
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': _('Email Address')
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': _('Phone Number (e.g. +250...)')
            }),
            'course': forms.Select(attrs={
                'class': 'form-input'
            }),
            'training_format': forms.Select(attrs={
                'class': 'form-input'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-input',
                'rows': 4,
                'placeholder': _('Any additional information or specific requirements?')
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ensure only active courses are shown
        self.fields['course'].queryset = Course.objects.filter(is_active=True)
        # Add labels if desired or rely on template labels
        self.fields['course'].empty_label = _("Select a Certification Program")
