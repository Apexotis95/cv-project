from django.contrib import admin
from .models import PersonalInfo, Skill, Experience, Education, LanguageInterest

admin.site.register(PersonalInfo)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(LanguageInterest)
