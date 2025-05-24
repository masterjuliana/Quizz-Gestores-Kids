import streamlit as st
import json
import random
from pathlib import Path

# Inicialização de estado
if "pergunta_atual" not in st.session_state:
    st.session_state.pergunta_atual = 0
    st.session_state.pontuacao = 0
    st.session_state.respondido = False
    st.session_state.resposta = None

# Carregar banco de questões
arquivo_json = "banco_de_questoes_hidraulica.json"
if Path(arquivo_json).exists():
    with open(arquivo_json, "r", encoding="utf-8") as f:
        banco = json.load(f)
else:
    st.error(f"Arquivo {arquivo_json} não encontrado.")
    banco = []

# Estilos e título
st.title("🌊 Quiz Hidráulica - GESTORES KIDS")
st.markdown("---")

# Mostrar pergunta atual
if banco:
    pergunta = banco[st.session_state.pergunta_atual]
    st.subheader(pergunta["pergunta"])

    # Mostrar alternativas
    for alt in pergunta["alternativas"]:
        if st.button(alt):
            st.session_state.resposta = alt
            st.session_state.respondido = True
            if alt[0] == pergunta["resposta_correta"]:
                st.session_state.pontuacao += 1
                st.success("✅ Resposta correta!")
            else:
                st.error(f"❌ Resposta errada! Correta: {pergunta['resposta_correta']}")
            st.info(pergunta.get("feedback", ""))

    # Próxima pergunta
    if st.session_state.respondido:
        if st.button("Próxima"):
            st.session_state.pergunta_atual += 1
            st.session_state.respondido = False
            st.session_state.resposta = None

# Fim do quiz
if st.session_state.pergunta_atual >= len(banco):
    st.balloons()
    st.success(f"Fim do quiz! Sua pontuação: {st.session_state.pontuacao} de {len(banco)}")
    if st.button("Recomeçar"):
        st.session_state.pergunta_atual = 0
        st.session_state.pontuacao = 0
        st.session_state.respondido = False
