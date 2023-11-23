from django import forms
from veterinaria.models import Usuario, TipoUsuario, Cliente, Ficha_clinica, Atencion

class ClienteForm(forms.ModelForm):
    rut = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '12345678-9'}))
    nombres = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Juan Ignacio'}))
    apellidos = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Gonzalez Perez'}))
    fono_1 = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '9 12345678'}))
    fono_2 = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '9 12345678'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@dom.cl'}))


    class Meta:
        model = Cliente
        fields = '__all__'

class AtencionForm(forms.ModelForm):
    hora_ingreso = forms.TimeField(widget=forms.TimeInput(attrs={'class':'form-control','type': 'time'}))
    hora_termino = forms.TimeField(widget=forms.TimeInput(attrs={'class':'form-control','type': 'time'}))
    diagnostico = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Ingrese Diagnostico'}))
    tratamiento = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Ingrese Tratamiento'}))
    observaciones = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Ingrese Observaciones'}))
    fecha_atencion = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','placeholder': 'Día/Mes/Año', 'type': 'date'}))
    id_ficha_clinica = forms.ModelChoiceField(
        queryset=Ficha_clinica.objects.all(),
        empty_label="Selecciona ficha clínica",
        widget=forms.Select(attrs={'class':'form-select'}),
        label="Ficha Clínica"
    )
    id_veterinario = forms.ModelChoiceField(
        queryset=Usuario.objects.filter(),
        empty_label="Selecciona veterinario",
        widget=forms.Select(attrs={'class':'form-select'}),
        label="Veterinario"
    )

    class Meta:
        model = Atencion
        fields = '__all__'