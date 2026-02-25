from django import forms
from .models import Registration, Course

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['full_name', 'email', 'phone_number', 'course', 'training_format', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Your Full Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'Email Address'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Phone Number (e.g. +250...)'
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
                'placeholder': 'Any additional information or specific requirements?'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ensure only active courses are shown
        self.fields['course'].queryset = Course.objects.filter(is_active=True)
        # Add labels if desired or rely on template labels
        self.fields['course'].empty_label = "Select a Certification Program"
