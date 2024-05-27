# Função para exibir o menu e gerenciar as escolhas do usuário
def exibir_menu():
    while True:
        print("\nMenu:")
        print("1. Inserir Aluno, Matéria e Nota")
        print("2. Consultar Dados")
        print("3. Deletar Aluno")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Digite o nome do aluno: ")
            materia = input("Digite a matéria: ")
            nota = float(input("Digite a nota: "))
            inserir_aluno(nome, materia, nota)
            print("Dados inseridos com sucesso!")
        elif escolha == '2':
            print("Dados dos alunos:")
            consultar()
        elif escolha == '3':
            aluno_id = int(input("Digite o ID do aluno a ser deletado: "))
            excluir_aluno(aluno_id)
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__== "__interface__":
exibir_menu()
