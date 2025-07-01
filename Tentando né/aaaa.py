

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



import pprint

def analisar_vendas():
    """
    Simula o registro de vendas e implementa as funcionalidades de análise.
    """
    # Para facilitar a execução, as vendas foram pré-definidas.
    # O formato segue o exemplo, e.g., {"produto": "Notebook", "quantidade": 3, "preco_unitario": 3500.0} [cite: 48]
    vendas = [
        {"produto": "Notebook", "quantidade": 2, "preco_unitario": 3500.0},
        {"produto": "Mouse", "quantidade": 10, "preco_unitario": 120.0},
        {"produto": "Teclado", "quantidade": 5, "preco_unitario": 250.0},
        {"produto": "Notebook", "quantidade": 1, "preco_unitario": 4200.0},
        {"produto": "Mouse", "quantidade": 8, "preco_unitario": 125.0},
        {"produto": "Monitor", "quantidade": 3, "preco_unitario": 1500.0},
        {"produto": "Teclado", "quantidade": 3, "preco_unitario": 260.0},
        {"produto": "Notebook", "quantidade": 3, "preco_unitario": 3800.0},
        {"produto": "Mouse", "quantidade": 5, "preco_unitario": 130.0},
        {"produto": "Monitor", "quantidade": 2, "preco_unitario": 1600.0}
    ]

    print("--- Vendas Registradas ---")
    pprint.pprint(vendas)

    # Dicionários para agregar os dados da análise
    total_arrecadado_por_produto = {}
    total_vendido_por_produto = {}
    
    # Processa cada venda da lista
    for venda in vendas:
        produto = venda["produto"]
        quantidade = venda["quantidade"]
        preco = venda["preco_unitario"]
        
        # Calcula o total da venda atual
        total_venda_atual = quantidade * preco
        
        # Agrega os totais por produto
        total_arrecadado_por_produto[produto] = total_arrecadado_por_produto.get(produto, 0) + total_venda_atual
        total_vendido_por_produto[produto] = total_vendido_por_produto.get(produto, 0) + quantidade
        
    print("\n--- Análise de Vendas ---")

    # (b.1) Exibe o total arrecadado por produto [cite: 51]
    print("\nTotal Arrecadado por Produto:")
    for produto, total in total_arrecadado_por_produto.items():
        print(f"  - {produto}: R$ {total:,.2f}")
        
    # (b.2) Identifica e exibe o produto mais vendido [cite: 52]
    if total_vendido_por_produto: # Garante que há vendas para analisar
        produto_mais_vendido = max(total_vendido_por_produto, key=total_vendido_por_produto.get)
        quantidade_maxima = total_vendido_por_produto[produto_mais_vendido]
        
        print("\nProduto Mais Vendido (por quantidade):")
        print(f"  - {produto_mais_vendido}, com um total de {quantidade_maxima} unidades vendidas.")
    else:
        print("\nNenhuma venda registrada para analisar.")

# --- Execução do programa ---
analisar_vendas()