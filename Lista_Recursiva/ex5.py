# from typing import List

# def busca_binaria(lista_ordenada: List[int], alvo: int) -> int:
#     """
#     Função principal que prepara e inicia a busca binária recursiva.

#     Args:
#         lista_ordenada: Uma lista de inteiros ordenada em ordem crescente.
#         alvo: O número que estamos procurando.

#     Returns:
#         O índice do alvo na lista, se encontrado. Caso contrário, retorna -1.
#     """
#     inicio = 0
#     fim = len(lista_ordenada) - 1
#     return busca_recursiva(lista_ordenada, alvo, inicio, fim)


# def busca_recursiva(lista: List[int], alvo: int, inicio: int, fim: int) -> int:
#     """
#     Função auxiliar que implementa a lógica recursiva da busca binária.
#     """
#     # CASO BASE 1: Elemento não encontrado.
#     # Se o ponteiro de início ultrapassar o de fim, significa que o espaço
#     # de busca se esgotou e o alvo não está na lista.   
#     if inicio > fim:
#         return -1

#     # Encontra o índice do meio da fatia atual da lista.
#     meio = (inicio + fim) // 2

#     # CASO BASE 2: Elemento encontrado!
#     # Se o elemento no meio é o nosso alvo, retornamos seu índice.
#     if lista[meio] == alvo:
#         return meio
    
#     # PASSOS RECURSIVOS:
    
#     # Se o alvo for menor que o elemento do meio, ele só pode estar na metade esquerda.
#     # Chamamos a função novamente, mas ajustando o ponteiro 'fim'.
#     elif alvo < lista[meio]:
#         return busca_recursiva(lista, alvo, inicio, meio - 1)
        
#     # Se o alvo for maior que o elemento do meio, ele só pode estar na metade direita.
#     # Chamamos a função novamente, mas ajustando o ponteiro 'inicio'.
#     else: # alvo > lista[meio]
#         return busca_recursiva(lista, alvo, meio + 1, fim)


# # --- Exemplo de uso ---
# numeros = [2, 5, 7, 8, 11, 12, 18, 25, 30, 42]
# alvo1 = 18
# alvo2 = 9 # Um número que não está na lista

# indice1 = busca_binaria(numeros, alvo1)
# indice2 = busca_binaria(numeros, alvo2)

# print(f"Buscando pelo número {alvo1}...")
# if indice1 != -1:
#     print(f"Elemento encontrado no índice: {indice1}")
# else:
#     print("Elemento não encontrado.")

# print("-" * 20)

# print(f"Buscando pelo número {alvo2}...")
# if indice2 != -1:
#     print(f"Elemento encontrado no índice: {indice2}")
# else:
#     print("Elemento não encontrado.")

from typing import List

def busca_binaria(lista: List[int], alvo: int):
    
    inicio = 0
    fim = len(lista) - 1
    return(busca_recursiva(lista, alvo, inicio, fim))

def busca_recursiva(lista: List[int], alvo: int, inicio: int, fim: int ):
    
    if inicio > fim:
        return -1
    
    meio = (inicio + fim) // 2
    
    if lista[meio] == alvo:
        return meio
    
    elif lista[meio] > alvo:
        return(busca_recursiva(lista, alvo, inicio, meio -1))
    
    else: 
        return(busca_recursiva(lista, alvo, meio + 1, fim))
    
    
lista = [2, 5, 7, 8, 11, 12, 18, 25, 30, 42]

alvo = 8

num = busca_binaria(lista, alvo)

if num != -1:
      print(f'alvo encontrado no indice {num}')
else:
    print(f'não achou o numero {alvo}')
  
