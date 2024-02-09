import re #próprio do python

def cpf_invalido(cpf):
    return len(cpf) != 11

def nome_invalido(nome):
    return not nome.isalpha()

# 86 99999-9999
def celular_valido(numero): #melhor numero que celular, mudar para VALIDO e colocar o not no serializer
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, numero) #retorna uma lista contendo todas as correspondências encontradas na string
    # se não bater o modelo com o número, resposta = [] e [] = False
    # resposta = ['86 99999-9999'] = True ou re = [] e [] = False
    print(resposta) # mostrar a resposta no print
    return resposta