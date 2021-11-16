"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from core.views import *
from django.views.generic import TemplateView
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('wel/', ReactView.as_view(), name="something"),
    path('post/', ReactView2.as_view(), name="somethingmore"),
    path('smail/', ReactView3.as_view(), name="somethingmore1"),
    path('feed/', ReactView4.as_view(), name="somethingmore2"),
    path('subh/', ReactView5.as_view(), name="somethingmore3"),

    path('abc/' , dashboard_internview.as_view(), name = "somethin3"),
    path('com/' , commentview.as_view(), name = "somethin4"),
    path('log/' , login_view.as_view(), name = "somethin5"),
    path('subd/' , data_update_view.as_view(), name = "somethin6"),
    path('logo/' , logout1.as_view(), name = "somethin6"),



    re_path("", TemplateView.as_view(template_name="index.html")),


    url(r'^media/(?P<path>.*)$', serve,{'document_root':  settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 


]
