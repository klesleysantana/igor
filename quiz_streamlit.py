import streamlit as st
import random

st.set_page_config(page_title="Quiz Romântico", page_icon="💖", layout="centered")

# Música de fundo (player manual)
st.markdown("""
<audio controls loop style='width: 100%;'>
  <source src="/static/musica_fundo.mp3" type="audio/mpeg">
  Seu navegador não suporta áudio.
</audio>
""", unsafe_allow_html=True)

# Perguntas do quiz
todas_perguntas = [
    {
        "pergunta": "Qual dessas qualidades você acha que eu mais tenho?",
        "opcoes": ["Carinho", "Paciência", "Amor acumulado por você 💖", "Todas as anteriores 😍"],
        "resposta_correta": "Todas as anteriores 😍",
        "qualquer_resposta": False
    },
    {
        "pergunta": "Se eu aparecesse com chocolate e flores, o que você faria?",
        "opcoes": ["Me daria um beijo 😘", "Diria 'Ai meu Deus!'", "Me chamaria de fofo(a)", "Todas as anteriores!"],
        "resposta_correta": "Todas as anteriores!",
        "qualquer_resposta": True
    },
    {
        "pergunta": "Se eu dissesse que tenho uma pergunta muito importante, você...",
        "opcoes": ["Ficaria curiosa(o)", "Pensaria 'vem bomba aí' 🤭", "Diria 'Pergunta logo!'", "Saberia que é sobre a gente..."],
        "resposta_correta": "Saberia que é sobre a gente...",
        "qualquer_resposta": True
    },
    {
        "pergunta": "Qual é minha cor favorita?",
        "opcoes": ["Azul", "Preto", "Verde", "Amarelo"],
        "resposta_correta": "Preto",
        "qualquer_resposta": False
    },
    {
        "pergunta": "Qual foi o nosso primeiro encontro?",
        "opcoes": ["No cinema", "No shopping", "No parque", "Na praça"],
        "resposta_correta": "No shopping",
        "qualquer_resposta": False
    },
    {
        "pergunta": "Agora a mais difícil: você aceita viver muitas aventuras e amores comigo?",
        "opcoes": ["Sim", "Óbvio", "Lógico", "Nasci pra isso! 💘"],
        "resposta_correta": "Nasci pra isso! 💘",
        "qualquer_resposta": True
    }
]

# Embaralhar perguntas apenas na primeira execução
if 'perguntas' not in st.session_state:
    st.session_state.perguntas = random.sample(todas_perguntas, len(todas_perguntas))
    st.session_state.pagina = 0
    st.session_state.pontuacao = 0
    st.session_state.respostas = []

# Tela inicial
if st.session_state.pagina == 0:
    st.markdown("""
    <h1 style='color:#FF1493; text-align:center;'>Bem-vindo ao Nosso Quiz Especial! 💖</h1>
    <p style='text-align:center;'>Prepare-se para reviver memórias e responder perguntas sobre a gente!</p>
    """, unsafe_allow_html=True)
    if st.button("Iniciar Quiz", use_container_width=True):
        st.session_state.pagina = 1
        st.rerun()

# Perguntas
elif 1 <= st.session_state.pagina <= len(st.session_state.perguntas):
    idx = st.session_state.pagina - 1
    pergunta = st.session_state.perguntas[idx]
    st.markdown(f"<h2 style='color:#FF1493'>{pergunta['pergunta']}</h2>", unsafe_allow_html=True)
    resposta = st.radio("Escolha uma opção:", pergunta["opcoes"], key=f"resposta_{idx}")
    if st.button("Responder", key=f"btn_{idx}", use_container_width=True):
        correta = pergunta["qualquer_resposta"] or resposta == pergunta["resposta_correta"]
        st.session_state.respostas.append((pergunta["pergunta"], resposta, correta))
        if correta:
            st.session_state.pontuacao += 1
        st.session_state.pagina += 1
        st.rerun()

# Tela final
else:
    st.markdown("""
    <h1 style='color:#FF1493; text-align:center;'>Uma Pergunta Muito Importante...</h1>
    """, unsafe_allow_html=True)
    if st.session_state.pontuacao >= 4:
        mensagem = f"""<p style='text-align:center;'>Parabéns! Você acertou <b>{st.session_state.pontuacao}</b> de <b>{len(st.session_state.perguntas)}</b> respostas especiais!<br><br>
        Você é a pessoa mais especial do mundo para mim.<br>
        Cada momento com você é único e precioso.<br><br>
        <span style='font-size:1.3em; color:#FF1493'><b>Quer namorar comigo? ❤️</b></span></p>"""
    else:
        mensagem = f"""<p style='text-align:center;'>Mesmo acertando <b>{st.session_state.pontuacao}</b> de <b>{len(st.session_state.perguntas)}</b>,<br>
        você ainda é a pessoa mais especial do mundo para mim!<br>
        Cada momento com você é único e precioso.<br><br>
        <span style='font-size:1.3em; color:#FF1493'><b>Quer namorar comigo? ❤️</b></span></p>"""
    st.markdown(mensagem, unsafe_allow_html=True)
    st.balloons()
    if st.button("Recomeçar", use_container_width=True):
        for k in ["perguntas", "pagina", "pontuacao", "respostas"]:
            if k in st.session_state:
                del st.session_state[k]
        st.rerun() 