

# def gerar_tabela_seu_jeito():
#     p = ['v', 'v', 'v', 'f', 'f']
#     q = ['v', 'v', 'f', 'v']
#     r = ['v', 'f', 'v', 'v']

#     # Usamos a compreensão de lista para CRIAR a lista de resultados 'V' ou 'F'
#     resultados_pEq = ['V' if p[i] == 'v' and q[i] == 'v' else 'F' for i in range(4)]
#     resultados_pEqOUr = ['V' if resultados_pEq[i] == 'v' ]
    
#     # Agora a variável 'resultados_pEq' contém: ['V', 'F', 'F', 'F']
    
#     # --- Agora vamos imprimir tudo de forma organizada ---
#     print('p | q || p e q')
#     print('--|---|-------')
    
#     # Usamos um loop simples para exibir os dados que já calculamos
#     for i in range(4):
#         print(f'{p[i]} | {q[i]} ||   {resultados_pEq[i]}')

# # --- Executando a versão corrigida ---
# gerar_tabela_seu_jeito()

def resolver_tabela_verdade():
    """
    Mostra a tabela-verdade para p, q, r e as fórmulas dadas.
    """
    print("--- Tabela-Verdade ---")
    # Imprime o cabeçalho da nossa tabela
    print(f'|  p  |  q  |  r  || (p e q) ou r | não r ou não q | não p e q |')
    print("-" * 65)

    # Todas as 8 combinações possíveis de Verdadeiro (True) e Falso (False)
    combinacoes = [
        [True, True, True], [True, True, False], [True, False, True], [True, False, False],
        [False, True, True], [False, True, False], [False, False, True], [False, False, False]
    ]

    # Para cada combinação, calcula e imprime os resultados
    for p, q, r in combinacoes:
        # Fórmulas lógicas dadas na questão
        formula1 = (p and q) or r
        formula2 = (not r) or (not q)
        formula3 = (not p) and q
        
        # Converte True/False para V/F para uma exibição mais clara
        p_v = "V" if p else "F"
        q_v = "V" if q else "F"
        r_v = "V" if r else "F"
        f1_v = "V" if formula1 else "F"
        f2_v = "V" if formula2 else "F"
        f3_v = "V" if formula3 else "F"

        print(f'|  {p_v}  |  {q_v}  |  {r_v}  ||      {f1_v}         |       {f2_v}        |     {f3_v}     |')

# Executa a função
resolver_tabela_verdade()




import pprint

def cadastrar_alunos():
    """
    Permite o cadastro de até 5 alunos em um dicionário e o exibe no final.
    """
    alunos_cadastrados = {}
    print("--- Cadastro de Alunos (máximo 5) ---")
    print("Para parar antes, deixe o nome do aluno em branco e pressione Enter.")

    for i in range(2):
        print(f"\n--- Aluno {i+1} ---")
        nome = input("Nome do aluno: ")
        
        # Condição de parada
        if not nome:
            break
            
        while True:
            try:
                matricula = int(input("Matrícula: "))
                nota_final = float(input("Nota final (0 a 10): "))
                if 0 <= nota_final <= 10:
                    break
                else:
                    print("A nota final deve ser entre 0 e 10.")
            except ValueError:
                print("Por favor, insira valores numéricos para matrícula e nota.")

        # Cria o dicionário interno e o adiciona ao dicionário principal
        alunos_cadastrados[nome] = {
            'Matrícula': matricula,
            'Nota final': nota_final
        }
        
    print("\n--- Cadastro Finalizado ---")
    print("Dicionário de Alunos Cadastrados:")
    # Usa pprint para uma exibição mais organizada do dicionário
    pprint.pprint(alunos_cadastrados)

    return alunos_cadastrados

# --- Execução do programa ---
cadastrar_alunos()



def cadastrar_3_produtos():
    """
    Pede ao usuário para inserir os dados de 3 produtos e os retorna em uma lista.
    """
    estoque = []
    print("--- Cadastro de 3 Produtos ---")

    for i in range(3):
        nome = input(f"Digite o nome do produto {i+1}: ")
        quantidade = int(input(f"Digite a quantidade de {nome}: "))
        
        # Cria o dicionário do produto e adiciona à lista de estoque
        produto = {"nome": nome, "quantidade": quantidade}
        estoque.append(produto)
        print("Produto cadastrado!")
        
    return estoque

def consultar_estoque(lista_de_produtos):
    """
    Pergunta ao usuário o nome de um produto e mostra a quantidade em estoque.
    """
    print("\n--- Consulta de Estoque ---")
    produto_procurado = input("Qual produto você quer consultar? ")
    
    encontrou = False
    for produto in lista_de_produtos:
        if produto["nome"] == produto_procurado:
            print(f"Resultado: Há {produto['quantidade']} unidades de '{produto['nome']}' no estoque.")
            encontrou = True
            break # Para o loop assim que encontrar o produto
            
    if not encontrou:
        print(f"O produto '{produto_procurado}' não foi encontrado.")

# --- Execução do Programa ---
# Primeiro, cadastra os produtos
estoque_da_loja = cadastrar_3_produtos()

# Depois, permite a consulta
consultar_estoque(estoque_da_loja)


def analisar_vendas_simples():
    """
    Analisa uma lista de vendas pré-definida.
    """
    # Lista de vendas já preenchida para facilitar o teste
    vendas = [
        {"produto": "Notebook", "quantidade": 2, "preco_unitario": 3500.0},
        {"produto": "Mouse", "quantidade": 10, "preco_unitario": 120.0},
        {"produto": "Teclado", "quantidade": 5, "preco_unitario": 250.0},
        {"produto": "Notebook", "quantidade": 1, "preco_unitario": 4200.0},
        {"produto": "Mouse", "quantidade": 8, "preco_unitario": 125.0},
    ]

    print("--- Dados de Vendas ---")
    print(vendas)

    # --- 1. Calcular o total arrecadado por produto ---
    faturamento_por_produto = {}
    for venda in vendas:
        produto = venda["produto"]
        receita_da_venda = venda["quantidade"] * venda["preco_unitario"]

        if produto not in faturamento_por_produto:
            faturamento_por_produto[produto] = 0 # Cria a chave se for a primeira vez
        
        faturamento_por_produto[produto] += receita_da_venda

    print("\n--- Total Arrecadado por Produto ---")
    for produto, total in faturamento_por_produto.items():
        print(f" - {produto}: R$ {total:.2f}")

    # --- 2. Identificar o produto mais vendido (por quantidade) ---
    quantidade_por_produto = {}
    for venda in vendas:
        produto = venda["produto"]
        quantidade = venda["quantidade"]
        
        if produto not in quantidade_por_produto:
            quantidade_por_produto[produto] = 0 # Cria a chave
            
        quantidade_por_produto[produto] += quantidade

    produto_mais_vendido = ""
    maior_quantidade = 0
    for produto, quantidade_total in quantidade_por_produto.items():
        if quantidade_total > maior_quantidade:
            maior_quantidade = quantidade_total
            produto_mais_vendido = produto

    print("\n--- Produto Mais Vendido ---")
    print(f"O produto mais vendido foi '{produto_mais_vendido}' com {maior_quantidade} unidades.")

# Executa a análise
analisar_vendas_simples()