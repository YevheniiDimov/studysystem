from django import forms
from .models import Workspace, Document

class WorkspaceForm(forms.Form):
    """Create a form for workspace creation"""
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=250)
    forecolor = forms.CharField(widget=forms.TextInput(attrs={'type': 'color', 'value': '#FFFFFF'}))
    backcolor = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))
    
class DocumentForm(forms.Form):
    """Create a form for document creation"""
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=250)
    file = forms.FileField()
    
class AuthorizationForm(forms.Form):
    """Create a form for user authorization"""
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)