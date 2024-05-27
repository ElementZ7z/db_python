import sqlite3

# Função para criar o banco de dados e a tabela
def criarbanco():
    connection = sqlite3.connect('trabp.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        materia TEXT NOT NULL,
        nota REAL NOT NULL
    )
    ''')
    connection.commit()
    connection.close()

# Função para inserir um aluno, matéria e nota
def inserir_aluno(nome, materia, nota):
    connection = sqlite3.connect('trabp.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO alunos (nome, materia, nota) VALUES (?, ?, ?)', (nome, materia, nota))
    connection.commit()
    connection.close()

# Função para consultar todos os dados da tabela alunos
def consultar():
    connection = sqlite3.connect('trabp.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM alunos')
    rows = cursor.fetchall()
    connection.close()
    for row in rows:
        print(row)

# Função para deletar um aluno pelo ID
def excluir_aluno(aluno_id):
    connection = sqlite3.connect('trabp.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM alunos WHERE id = ?', (aluno_id,))
    connection.commit()
    connection.close()
    print("Aluno deletado com sucesso!")

