import streamlit as st
import random

st.set_page_config(page_title="Ecuación Lineal Aleatoria", page_icon="🧮", layout="centered")
st.title("🧮 Resuelve la ecuación lineal")

def nueva_ecuacion():
    x_sol = random.randint(-10, 10)
    a = random.choice([i for i in range(-10, 11) if i not in [0, 1, -1, 0]])
    b = random.randint(-20, 20)
    c = a * x_sol + b
    st.session_state["a"] = a
    st.session_state["b"] = b
    st.session_state["c"] = c
    st.session_state["x_sol"] = x_sol
    st.session_state["respuesta"] = ""
    st.session_state["resultado"] = ""
    st.session_state["color"] = ""
    st.session_state["mostrar_otro"] = False

# Inicializa la ecuación la primera vez
if "a" not in st.session_state:
    nueva_ecuacion()

a = st.session_state["a"]
b = st.session_state["b"]
c = st.session_state["c"]
x_sol = st.session_state["x_sol"]

st.latex(f"{a}x {'+' if b >= 0 else '-'} {abs(b)} = {c}")

respuesta = st.text_input(
    "¿Cuál es el valor de $x$ que resuelve la ecuación?",
    value=st.session_state.get("respuesta", ""),
    key="respuesta"
)

verificar = st.button("Verificar respuesta")

if verificar:
    st.session_state["respuesta"] = respuesta  # Mantener respuesta en el input
    try:
        respuesta_usuario = float(respuesta.replace(",", "."))
        if respuesta_usuario == x_sol:
            st.session_state["resultado"] = f"¡Correcto! La solución es $x = {x_sol}$"
            st.session_state["color"] = "#00FF0070"  # Verde
        else:
            st.session_state["resultado"] = "❌ Respuesta incorrecta."
            st.session_state["color"] = "#FF000070"  # Rojo
        st.session_state["mostrar_otro"] = True
    except Exception:
        st.session_state["resultado"] = "Por favor, ingresa un número válido."
        st.session_state["color"] = "#FF000070"
        st.session_state["mostrar_otro"] = True

if st.session_state.get("resultado", ""):
    color = st.session_state.get("color", "#FF000070")
    st.markdown(
        f'<div style="background-color: {color}; color: #222; width: 100%; padding: 0.5em; border-radius: 0.5em; margin-bottom: 1em;">{st.session_state["resultado"]}</div>',
        unsafe_allow_html=True
    )

if st.session_state.get("mostrar_otro", False):
    if st.button("¿Quieres otra ecuación?"):
        nueva_ecuacion()
        st.experimental_rerun()

