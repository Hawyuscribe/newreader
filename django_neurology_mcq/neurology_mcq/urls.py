"""
URL configuration for neurology_mcq project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Import the trigger view
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from trigger_import_view import trigger_import_view
from .health import healthz

urlpatterns = [
    path('healthz/', healthz, name='healthz'),
    path('admin/import-mcqs/', trigger_import_view, name='trigger_import'),
    path('', include('mcq.urls')),
    path('admin/', admin.site.urls),
]

# Add static URL mapping in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
