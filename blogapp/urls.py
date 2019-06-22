
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('home/', views.home, name='bloghome'),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('new/',views.new, name='new' ),
    path('create/', views.create, name="create"),
]
