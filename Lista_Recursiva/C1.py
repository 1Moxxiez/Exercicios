'''
C1. Quadrados dos n´umeros pares
Dada uma lista de n´umeros, retorne uma nova lista com os quadrados apenas dos
n´umeros pares.
'''

def quadrado(*args):
    
    # quadrado = map(
    #     lambda numero: numero ** 2, filter(
    #                                     lambda num: num % 2 == 0, args
    #     )
        
    # )
    
    return [num ** 2 for num in args  if num % 2 == 0  ]
    
    return list(quadrado)

print(quadrado(2, 4, 5))