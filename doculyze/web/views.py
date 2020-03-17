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
#from doculyze import doculyze

from .forms import DocumentForm
from .models import Document

def home(request):
    return render(request, 'web/home.html')



class BasicUploadView(View):
    def get(self, request):
        document_list = Document.objects.all()
        return render(self.request, 'web/home.html', {'documents': document_list})

    def post(self, request):
        form = DocumentForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            document = form.save()
            data = {'is_valid': True, 'name': document.file.name, 'url': document.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)