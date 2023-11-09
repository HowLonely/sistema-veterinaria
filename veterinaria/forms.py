from django import forms
from veterinaria.models import Clientes, Asistentes, FichasClinicas, Veterinarios

class ClienteForm(forms.ModelForm):
    rut = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '12345678-9'}))

    class Meta:
        model = Clientes
        fields = '__all__'
