# Raw Django to Serialize Models
# Better to use serializer.py with djangoRestFramework


from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
        ]
