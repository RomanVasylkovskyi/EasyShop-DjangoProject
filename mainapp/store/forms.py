from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'price', 'description', 'category', 'author', 'cover_type',
            'format', 'illustrations', 'publisher', 'language', 'pages',
            'year_published', 'isbn', 'weight', 'sections'
        ]