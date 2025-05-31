from django import forms
from .models import StudyGroup

class StudyGroupForm(forms.ModelForm):
    meeting_times = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    class Meta:
        model = StudyGroup
        fields = ['title', 'description', 'subject', 'meeting_times', 'location', 'is_active', 'max_members']
