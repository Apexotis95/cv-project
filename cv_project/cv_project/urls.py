"""
URL configuration for cv_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# cv_project/urls.py
# cv_project/urls.py
from django.contrib import admin
from django.urls import path, include
from cv_app import views  # Import the views from your cv_app

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel URL

    # Homepage URL (maps to the home view in cv_app)
    path('', views.home, name='home'),

    # Include URLs from cv_app (app-specific URLs)
    path('cv/', include('cv_app.urls')),
]
