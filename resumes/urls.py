from django.urls import path
from resumes.views import *


urlpatterns = [
    # Add/Edit
    path('profiles/add/', manage_profile, name='add_profile'),
    path('profiles/edit/<uuid:uid>/', manage_profile, name='edit_profile'),
]
