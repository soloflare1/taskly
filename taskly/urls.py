# taskly/urls.py

from django.urls import path, include

urlpatterns = [
    path("tasks/", include("tasks.urls"))
]