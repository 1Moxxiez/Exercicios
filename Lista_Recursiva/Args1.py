'''
A1. Soma com *args
Escreva uma fun¸c˜ao que aceita qualquer quantidade de argumentos num´ericos e
retorna a soma deles.

'''

def soma(*qualquer): #recebe tupla
    
    # total = 0
    
    # for numero in qualquer:
    #     total += numero
    # return total
    
    return sum(qualquer)



print(soma(1, 5, 7))