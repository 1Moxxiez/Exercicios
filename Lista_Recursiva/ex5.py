

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

alvo = 55

num = busca_binaria(lista, alvo)

if num != -1:
      print(f'alvo encontrado no indice {num}')
else:
    print(f'não achou o numero {alvo}')
  
