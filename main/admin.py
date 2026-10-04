from django.contrib import admin
from .models import *
"""
Django Admin

Django Admin is a powerful feature for managing data models via a friendly UI.

Key topics covered:
- Registering models with the admin site
- Customizing the admin interface
- Adding search and filters
- Inline model administration

"""

"""
To create a superuser type in the terminal:
python manage.py createsuperuser
"""

"""
Registering Models

Django Admin requires models to be registered for them to 
appear in the admin interface.
We can do that with 'admin.site.register(Model)'.
"""

admin.site.register(Author)
admin.site.register(Book)