import streamlit as st
import random

st.set_page_config(page_title="Ecuación Lineal Aleatoria", page_icon="🧮", layout="centered")

st.title("🧮 Resuelve la ecuación lineal")

# --- Función para generar nueva ecuación ---
def nueva_ecuacion():
    a = random.choice([i for i in range(-10, 11) if i not in [0, 1, -1]])
    x_sol = random.randint(-10, 10)
    b = random.randint(-20, 20)
    c = a * x_sol + b
    st.session_state["a"] = a
    st.session_state["b"] = b
    st.session_state["c"] = c
    st.session_state["x_sol"] = x_sol
    st.session_state["resultado"] = ""
    st.session_state["color"] = ""
    st.session_state["respuesta"] = ""

# --- Inicializa ecuación si no existe ---
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

# Botón para verificar la respuesta
verificar = st.button("Verificar respuesta")

# Verificación de la respuesta
if verificar:
    try:
        respuesta_usuario = float(respuesta.replace(",", "."))
        if abs(respuesta_usuario - x_sol) < 1e-6:
            st.session_state["resultado"] = f"¡Correcto! La solución es $x = {x_sol}$"
            st.session_state["color"] = "#00FF0070"  # Verde
        else:
            st.session_state["resultado"] = "❌ Respuesta incorrecta."
            st.session_state["color"] = "#FF000070"  # Rojo
        st.session_state["mostrar_otro"] = True
    except Exception:
        st.session_state["resultado"] = "Por favor, ingresa un número válido."
        st.session_state["color"] = "#FF000070"  # Rojo
        st.session_state["mostrar_otro"] = True

# Mostrar resultado solo si hay uno
if st.session_state.get("resultado", ""):
    color = st.session_state.get("color", "#FF000070")
    st.markdown(
        f'<div style="background-color: {color}; color: #222; width: 100%; padding: 0.5em; border-radius: 0.5em; margin-bottom: 1em;">{st.session_state["resultado"]}</div>',
        unsafe_allow_html=True
    )

# Mostrar botón para otra ecuación si ya se verificó una vez
if st.session_state.get("mostrar_otro", False):
    if st.button("¿Quieres otra ecuación?"):
        nueva_ecuacion()
        st.session_state["mostrar_otro"] = False
        st.experimental_rerun()


