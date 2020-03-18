from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.views import View
from django.http import JsonResponse
from .doculyze import Doculyze

from .forms import DocumentForm, DocumentTempFormset 
from .models import Document


def home(request):

    if request.method == 'GET':
        formset = DocumentTempFormset(request.GET or None)
    return render(request, 'web/home.html', {'formset': formset})

class AnalyzeView(View):    
    def post(self, request):
        formset = DocumentTempFormset(request.POST)
        if formset.is_valid():
            files_list = []
            try:
                for form in formset:
                    form = form.cleaned_data
                    if form['name']:
                        doc_name = form['name'].replace("documents/", "")
                        files_list.append(doc_name)                
            except KeyError:
                pass
            analyze = Doculyze(files_list)
            data = analyze.get_data()     
            #print (data)       
            return render(self.request, 'web/analyze.html', {'data': data})
        

class BasicUploadView(View):
    # def get(self, request):
    #     print("here")
    #     document_list = Document.objects.all()
    #     print (document_list)
    #     return render(self.request, 'web/home.html', {'documents': document_list})

    def post(self, request):
        form = DocumentForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            document = form.save()
            data = {'is_valid': True, 'name': document.file.name, 'url': document.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)