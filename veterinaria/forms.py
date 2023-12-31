from django import forms
from veterinaria.models import CustomUser, TipoUsuario, Cliente, FichaClinica, Atencion, Raza

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
    
    def clean_nombres(self):
        nombres = self.cleaned_data.get('nombres')

        if nombres and not nombres.isalpha() and ' ' not in nombres:
            raise forms.ValidationError("El nombre debe tener solo letras y espacios")
        
        return nombres

    def clean_apellidos(self):
        apellidos = self.cleaned_data.get('apellidos')

        if apellidos and not apellidos.isalpha() and ' ' not in apellidos:
            raise forms.ValidationError("El nombre debe tener solo letras y espacios")
        
        return apellidos

class FichaForm(forms.ModelForm):

    opciones_sexo = {
        (0, 'Hembra'),
        (1, 'Macho'),
    }

    nombre_mascota = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pepito'}))
    num_chip = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '123456'}))
    edad_meses = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '32'}))
    sexo = forms.ChoiceField(choices=opciones_sexo, widget=forms.Select(attrs={'class': 'form-select'}))
    imagen = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}), required=False, label='Imagen')
    id_raza = forms.ModelChoiceField(
        queryset=Raza.objects.all(),
        empty_label="Selecciona raza",
        widget=forms.Select(attrs={'class':'form-select'}),
        label="Raza"
    )
    id_cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(),
        empty_label="Selecciona cliente",
        widget=forms.Select(attrs={'class':'form-select'}),
        label="Dueño"
    )

    def clean_nombre_mascota(self):
        nombre = self.cleaned_data.get('nombre_mascota')

        if nombre and not nombre.isalpha() and ' ' not in nombre:
            raise forms.ValidationError("El nombre de la mascota debe tener solo letras y espacios")
        
        return nombre

    def clean_edad_meses(self):
        edad = self.cleaned_data.get('edad_meses')

        try:
            edad = int(edad)
        except ValueError:
            raise forms.ValidationError("Edad debe ser un número entero")
        
        if edad < 0:
            raise forms.ValidationError("Edad debe ser mayor que 0")
        
        return edad
    
    class Meta:
        model = FichaClinica
        fields = '__all__'

class AtencionForm(forms.ModelForm):
    hora_ingreso = forms.TimeField(widget=forms.TimeInput(attrs={'class':'form-control','type': 'time'}), required=True)
    hora_termino = forms.TimeField(widget=forms.TimeInput(attrs={'class':'form-control','type': 'time'}), required=True)
    diagnostico = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'Ingrese Diagnostico', 'rows': '2'}), required=False)
    tratamiento = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'Ingrese Tratamiento', 'rows': '2'}), required=False)
    observaciones = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'Ingrese Observaciones', 'rows': '2'}), required=False)
    fecha_atencion = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','placeholder': 'Día/Mes/Año', 'type': 'date'}), required=True)
    id_mascota = forms.ModelChoiceField(
        queryset=FichaClinica.objects.all(),
        empty_label="Selecciona ficha clínica",
        widget=forms.Select(attrs={'class':'form-select'}),
        label="Ficha Clínica",
        required=False
    )
    id_veterinario = forms.ModelChoiceField(
        queryset=CustomUser.objects.filter(id_tipo_usuario_id=3),
        empty_label="Selecciona veterinario",
        widget=forms.Select(attrs={'class':'form-select'}),
        label="Veterinario",
        required=True
    )

    class Meta:
        model = Atencion
        fields = '__all__'

class RazaForm(forms.ModelForm):
    nombre_especie = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Especie', 'id': 'myAutocomplete'}))
    nombre_raza = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Raza'}))

    def clean_nombre_especie(self):
        nombre = self.cleaned_data.get('nombre_especie')

        if nombre and not nombre.isalpha() and ' ' not in nombre:
            raise forms.ValidationError("El nombre de la especie debe tener solo letras y espacios")
        
        return nombre

    def clean_nombre_raza(self):
        nombre = self.cleaned_data.get('nombre_raza')

        if nombre and not nombre.isalpha() and ' ' not in nombre:
            raise forms.ValidationError("El nombre de la raza debe tener solo letras y espacios")
        
        return nombre

    class Meta:
        model = Raza
        fields = '__all__'