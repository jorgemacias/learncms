"""learncms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.views.generic.list import ListView

from .models import Lesson
from .views import LessonDetailView, handler404, handler500

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^lesson/(?P<slug>[a-z\-]+)/$', LessonDetailView.as_view(), name='lesson-detail'),
    url(r'^/?$', ListView.as_view(template_name="index.html",model=Lesson), name='homepage'),
] 

# these only work if the URL does not have a protocol (i.e. local)
# otherwise, Django will save us
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
