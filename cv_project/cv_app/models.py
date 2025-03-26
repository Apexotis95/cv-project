from django.db import models

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    nationality = models.CharField(max_length=50)

class Skill(models.Model):
    skills = models.TextField()

class Experience(models.Model):
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    period = models.CharField(max_length=50)

class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    period = models.CharField(max_length=50)

class LanguageInterest(models.Model):
    languages = models.TextField()
    interests = models.TextField()
