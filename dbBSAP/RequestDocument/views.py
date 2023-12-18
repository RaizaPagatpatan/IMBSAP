from django.shortcuts import render, redirect
from django.apps import apps
from django.views import View

from .forms import *
from .models import DocumentRequest

Resident = apps.get_model('CreateAccount', 'Resident')


def document_req(request):
    return render(request, 'request_doc.html',{})


def home_view(request):
    return render(request, 'home.html', {})


def register(request):
    # Your view logic here
    return render(request, 'registration.html', {})


def login(request):
    return render(request, 'index.html', {})


class RegisterResident(View):
    template = 'registration.html'

    def get(self, request):
        register = ResidentRegisterForm()
        return render(request, self.template, {'form': register})

    def post(self, request):
        register = ResidentRegisterForm(request.POST)
        username = request.POST['username']
        message = 'Success'
        try:
            Resident.objects.get(username=username)
            message = 'Username Not Available'
        except Resident.DoesNotExist:
            register.save()
            return redirect('login')
        return render(request,self.template, {'form': register,'error_message': message})
