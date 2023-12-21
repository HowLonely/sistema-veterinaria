from rest_framework import serializers
from veterinaria.models import Raza, FichaClinica, Atencion, Cliente

class RazaSerializar(serializers.ModelSerializer):
    class Meta:
        model = Raza
        fields = '__all__'

class FichaClinicaSerializar(serializers.ModelSerializer):
    class Meta:
        model = FichaClinica
        fields = '__all__'

class AtencionSerializar(serializers.ModelSerializer):
    class Meta:
        model = Atencion
        fields = '__all__'

class ClienteSerializar(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'