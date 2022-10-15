from django.urls import path
from . import views

urlpatterns = [
    path('newsletter_list/', views.newsletter_list, name='newsletter_list'),
]
