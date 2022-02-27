from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not validate_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf': "o CPF deve conter 11 dígitos"})
        if not validate_nome(data['nome']):
            raise serializers.ValidationError({'nome': "O nome deve conter apenas letras"})
        if not validate_rg(data['rg']):
            raise serializers.ValidationError({'rg':"O RG deve conter 9 caracteres"})
        if not validate_celular(data['celular']):
            raise serializers.ValidationError({'celular':"O celular deve deve seguir o padrão (11) 11111-1111"})
        return data
