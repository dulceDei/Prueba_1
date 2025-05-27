import streamlit as st
import random

st.set_page_config(page_title="Ecuación Lineal Aleatoria", page_icon="🧮", layout="centered")

st.title("🧮 Resuelve la ecuación lineal")

# --- Generar la ecuación aleatoria o conservar la anterior ---
if "a" not in st.session_state:
    a = random.choice([i for i in range(-10, 11) if i not in [0, 1, -1]])
    x_sol = random.randint(-10, 10)
    b = random.randint(-20, 20)
    c = a * x_sol + b
    st.session_state["a"] = a
    st.session_state["b"] = b
    st.session_state["c"] = c
    st.session_state["x_sol"] = x_sol

a = st.session_state["a"]
b = st.session_state["b"]
c = st.session_state["c"]
x_sol = st.session_state["x_sol"]

st.latex(f"{a}x {'+' if b >= 0 else '-'} {abs(b)} = {c}")

# --- Campo de respuesta ---
respuesta = st.text_input("¿Cuál es el valor de $x$ que resuelve la ecuación?", key="respuesta")

# --- Botón para verificar ---
if st.button("Verificar respuesta"):
    try:
        respuesta_usuario = float(respuesta.replace(",", "."))
        if abs(respuesta_usuario - x_sol) < 1e-6:
            st.success(f"¡Correcto! La solución es $x = {x_sol}$", icon="✅")
            st.markdown(
                f'<input style="background-color: #00FF0070; color: #222; width: 100%; padding: 0.5em; border-radius: 0.5em;" value="{respuesta_usuario}" readonly>',
                unsafe_allow_html=True
            )
            # Nueva ecuación tras acierto
            if st.button("¿Quieres otra ecuación?"):
                for k in ["a", "b", "c", "x_sol", "respuesta"]:
                    if k in st.session_state:
                        del st.session_state[k]
                st.experimental_rerun()
        else:
            st.error("❌ Respuesta incorrecta.", icon="❌")
            st.markdown(
                f'<input style="background-color: #FF000070; color: #222; width: 100%; padding: 0.5em; border-radius: 0.5em;" value="{respuesta}" readonly>',
                unsafe_allow_html=True
            )
    except Exception:
        st.error("Por favor, ingresa un número válido.", icon="⚠️")

