from django.forms import ModelForm, TextInput, DecimalField,ImageField, Select

from apps.product.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'category', 'image', 'quantity', 'brief_description', 'price']
       