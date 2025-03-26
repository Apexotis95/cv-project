# cv_app/forms.py
from django import forms
from .models import PersonalInfo, Skill, Experience, Education, LanguageInterest

# Form for PersonalInfo
class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ['name', 'email', 'phone', 'address', 'nationality']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

# Form for Skill
class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skills']
        widgets = {
            'skills': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

# Form for Experience
class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['position', 'company', 'period']

# Form for Education
class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'institution', 'period']

# Form for LanguageInterest
class LanguageInterestForm(forms.ModelForm):
    class Meta:
        model = LanguageInterest
        fields = ['languages', 'interests']
        widgets = {
            'languages': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'interests': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
