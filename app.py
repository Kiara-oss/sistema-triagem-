import streamlit as st
import csv

st.title("📋 Sistema de Triagem de Candidatos")

# Função para cadastrar candidatos
def cadastrar_candidato():
    nome = st.text_input("Nome:")
    idade = st.number_input("Idade:", min_value=0)
    vaga = st.selectbox(
        "Vaga desejada:",
        [
            "Chefe de Confeiteiro",
            "Confeiteiro",
            "Auxiliar de Confeitaria",
            "Atendente",
            "Gerente",
            "Barista",
            "Auxiliar de Barista",
        ],
    )
    experiencia = st.radio("Tem experiência?", ["Sim", "Não"])

    if st.button("Cadastrar candidato"):
        with open("candidatos.csv", "a", newline="") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow([nome, idade, vaga, experiencia])
        st.success(f"Candidato {nome} cadastrado com sucesso!")

# Função que analisa o candidato
def analisar_candidato(nome, idade, vaga, experiencia):
    vagas_com_experiencia = ["Chefe de Confeiteiro", "Confeiteiro", "Gerente", "Barista"]
    if idade < 18:
        return f"{nome}: ❌ Não aceito (idade mínima não atingida)"
    if vaga in vagas_com_experiencia and experiencia.lower() != "sim":
        return f"{nome}: ❌ Não aceito (precisa ter experiência para a vaga de {vaga})"
    return f"{nome}: ✅ Aprovado para a próxima etapa!"

# Função para filtrar e analisar candidatos
def filtrar_candidatos():
    try:
        with open("candidatos.csv", "r") as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                nome, idade, vaga, experiencia = linha
                idade = int(idade)
                st.write(analisar_candidato(nome, idade, vaga, experiencia))
    except FileNotFoundError:
        st.warning("Ainda não há candidatos cadastrados!")

# Interface do app
aba = st.sidebar.selectbox("Escolha uma opção:", ["Cadastrar", "Analisar"])

if aba == "Cadastrar":
    cadastrar_candidato()
else:
    filtrar_candidatos()
