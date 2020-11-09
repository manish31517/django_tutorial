from django.contrib import admin
from django.urls import path, include
from home import views
# Django admin headerr customization
admin.site.site_header= "Devloper Manish"
admin.site.site_title = "Welcome to Manish's Dashboard"
admin.site.index_title = "Welcome to this portal"

urlpatterns = [
    path('',views.home, name ='home'),
    path('about',views.about, name='about'),
     path('project',views.projects, name ='project'),
      path('contacts',views.contacts, name ='contact'),
    
]
