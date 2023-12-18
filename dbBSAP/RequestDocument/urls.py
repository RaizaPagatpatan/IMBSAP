
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('login', views.login, name='login'),
    path('register', views.RegisterResident.as_view(), name='register'),
    path('document_req', views.document_req, name='document_req')
]
