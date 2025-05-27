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

if "verificado" not in st.session_state:
    st.session_state["verificado"] = False
if "puntaje" not in st.session_state:
    st.session_state["puntaje"] = 0

# --- Botón para reiniciar (deseleccionar) ---
if st.session_state.get("verificado", False):
    if st.button("Intentar de nuevo"):
        for idx in range(len(preguntas)):
            key = f"preg_{idx}"
            if key in st.session_state:
                del st.session_state[key]
        st.session_state["verificado"] = False
        st.session_state["puntaje"] = 0

# --- Renderizar preguntas ---
for idx, pregunta in enumerate(preguntas):
    st.radio(
        f"{idx+1}. {pregunta['pregunta']}",
        pregunta["opciones"],
        key=f"preg_{idx}",
        index=None,
        disabled=st.session_state.get("verificado", False)
    )

# --- Botón para verificar respuestas ---
if not st.session_state.get("verificado", False):
    if st.button("Verificar mis respuestas"):
        aciertos = 0
        for idx, pregunta in enumerate(preguntas):
            seleccion = st.session_state.get(f"preg_{idx}")
            correcta = pregunta["opciones"][pregunta["respuesta"]]
            if seleccion == correcta:
                aciertos += 1
        st.session_state["puntaje"] = aciertos
        st.session_state["verificado"] = True

# --- Mostrar resultados después de verificar ---
if st.session_state.get("verificado", False):
    puntaje = st.session_state.get("puntaje", 0)
    st.markdown(f"### Tu puntaje: **{puntaje}/5**")
    for idx, pregunta in enumerate(preguntas):
        seleccion = st.session_state.get(f"preg_{idx}")
        correcta = pregunta["opciones"][pregunta["respuesta"]]
        if seleccion == correcta:
            st.success(f"Pregunta {idx+1}: ¡Correcto!")
        else:
            st.error(f"Pregunta {idx+1}: Incorrecto. Respuesta correcta: '{correcta}'")
    if puntaje == 5:
        st.balloons()

