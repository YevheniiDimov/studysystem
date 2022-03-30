from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import Workspace, Document
from .forms import WorkspaceForm, DocumentForm, FileForm
from django.contrib.auth.decorators import login_required
import datetime

@login_required
def index(request):
    if request.user.is_authenticated:
        workspaces = Workspace.objects.filter(user=request.user)
        context = {"workspaces": workspaces, "form": WorkspaceForm(), "message": "", "message_color": ""}
        
        if request.method == 'POST':
            form = WorkspaceForm(request.POST)
            if form.is_valid():
                workspace = Workspace(name = form.cleaned_data['name'], date = datetime.datetime.now().date(), forecolor = form.cleaned_data['forecolor'], backcolor = form.cleaned_data['backcolor'], user = request.user)
                workspace.save()
                
                context["message"] = "Workspace created successfully!"
                context["message_color"] = "text-success"
            else:
                context["message"] = "Workspace creation failed!"
                context["message_color"] = "text-danger"

        return render(request, "home.html", context=context)
    else:
        return redirect('/accounts/login')

@login_required
def workspace(request, workspace):
    workspace = Workspace.objects.filter(id=workspace).first()
    
    if workspace.user != request.user:
        return render(request, "error.html", context={"message": "You are not allowed to access this workspace!"})
    
    documents = Document.objects.filter(workspace=workspace)
    context = {"workspace": workspace, "documents": documents, "form": DocumentForm(), "file_form": FileForm(), "message": ""}
    
    if request.method == 'POST':
        if request.FILES.get('file') != None:
            text = request.FILES.get('file').read().decode('utf-8');
            document = Document(name = request.FILES.get('file').name, date = datetime.datetime.now().date(), text = text, workspace = workspace)
            document.save()
        else:
            form = DocumentForm(request.POST)
            
            if form.is_valid():
                document = Document(name = form.cleaned_data['name'], date = datetime.datetime.now().date(), text = "", workspace = workspace)
                document.save()
                
                context["message"] = "Document created successfully!"
                context["message_color"] = "text-success"
            else:
                print(form.errors)
                context["message"] = "Document creation failed!"
                context["message_color"] = "text-danger"
    
    return render(request, "workspace.html", context=context)

@login_required
def workspace_action(request, workspace, action):
    workspace = Workspace.objects.filter(id=workspace).first()
    
    if workspace.user != request.user:
        return render(request, "error.html", context={"message": "You are not allowed to access this workspace!"})
    
    try:
        if action == "delete":
            workspace.delete()
            return JsonResponse({"status": "Workspace was successfuly deleted", "status_color": "text-success"});
        if action == "name":
            if len(request.GET.get('name')) > 0:
                workspace.name = request.GET.get('name')
                workspace.save()
                return JsonResponse({"status": "Name was successfuly changed", "status_color": "text-success"});
            else:
                return JsonResponse({"status": "Name is empty", "status_color": "text-danger"});
        else:
            return JsonResponse({"status": "Unknown action " + action, "status_color": "text-danger"});
    except:
        return JsonResponse({"status": "Something went wrong", "status_color": "text-danger"});

@login_required
def document(request, workspace, document):
    workspace = Workspace.objects.filter(id=workspace).first()
    document = Document.objects.filter(id=document).first()
    
    if workspace.user != request.user or document.workspace != workspace:
        return render(request, "error.html", context={"message": "You are not allowed to access this document!"})
    
    form = DocumentForm()
    form.name = document.name
    form.text = document.text
    
    if request.GET.get('action') != None:
        if request.GET.get('action') == "delete":
            document.delete()
            return redirect('/home/workspace/' + workspace.id)
        if request.GET.get('action') == "save":
            document.text = request.GET.get('text')
    
    context = {"workspace": workspace, "document": document, "form": form, "text": form.text}
    
    return render(request, "document.html", context=context)

@login_required
def document_action(request, workspace, document, action):
    workspace = Workspace.objects.filter(id=workspace).first()
    document = Document.objects.filter(id=document).first()
    
    if workspace.user != request.user or document.workspace != workspace:
        return render(request, "error.html", context={"message": "You are not allowed to access this document!"})
    
    try:
        if action == "delete":
            document.delete()
            return JsonResponse({"status": "Document was successfuly deleted", "status_color": "text-success"});
        if action == "save":
            if len(request.GET.get('text')) > 0:
                document.text = request.GET.get('text')
                document.save()
                return JsonResponse({"status": "Text was successfuly saved", "status_color": "text-success"});
            else:
                return JsonResponse({"status": "Text is empty", "status_color": "text-danger"});
        if action == "name":
            if len(request.GET.get('name')) > 0:
                document.name = request.GET.get('name')
                document.save()
                return JsonResponse({"status": "Name was successfuly changed", "status_color": "text-success"});
            else:
                return JsonResponse({"status": "Name is empty", "status_color": "text-danger"});
        else:
            return JsonResponse({"status": "Unknown action " + action, "status_color": "text-danger"});
    except:
        return JsonResponse({"status": "Something went wrong", "status_color": "text-danger"});