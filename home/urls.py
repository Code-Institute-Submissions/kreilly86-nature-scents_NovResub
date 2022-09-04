from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('philosophy/', views.philosophy, name='philosophy'),
]
