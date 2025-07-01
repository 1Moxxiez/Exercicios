'''Crie uma fun¸c˜ao que compare duas listas e retorne os elementos que est˜ao em ambas
(interse¸c˜ao).'''

def compara(l1,l2):


    return [item for item in l2 if item in l1 ]

print(compara([1, 2, 3, 4], [1, 2, 4, 5, 6]))