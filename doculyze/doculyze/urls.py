
from django.contrib import admin
from django.urls import path
from web import views as web_views

from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from web.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', web_views.home, name='home'),
    path('basic-upload', BasicUploadView.as_view(),  name='basic_upload'),

]
