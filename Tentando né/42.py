'''Dada uma lista de inteiros, crie uma fun¸c˜ao que identifique os n´umeros que aparecem
mais de uma vez e quantas vezes cada um aparece.'''

def aparece(l1):

    numeros = [item for item in l1 if l1.count(item) > 1]
    
    formata = map
    
    return numeros
    
print(aparece([1, 1, 1, 2, 3, 4]))