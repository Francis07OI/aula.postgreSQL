import streamlit as st 
from crud import criar_aluno, listar_alunos, atualizar_idade, deletar_aluno

st.set_page_config(page_title="gerenciamento de alunos", page_icon= "👨‍✈️")

st.title("sistema de alunos com o postgreSQL")

menu = st.sidebar.radio("menu",["inserir", "listar", "Atualizar", "Deletar"])

if menu == "inserir":
    st.subheader('➕ inserir alunos')
    nome = st.text_input("nome", placeholder="seu nome")
    idade = st.number_input("idade", min_value=16, step=1)
    if st.button("cadastrar"):
        if nome.strip() != "":
            criar_aluno(nome, idade)
            st.success(f'aluno {nome} inserindo com sucesso!')
        else:
            st.warning("o campo nome não pode ser vazio.")

elif menu == "listar":
    st.subheader("listar alunos")
    alunos = listar_alunos()
    if alunos:
        for linha in alunos:
            st.write(f"ID={linha[0]} | NOME={linha[1]} | IDADE={linha[2]}")
    else:
        st.info("nenhum aluno encontrado.")


elif menu== "Atualizar":
    st.subheader("Atualizar idade")
    alunos = listar_alunos()
    if alunos:
        id_aluno = st.selectbox("escolha o id do aluno  para atualizar", [linha[0] for linha in alunos])
        nova_idade = st.number_input("nova idade", min_value=16, 
        step=1)
        if st.button("atualizar"):
            atualizar_idade(id_aluno, nova_idade)
            st.success(f"idade do aluno atualizada com sucesso.")
    else:
        st.info("nenhum aluno dispoivel para atualizar")


elif menu == "Deletar":
    st.subheader("Deletar aluno")
    alunos = listar_alunos()
    if alunos:
        id_aluno = st.selectbox("Escolha o ID do aluno que deseja remover",  [linha [0] for linha in alunos])
        if st.button("Deletar"):
            deletar_aluno(id_aluno)
            st.success(f"Aluno {id_aluno} removido.")
        else:
            st.info("Digite o id do aluno para remover!")