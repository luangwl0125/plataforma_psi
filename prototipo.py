import streamlit as st
from datetime import datetime

# Título da Plataforma
st.title("Plataforma de Psicologia")

# Menu de Navegação
page = st.sidebar.selectbox("Escolha uma opção:", ["Atendimento On-line", "Agenda", "Gerenciador de Pacientes", "Biblioteca Psi", "Notícias"])

# Página de Atendimento On-line
if page == "Atendimento On-line":
    st.header("Atendimento On-line")
    st.write("Conecte-se com seu paciente através de videochamada.")
    if st.button("Iniciar Atendimento"):
        st.success("Conectando ao atendimento...")

# Página de Agenda
elif page == "Agenda":
    st.header("Agenda")
    st.subheader("Agendar Nova Consulta")
    data = st.date_input("Escolha uma data", datetime.today())
    hora = st.time_input("Escolha um horário")
    paciente = st.text_input("Nome do Paciente")

    if st.button("Agendar Consulta"):
        st.success(f"Consulta agendada para {paciente} em {data} às {hora}.")

# Página de Gerenciador de Pacientes
elif page == "Gerenciador de Pacientes":
    st.header("Gerenciador de Pacientes")
    st.subheader("Adicionar Novo Paciente")
    nome_paciente = st.text_input("Nome do Paciente")
    idade = st.number_input("Idade", min_value=0, max_value=120)
    descricao = st.text_area("Descrição do Paciente")

    if st.button("Adicionar Paciente"):
        st.success(f"Paciente {nome_paciente} adicionado com sucesso!")

# Página de Biblioteca Psi
elif page == "Biblioteca Psi":
    st.header("Biblioteca Psi")
    busca = st.text_input("Pesquise por recursos ou temas:")
    if st.button("Pesquisar"):
        st.write(f"Aqui estão os resultados para '{busca}':")
        st.write("1. Livro: Psicologia e Tecnologia")
        st.write("2. Artigo: A Importância da Escuta na Psicologia")

# Página de Notícias
elif page == "Notícias":
    st.header("Notícias Diárias")
    st.write("Aqui aparecerão as últimas notícias sobre psicologia.")
    st.write("1. Novo estudo revela a eficácia da terapia cognitivo-comportamental.")
    st.write("2. O impacto da inteligência artificial na prática psicológica.")

# Rodapé
st.write("Desenvolvido por Madie Laine - OpenAI Researcher")
