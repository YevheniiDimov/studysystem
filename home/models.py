from django.db import models
from colorfield.fields import ColorField
from martor.models import MartorField
import uuid

"""Create Workspace model with name, description, date and color"""
class Workspace(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    forecolor = ColorField(default='#000000')
    backcolor = ColorField(default='#ffffff')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    user = models.ForeignKey('auth.User', null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
"""Create Document model with name, description, date and file"""
class Document(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    text = MartorField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name