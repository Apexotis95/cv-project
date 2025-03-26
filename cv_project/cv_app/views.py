from django.shortcuts import render
from .models import PersonalInfo, Skill, Experience, Education, LanguageInterest

# View to list personal information
def personal_info_list(request):
    personal_info = PersonalInfo.objects.all()
    return render(request, 'cv_app/personal_info_list.html', {'personal_info': personal_info})

# View to list skills
def skill_list(request):
    skills = Skill.objects.all()
    return render(request, 'cv_app/skill_list.html', {'skills': skills})

# View to list experiences
def experience_list(request):
    experiences = Experience.objects.all()
    return render(request, 'cv_app/experience_list.html', {'experiences': experiences})

# View to list education
def education_list(request):
    educations = Education.objects.all()
    return render(request, 'cv_app/education_list.html', {'educations': educations})

# View to list languages and interests
def language_interest_list(request):
    language_interests = LanguageInterest.objects.all()
    return render(request, 'cv_app/language_interest_list.html', {'language_interests': language_interests})

# View for homepage
def home(request):
    return render(request, 'cv_app/home.html')
