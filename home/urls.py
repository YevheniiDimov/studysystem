from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('workspace/<uuid:workspace>', views.workspace, name='workspace'),
    path('workspace/<uuid:workspace>/document/<uuid:document>', views.document, name='document'),
    path('workspace/<uuid:workspace>/<str:action>', views.workspace_action, name='workspace_action'),
    path('workspace/<uuid:workspace>/document/<uuid:document>/<str:action>', views.document_action, name='document_action'),
]