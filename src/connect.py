import psycopg2
import os
from tabulate import tabulate

# Função para imprimir os dados da tabela alunos
def imprimir_alunos():
    os.system('cls')
    try:
        # Executar a consulta SELECT
        cursor.execute("SELECT * FROM alunos")
        
        # Obter todos os resultados da consulta
        rows = cursor.fetchall()

        # Organizar os dados em uma lista de listas
        data = [[row[0], row[1], row[2]] for row in rows]

        # Definir os cabeçalhos das colunas
        headers = ["ID", "Nome", "Sobrenome"]

        # Imprimir os dados como uma tabela
        print(tabulate(data, headers, tablefmt="fancy_grid"))
        
    except (Exception, psycopg2.Error) as error:
        print('Erro ao consultar os alunos:', error)
    
    print("\n---------------------------")
    print("Voltar (Qualquer Tecla)")
    print("--------------------------- \n")
    
    input()

# Dados de conexão com o banco de dados
host = 'localhost'
database = 'ATIVIDADE 05-06-2023'
user = 'postgres'
password = 'umc@2022'

# Conectando ao banco de dados
try:
    connection = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )
    cursor = connection.cursor()
    print('Conexão bem-sucedida ao banco de dados!')

    while True:
        os.system('cls')
        print("\n Opções:")
        print("1 - Consultar alunos")
        print("2 - Inserir aluno")
        print("3 - Deletar aluno")
        print("0 - Sair")

        opcao = int(input("Digite o número da opção desejada: "))

        if opcao == 1:
            imprimir_alunos()
        
        elif opcao == 2:
            os.system('cls')
            nome = input("Digite o nome do aluno: ")
            sobrenome = input("Digite o sobrenome do aluno: ")

            try:
                # Executar a inserção na tabela alunos
                cursor.execute("INSERT INTO alunos (nome, sobrenome) VALUES (%s, %s)", (nome, sobrenome))
                connection.commit()
                print("Aluno inserido com sucesso!")
            except (Exception, psycopg2.Error) as error:
                print('Erro ao inserir o aluno:', error)

        elif opcao == 3:

            id_aluno = int(input("Digite o ID do aluno que deseja deletar: "))

            try:
                # Executar a exclusão na tabela alunos
                cursor.execute("DELETE FROM alunos WHERE id = %s", (id_aluno,))
                connection.commit()
                os.system('cls')
                print("\n--------------------------- \n")
                print("Aluno deletado com sucesso!")
                print("--------------------------- \n")
                
            except (Exception, psycopg2.Error) as error:
                os.system('cls')
                print("\n --------------------------- \n")
                print('Erro ao deletar o aluno:', error)
                print("\n --------------------------- \n") 
        elif opcao == 0:
            break

        else:
            print("Opção inválida. Tente novamente.")

except (Exception, psycopg2.Error) as error:
    print('Erro ao conectar ao banco de dados:', error)
finally:
    # Fechar a conexão com o banco de dados
    if connection:
        cursor.close()
        connection.close()
        print('Conexão fechada.')
