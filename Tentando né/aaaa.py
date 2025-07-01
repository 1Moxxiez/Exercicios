

def gerar_tabela_seu_jeito():
    p = ['v', 'v', 'v', 'f', 'f']
    q = ['v', 'v', 'f', 'v']
    r = ['v', 'f', 'v', 'v']

    # Usamos a compreensão de lista para CRIAR a lista de resultados 'V' ou 'F'
    resultados_pEq = ['V' if p[i] == 'v' and q[i] == 'v' else 'F' for i in range(4)]
    resultados_pEqOUr = ['V' if resultados_pEq[i] == 'v' ]
    
    # Agora a variável 'resultados_pEq' contém: ['V', 'F', 'F', 'F']
    
    # --- Agora vamos imprimir tudo de forma organizada ---
    print('p | q || p e q')
    print('--|---|-------')
    
    # Usamos um loop simples para exibir os dados que já calculamos
    for i in range(4):
        print(f'{p[i]} | {q[i]} ||   {resultados_pEq[i]}')

# --- Executando a versão corrigida ---
gerar_tabela_seu_jeito()

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

    for i in range(5):
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