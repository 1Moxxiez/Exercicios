'''Implemente uma fun¸c˜ao que conte quantas vezes um valor aparece em uma lista.'''

def conta (valor,l1):
    contador = [item for item in l1 if item == valor]
    
    
    return[len(contador)]

print(conta(5, [1, 2, 3, 5, 6, 3, 5, 1, 4, 5]))