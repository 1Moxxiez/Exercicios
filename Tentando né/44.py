'''Divida uma lista em N sublistas de tamanho igual'''

def dividir(l1, tamanho):
    
    return[l1[i : i + tamanho   ] for i in range(0, len(l1), tamanho)]

print(dividir([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2))
    
