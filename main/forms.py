from django.forms import ModelForm
from .models import *
from django import forms
import datetime
"""
Forms allow to collect, validate, and process 
data input in Django applications. 
They allow you to define fields for entered data, 
specify validation rules, and handle data sending securely.
"""

class AuthorForm(ModelForm):
    """
    'Meta' is an inner Django model class used to define metadata and
    configuration options that control how the model behaves in the
    database and Django ORM (e.g., ordering, table name, constraints).
    """
    class Meta:
        # Specifying a model for a form
        model = Author

        # Displaying all fields of a form
        fields = '__all__'
    birth_date = forms.DateField(initial=datetime.date.today,
                                 widget=forms.DateInput(attrs={'type': 'date'}))
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'price' : forms.NumberInput(attrs={'min': '0'}),
        }
    publication_date = forms.DateField(initial=datetime.date.today,
                           widget=forms.DateInput(attrs={'type':'date'}))
class LetterForm(ModelForm):
    class Meta:
        model = Letter
        fields = '__all__'

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'