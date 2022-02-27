import re
from validate_docbr import CPF

def validate_cpf(cpf):
    cpf = CPF()
    return cpf.validate(cpf)


def validate_nome(nome):
    return nome.isalpha()


def validate_rg(rg):
    return len(rg) == 9


def validate_celular(celular):
     if len(celular) == 11:
         modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
         resposta = re.findall(modelo,celular)
         return resposta


