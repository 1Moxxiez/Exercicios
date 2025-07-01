'''Pares de n´umeros (produto cartesiano)
Dadas duas listas de n´umeros, gere todos os pares poss´ıveis entre elementos de uma
e de outra.
Exemplo: [1,2] e [3,4] → [(1,3), (1,4), (2,3), (2,4)]
'''


def junta(l1,l2):
    
    pares= [(item1,item2)  for item1 in l1  for item2 in l2]
 
    return pares




print(junta ([1, 2], [3, 4]))