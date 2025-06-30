'''
A4. Fun¸c˜ao de filtro com *args e **kwargs
Escreva uma fun¸c˜ao que aceita uma lista de n´umeros via *args e usa **kwargs para
aplicar filtros, como min=10, max=50.

'''

def filtrar(*args, **kwargs):

    maxi = kwargs.get('max')
    mini = kwargs.get('min')
    
    return list(filter(lambda numero: 
        numero if mini < numero < maxi else "", args
        )
    )
    
print(filtrar( 11 ,22, 4, 51, 6, 31, 10, min=10, max=50))