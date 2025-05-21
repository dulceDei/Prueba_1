import streamlit as st
import random

# Configuración de la página
st.set_page_config(page_title="Ecuaciones de Primer Grado", page_icon="🧮", layout="centered")

st.title("🧮 Ecuaciones de Primer Grado")
st.markdown("Resuelve la ecuación y verifica tu respuesta. Cada vez que recargues, aparecerá una nueva.")

# Generar coeficientes aleatorios
a = random.randint(1, 10)
b = random.randint(-10, 10)
x_real = random.randint(-10, 10)
c = a * x_real + b

# Mostrar ecuación
st.markdown(f"### ¿Cuál es el valor de x en la siguiente ecuación?")
st.latex(f"{a}x + ({b}) = {c}")

# Entrada del usuario
user_input = st.text_input("Tu respuesta para x:", "")

# Botón para verificar
if st.button("Verificar"):
    try:
        user_x = float(user_input)
        if abs(user_x - x_real) < 1e-3:
            st.success("✅ ¡Correcto! 🎉")
            st.balloons()
        else:
            st.error(f"❌ Incorrecto. La respuesta correcta es x = {x_real}")
    except ValueError:
        st.warning("Por favor, ingresa un número válido.")
