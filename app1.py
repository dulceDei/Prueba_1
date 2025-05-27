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
    st.session_state["respuesta"] = ""
    st.session_state["acierto"] = False

# --- Inicializa ecuación si no existe ---
if "a" not in st.session_state:
    nueva_ecuacion()

a = st.session_state["a"]
b = st.session_state["b"]
c = st.session_state["c"]
x_sol = st.session_state["x_sol"]

st.latex(f"{a}x {'+' if b >= 0 else '-'} {abs(b)} = {c}")

# --- Campo de respuesta ---
respuesta = st.text_input(
    "¿Cuál es el valor de $x$ que resuelve la ecuación?",
    value=st.session_state.get("respuesta", ""),
    key="respuesta"
)

# --- Verifica respuesta solo si no se ha acertado ---
if not st.session_state.get("acierto", False):
    if st.button("Verificar respuesta"):
        try:
            respuesta_usuario = float(respuesta.replace(",", "."))
            if abs(respuesta_usuario - x_sol) < 1e-6:
                st.success(f"¡Correcto! La solución es $x = {x_sol}$", icon="✅")
                st.markdown(
                    f'<input style="background-color: #00FF0070; color: #222; width: 100%; padding: 0.5em; border-radius: 0.5em;" value="{respuesta_usuario}" readonly>',
                    unsafe_allow_html=True
                )
                st.session_state["acierto"] = True  # Marca acierto para mostrar botón
            else:
                st.error("❌ Respuesta incorrecta.", icon="❌")
                st.markdown(
                    f'<input style="background-color: #FF000070; color: #222; width: 100%; padding: 0.5em; border-radius: 0.5em;" value="{respuesta}" readonly>',
                    unsafe_allow_html=True
                )
        except Exception:
            st.error("Por favor, ingresa un número válido.", icon="⚠️")

# --- Mostrar botón solo después de acertar ---
if st.session_state.get("acierto", False):
    if st.button("¿Quieres otra ecuación?"):
        nueva_ecuacion()
        st.experimental_rerun()  # Recarga la app para mostrar nueva ecuación


