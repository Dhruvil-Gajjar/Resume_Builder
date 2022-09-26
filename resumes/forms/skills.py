from django import forms

from resumes.models import Skills


class SkillForm(forms.ModelForm):

    class Meta:
        model = Skills
        fields = ('skill_name',)

        widgets = {
            'skill_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Skill'}),
        }
