from django.shortcuts import redirect, render
from .models import Workspace, Document
from .forms import WorkspaceForm, DocumentForm, AuthorizationForm
from django.contrib.auth import authenticate
import datetime

def index(request):
    if request.user.is_authenticated:
        workspaces = Workspace.objects.filter(user=request.user)
        context = {"workspaces": workspaces, "form": WorkspaceForm(), "message": "", "message_color": ""}
        
        if request.method == 'POST':
            form = WorkspaceForm(request.POST)
            if form.is_valid():
                workspace = Workspace(name = form.cleaned_data['name'], description = form.cleaned_data['description'], date = datetime.datetime.now().date(), forecolor = form.cleaned_data['forecolor'], backcolor = form.cleaned_data['backcolor'], user = request.user)
                workspace.save()
                
                context["message"] = "Workspace created successfully!"
                context["message_color"] = "text-success"
            else:
                context["message"] = "Workspace creation failed!"
                context["message_color"] = "text-danger"

        return render(request, "home.html", context=context)
    else:
        return redirect('/accounts/login')

def workspace(request, workspace):
    workspace = Workspace.objects.filter(id=workspace).first()
    documents = Document.objects.filter(workspace=workspace)
    context = {"workspace": workspace, "documents": documents, "form": DocumentForm(), "message": ""}
    
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            document = Document(name = form.cleaned_data['name'], description = form.cleaned_data['description'], date = datetime.datetime.now().date(), file = form.cleaned_data['file'], user = request.user)
            document.save()
            
            context["message"] = "Document created successfully!"
            context["message_color"] = "text-success"
        else:
            context["message"] = "Document creation failed!"
            context["message_color"] = "text-danger"
    
    return render(request, "workspace.html", context=context)
    