'''
Potˆencia Recursiva
Implemente uma fun¸c˜ao recursiva que calcula base^expoente, onde ambos s˜ao inteiros positivos.

'''

def calculo (base: int, expoente: int):
    
    if base <= 0 or expoente <= 0:
        # Lança um erro para informar que a entrada é inválida.
        return ('n serve')

    # A lógica recursiva, que só será executada se a entrada for válida.
    if expoente == 1:
        return base

    return(base * (calculo(base, expoente - 1)))
    
print(calculo(5, -4))