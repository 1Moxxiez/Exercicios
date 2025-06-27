'''
R1. Contagem regressiva com atraso
Implemente uma fun¸c˜ao recursiva contagem regressiva(n) que imprime uma contagem de n at´e 0. Ao chegar a 0, deve imprimir "Boom!".
(Opcional: usar time.sleep(1) para simular contagem real.)
♦
'''

import time

def contagem_regressiva(n):
    
# 1. Caso Base: A condição de parada.
    # Quando a contagem passa de 0 para -1, a recursão para.
    if n < 0:
        print("Boom!")
        return  # Encerra a execução desta chamada e retorna para a anterior.

    # 2. Ação do Passo Atual
    # Imprime o número atual da contagem.
    print(n)
    
    # Opcional: Pausa por 1 segundo para simular uma contagem real.
    time.sleep(1)

    # 3. Passo Recursivo
    # A função chama a si mesma, mas com o próximo número (n - 1).
    contagem_regressiva(n - 1)
    
    
contagem_regressiva(5)