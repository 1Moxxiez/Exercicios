'''
A5. Fun¸c˜ao de formata¸c˜ao flex´ıvel
Crie uma fun¸c˜ao que usa **kwargs para formatar strings com placeholders personalizados.
Exemplo: formata("Ol´a {nome}, seja bem-vindo(a) a {cidade}.", nome="Ana",
cidade="Recife")

'''

def formata(frase_modelo, **kwargs):
  """
  Formata uma string substituindo os placeholders {} com os valores
  passados via **kwargs.
  """
  # A frase modelo usa o método .format() e nós desempacotamos
  # o dicionário kwargs para preenchê-la.
  return frase_modelo.format(**kwargs)

# --- TESTANDO A FLEXIBILIDADE ---

# Teste 1: O exemplo do exercício
mensagem1 = formata("Olá {nome}, seja bem-vindo(a) a {cidade}.", nome="Ana", cidade="Recife")
print(mensagem1)

# Teste 2: Um template completamente diferente
relatorio = "O produto {produto} (ID: {id}) tem {estoque} unidades em estoque."
mensagem2 = formata(relatorio, produto="Notebook", id=123, estoque=42)
print(mensagem2)

# Teste 3: Usando os mesmos placeholders com outros valores
mensagem3 = formata("Olá {nome}, seja bem-vindo(a) a {cidade}.", nome="Carlos", cidade="Três Lagoas")
print(mensagem3)