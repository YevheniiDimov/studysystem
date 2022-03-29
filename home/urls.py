from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('workspace/<uuid:workspace>', views.workspace, name='workspace'),
]