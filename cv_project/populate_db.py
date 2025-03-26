
import os
import django

# Step 1: Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cv_project.settings")
django.setup()  # This ensures Django is initialized before importing models

# Step 2: Import models (after django.setup())
from cv_app.models import PersonalInfo, Skill, Experience, Education, LanguageInterest

# Step 3: Populate Personal Info
PersonalInfo.objects.get_or_create(
    name="OTIS IDAHOH",
    email="idahohotis123@gmail.com",
    phone="07 58 82 35 47",
    address="31 Rue du tiers pot, 95140 GARGES LES GONESSE, France",
    nationality="Nigérian"
)

# Step 4: Populate Skills
Skill.objects.get_or_create(
    skills="Expert WiFi, Installation de fibres optiques, Dépannage, CAO, Analyse de pannes, Normes de sécurité, Electrical Installation & Maintenance, Web Development (Python, Django), Sound Engineering, DevOps (Basic), Network Troubleshooting, Computer-Aided Design (CAO), Network Analysis Tools, Troubleshooting Hardware/Software Failures"
)

# Step 5: Populate Experience
Experience.objects.bulk_create([
    Experience(position="Technicien de son", company="Jhfan Hôtel Renaissance", period="2021-Present"),
    Experience(position="Stage Developer Web", company="Le Garage Numérique", period="Juillet 2024 - Août 2024"),
    Experience(position="Installation de la fibre", company="Jfibre", period="Fév 2023 - Nov 2023"),
    Experience(position="Installation de câbles électriques", company="A.EJ Montsoult", period="Nov 2018 - Déc 2021"),
])

# Step 6: Populate Education
Education.objects.bulk_create([
    Education(degree="Formation DSP Bac+1 + DevOps", institution="CNAM", period="Avr 2024 - Août 2024"),
    Education(degree="Brevet spécialiste WiFi", institution="Circet", period="Juin 2023"),
    Education(degree="Maintenance Réseaux et Fibre Optique", institution="Hub Nikola Tesla", period="Juil 2022 - Déc 2022"),
    Education(degree="Bac Pro MELEC", institution="Lycée Louis Jouvet", period="2018-2021"),
])

# Step 7: Populate Languages & Interests
LanguageInterest.objects.get_or_create(
    languages="Français, Anglais (Bilingue)",
    interests="Musique (afrobeat, batterie 5 ans), Football (17 ans), Danse (afro)"
)

print("✅ CV successfully added to the database.")
