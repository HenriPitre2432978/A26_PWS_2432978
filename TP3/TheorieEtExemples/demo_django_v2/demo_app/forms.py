from django import forms
from django.core.exceptions import ValidationError

from .models import Category, Product


"""
class CategoryForm(forms.Form):
  name = forms.CharField(max_length=50, label="Nom")
"""

class CategoryForm(forms.ModelForm):
  template_name = "demo_app/snippets/form_snippet.html"

  class Meta:
    model = Category
    fields = "__all__"
    #fields = ['name']
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control'}),
    }
  
  def clean_name(self):
    name = self.cleaned_data['name']

    if self.instance.pk is None:
      name_exists = Category.objects.filter(name=name).exists()
    else:
      name_exists = Category.objects.filter(name=name).exclude(id=self.instance.pk).exists()

    if name_exists:
      raise ValidationError("Le nom de catégorie existe déjà")
    
    return name


class ProductForm(forms.ModelForm):
  template_name = "demo_app/snippets/form_snippet.html"
  
  class Meta:
    model = Product
    fields = ['code', 'name', 'active', 'quantity', 'category', 'image']
    widgets = {
      'code': forms.TextInput(attrs={'class': 'form-control'}),
      'name': forms.TextInput(attrs={'class': 'form-control'}),
      'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
      'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
      'category': forms.Select(attrs={'class': 'form-control'}),
    }

  def clean_code(self):
    code = self.cleaned_data['code']

    if self.instance.pk is None:
      code_exists = Product.objects.filter(code=code).exists()
    else:
      code_exists = Product.objects.filter(code=code).exclude(id=self.instance.pk).exists()

    if code_exists:
      raise ValidationError("Le code de produit existe déjà")

    return code

  def clean_name(self):
    name = self.cleaned_data['name']

    if self.instance.pk is None:
      name_exists = Product.objects.filter(name=name).exists()
    else:
      name_exists = Product.objects.filter(name=name).exclude(id=self.instance.pk).exists()

    if name_exists:
      raise ValidationError("Le nom de produit existe déjà")

    return name