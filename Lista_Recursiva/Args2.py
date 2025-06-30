'''
A2. Multiplica¸c˜ao com *args e verifica¸c˜ao de tipo
Crie uma fun¸c˜ao que multiplica todos os argumentos num´ericos, ignorando qualquer
argumento que n˜ao seja int ou float.

'''
import math
def multiplica(*args):
    total = 1
    
    num_validos = [numero for numero in args if isinstance(numero, (int,float))]

    for n in num_validos:
        total *= n
    
    # math.prod multiplica todos os itens de uma lista
    return math.prod(num_validos)
    # return total


print(multiplica(2, 'oi' ,4))












# def multiplica(*qualquer):
    
#     total = 1
    
#     for numero in qualquer:
#         # isinstance(objeto, tipo_ou_tupla_de_tipos) retorna True se o objeto for do tipo especificado.
#         if isinstance(numero, (int,float)):
#             total *= numero
#         else:
#             pass
#     return total

# print(multiplica(2,'oi' ,4))
