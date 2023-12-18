from django import forms
from .models import Document
from django.apps import apps


Resident = apps.get_model('CreateAccount','Resident')


class ResidentRegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    first_name = forms.CharField(widget=forms.TextInput, label="Firstname")
    last_name = forms.CharField(widget=forms.TextInput, label="Lastname")
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Birth date")
    present_address = forms.CharField(widget=forms.TextInput, label="Present Address")
    user_type = forms.CharField(widget=forms.HiddenInput, initial='R')

    class Meta:
        model = Resident
        fields = ['username', 'password', 'first_name', 'last_name', 'birth_date', 'present_address', 'user_type']


class DocumentForm(forms.ModelForm):
    residentName = forms.ModelChoiceField(
        queryset=Resident.object.all(),
        widget=forms.HiddenInput,
        required=False, label="Resident Name"
    )
    doc_type = forms.CharField(
            max_length=1,
            widget=forms.Select(choices=Document.CHOICES),
            label="Document Type"
    )
    fee = forms.FloatField(default=0)

    class Meta:
        model = Document
        fields = ['residentName', 'doc_type']


