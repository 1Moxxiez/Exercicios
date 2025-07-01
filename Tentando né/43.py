'''Implemente um sistema que simule um carrinho de compras: adi¸c˜ao, remo¸c˜ao e
total de itens com pre¸cos.
'''

carrinho={'item':[], 'preço':[]}

def adicao(item, preco):
    global carrinho
    
    carrinho['item'].append(item)
    carrinho['preço'].append(preco)
    return f"O item {item} com o preço {preco} foi adicionado"

def remoção(item, preco):
    global carrinho
    
    if item in carrinho['item'] and preco in carrinho['preço']:
        carrinho['item'].remove(item)
        carrinho['preço'].remove(preco)
        return f"O item {item} com o preço {preco} foi removido"

    else:
        return f'o item não foi encontrado'

def total():
    global carrinho
    
    total_item = [len(carrinho['item'])]
    total_preço = [sum(carrinho['preço'])]
    
    return f"O total de items: {total_item}. total do preço: {total_preço}"


print(adicao('maça', 2))
print(adicao('pera', 3))
print(adicao('abobora', 3))
print(remoção('maça', 2))
print(total())

    