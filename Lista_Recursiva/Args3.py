'''
A3. Sauda¸c˜ao personalizada com **kwargs
Crie uma fun¸c˜ao saudar(**kwargs) que aceita os argumentos nome, idade e cidade,
e monta uma mensagem personalizada.
Exemplo: "Ol´a, Jo~ao de 30 anos, morador de S~ao Paulo!"

'''

# def saudar(**kwargs): #Dicionario
#     nome = kwargs['nome']
#     idade = kwargs['idade']
#     cidade = kwargs['cidade']
    
#     return (f"Ol´a, {nome} de {idade} anos, morador de {cidade}!")
        
# print(saudar( nome = "Carlos",idade = "30", cidade = "São Paulo"))

def saudar(**kwargs):
    lista = list(kwargs.values()) #a lista ja recebe só os valores
    
    return (f"Ol´a, {lista[0]} de {lista[1]} anos, morador de {lista[2]}!")
    
print(saudar( nome = "Carlos",idade = "30", cidade = "São Paulo"))