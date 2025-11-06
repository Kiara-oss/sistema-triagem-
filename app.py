import streamlit as st
import csv
import os

st.set_page_config(page_title="Sistema de Triagem de Candidatos", page_icon="🧁")

st.title("🧁 Sistema de Triagem de Candidatos")

# Função para cadastrar candidato
def cadastrar_candidato(nome, idade, vaga, experiencia):
    with open("candidatos.csv", "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([nome, idade, vaga, experiencia])
    st.success(f"Candidato {nome} cadastrado com sucesso!")

# Função que analisa candidato
def analisar_candidato(nome, idade, vaga, experiencia):
    vagas_com_experiencia = ["chefe de confeitaria", "confeiteiro", "gerente", "barista"]

    if idade < 18:
        return f"{nome}: ❌ Não aceito (idade mínima não atingida)"
    if vaga.lower() in vagas_com_experiencia and experiencia.lower() not in ["sim", "s"]:
        return f"{nome}: ❌ Não aceito (precisa ter experiência para a vaga de {vaga})"
    return f"{nome}: ✅ Aprovado para a próxima etapa!"

# Função para filtrar e analisar candidatos
def filtrar_candidatos():
    if not os.path.exists("candidatos.csv"):
        st.warning("Ainda não há candidatos cadastrados!")
        return

    with open("candidatos.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            nome, idade, vaga, experiencia = linha
            resultado = analisar_candidato(nome, int(idade), vaga, experiencia)
            st.write(resultado)

# Interface principal
aba = st.sidebar.selectbox("Menu", ["Cadastrar candidato", "Analisar candidatos"])

if aba == "Cadastrar candidato":
    st.subheader("📋 Cadastrar novo candidato")

    nome = st.text_input("Nome")
    idade = st.number_input("Idade", min_value=0, step=1)
    vaga = st.selectbox(
        "Vaga desejada",
        [
            "Chefe de Confeitaria",
            "Confeiteiro",
            "Auxiliar de Confeitaria",
            "Atendente",
            "Gerente",
            "Barista",
            "Auxiliar de Barista",
        ],
    )
    experiencia = st.radio("Tem experiência?", ["Sim", "Não"])

    if st.button("Salvar cadastro"):
        if nome and idade:
            cadastrar_candidato(nome, idade, vaga, experiencia)
        else:
            st.error("Por favor, preencha todos os campos!")

elif aba == "Analisar candidatos":
    st.subheader("🔍 Análise de candidatos")
    filtrar_candidatos()
