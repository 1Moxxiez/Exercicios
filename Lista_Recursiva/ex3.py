'''
R3. Soma dos d´ıgitos de um n´umero
Escreva uma fun¸c˜ao recursiva que retorna a soma dos d´ıgitos de um n´umero inteiro
positivo.
Exemplo: soma digitos(1234) → 10

'''

def soma (n: int):
    
    # Base for positivo
    if n <= 0:
        return 0
    
    ultimo_digito = n % 10
    
    resto = n // 10
    
    return ultimo_digito + soma(resto)

#=========================================
# soma_digitos(123)

# ultimo_digito = 123 % 10 → 3
# resto_do_numero = 123 // 10 → 12
# Retorna: 3 + soma_digitos(12)
#==========================================

print(soma(555))