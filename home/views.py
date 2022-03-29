from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import Workspace, Document
from .forms import WorkspaceForm, DocumentForm
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
            document = Document(name = form.cleaned_data['name'], description = form.cleaned_data['description'], date = datetime.datetime.now().date(), text = "", workspace = workspace)
            document.save()
            
            context["message"] = "Document created successfully!"
            context["message_color"] = "text-success"
        else:
            print(form.errors)
            context["message"] = "Document creation failed!"
            context["message_color"] = "text-danger"
    
    return render(request, "workspace.html", context=context)

def document(request, workspace, document):
    workspace = Workspace.objects.filter(id=workspace).first()
    document = Document.objects.filter(id=document).first()
    
    form = DocumentForm()
    form.name = document.name
    form.description = document.description
    form.text = document.text
    
    if request.GET.get('action') != None:
        if request.GET.get('action') == "delete":
            document.delete()
            return redirect('/home/workspace/' + workspace.id)
        if request.GET.get('action') == "save":
            document.text = request.GET.get('text')
    
    context = {"workspace": workspace, "document": document, "form": form, "text": form.text}
    
    return render(request, "document.html", context=context)

def document_action(request, workspace, document, action):
    workspace = Workspace.objects.filter(id=workspace).first()
    document = Document.objects.filter(id=document).first()
    
    try:
        if action == "delete":
            document.delete()
            return JsonResponse({"status": "Document was successfuly deleted", "status_color": "text-success"});
        if action == "save":
            if len(request.GET.get('text')) > 0:
                print("+---Texts---+")
                print(request.GET.get('text'))
                document.text = request.GET.get('text')
                print(document.text)
                document.save()
                return JsonResponse({"status": "Text was successfuly saved", "status_color": "text-success"});
            else:
                return JsonResponse({"status": "Text is empty", "status_color": "text-danger"});
        else:
            return JsonResponse({"status": "Unknown action " + action, "status_color": "text-danger"});
    except:
        return JsonResponse({"status": "Something went wrong", "status_color": "text-danger"});