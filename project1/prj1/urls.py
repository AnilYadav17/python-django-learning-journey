
from django.contrib import admin
from django.urls import path


#for connect view to url
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about/', views.about),
    path('entry1/', views.entry1),
    path('entry2/', views.entry2),
    path('entry11/', views.entry11),
    path('entry3/', views.entry3),
    path('entry4/', views.entry4),
    path('entry5/', views.entry5),
]


