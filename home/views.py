from django.shortcuts import render
from .models import Workspace, Document
from .forms import WorkspaceForm
import datetime

def index(request):
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

def workspace(request, workspace):
    workspace = Workspace.objects.filter(id=workspace).first()
    documents = Document.objects.filter(workspace=workspace)
    return render(request, "workspace.html", context={"workspace": workspace, "documents": documents, "message": ""})
    