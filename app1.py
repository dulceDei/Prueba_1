import streamlit as st

st.set_page_config(page_title="Quiz Python - Repaso Básico", page_icon="🐍", layout="centered")
st.title("🐍 Quiz de Repaso: Sintaxis de Python")

preguntas = [
    {
        "pregunta": "¿Cuál es la sintaxis correcta para definir una función en Python?",
        "opciones": [
            "function mi_funcion():",
            "def mi_funcion():",
            "define mi_funcion()",
            "func mi_funcion():"
        ],
        "respuesta": 1,
    },
    {
        "pregunta": "¿Cómo accedemos al tercer elemento de la lista llamada 'frutas'?",
        "opciones": [
            "frutas[2]",
            "frutas(3)",
            "frutas[3]",
            "frutas[1]"
        ],
        "respuesta": 0,
    },
    {
        "pregunta": "¿Qué imprime el siguiente código?\n\nfor i in range(2):\n    print(i)",
        "opciones": [
            "1\n2",
            "0\n1",
            "0\n1\n2",
            "1\n2\n3"
        ],
        "respuesta": 1,
    },
    {
        "pregunta": "¿Cuál es la sintaxis correcta para un condicional 'if'?",
        "opciones": [
            "if x == 10",
            "if x = 10:",
            "if x == 10:",
            "if (x == 10)"
        ],
        "respuesta": 2,
    },
    {
        "pregunta": "¿Qué devuelve la función len(['a','b','c'])?",
        "opciones": [
            "2",
            "3",
            "4",
            "'abc'"
        ],
        "respuesta": 1,
    },
]

# --- RESETEO (importante hacerlo antes de los widgets) ---
if "reset_quiz" not in st.session_state:
    st.session_state["reset_quiz"] = False

if st.session_state["reset_quiz"]:
    # Borrar respuestas previas de cada pregunta


