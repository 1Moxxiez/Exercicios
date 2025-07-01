import itertools

# def gerar_tabela_verdade():
#     """
#     Gera e exibe a tabela-verdade para as proposições p, q, r e as fórmulas lógicas dadas.
#     """
#     p = ['v', 'v', 'f', 'f']
    
#     q = ['v', 'f', 'v', 'f']
    
#     print('p e q')
    
#     pEq = [print('   v') if p[i] and q[i] for i in range(0,4)]


# # Executa a função para gerar a tabela
# gerar_tabela_verdade()



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