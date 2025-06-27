'''
R2. Inverter string recursivamente
Escreva uma fun¸c˜ao recursiva que recebe uma string e retorna a string invertida.
Exemplo: "python" → "nohtyp"
'''

def invertida(s: str):
    
    # 1. Caso Base: a condição de parada.
    # Se a string estiver vazia, não há nada para inverter.
    # Retornamos uma string vazia, encerrando a recursão.
    if len(s) == 0:
        return ""
    
    primeira_letra = s[0] #pega a primeira letra
    
    resto = s[1:] #guarda o resto da frase
    
    return invertida(resto) + primeira_letra # ele vai somar sempre a primeira letra da frase enquanto gurada o rest na variavel
                                             #até o resto ficar vazio e ele retornar ''

print(invertida('porta'))
    