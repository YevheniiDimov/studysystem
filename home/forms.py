from django import forms
from .models import Workspace

class WorkspaceForm(forms.Form):
    """Create a form for workspace creation"""
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=250)
    forecolor = forms.CharField(widget=forms.TextInput(attrs={'type': 'color', 'value': '#FFFFFF'}))
    backcolor = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))