# forms.py
from django import forms
from .models import Menu, MenuItem

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name']

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'url']
