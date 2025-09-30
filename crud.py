from db import conectar

def criar_aluno(nome, idade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO alunos (nome, idade VALUES (%s %s)",
                (nome,idade)
                )
            conexao.commit()
        except Exception as erro:
            print(f"erro ao criar aluno:{erro}")
        finally:
            cursor.close()
            cursor.close()
            