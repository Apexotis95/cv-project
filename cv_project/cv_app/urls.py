from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('personal-info/', views.personal_info_list, name='personal_info_list'),
    path('skills/', views.skill_list, name='skill_list'),
    path('experiences/', views.experience_list, name='experience_list'),
    path('educations/', views.education_list, name='education_list'),
    path('language-interests/', views.language_interest_list, name='language_interest_list'),
]
