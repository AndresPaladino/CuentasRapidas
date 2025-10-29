import streamlit as st
import random

# Configuración de la página
st.set_page_config(
    page_title="Cuentas Rápidas",
    page_icon="🧮",
    layout="centered"
)

# CSS personalizado para reducir el ancho de la sidebar
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        min-width: 0px;
        max-width: 200px;
    }
    </style>
    """, unsafe_allow_html=True)

# Inicializar el estado de la sesión
if 'operacion' not in st.session_state:
    st.session_state.operacion = None
    st.session_state.resultado = None
    st.session_state.mostrar_resultado = False

def generar_operacion():
    """Genera una multiplicacion matemática aleatoria"""
    num1 = random.randint(2, 8)
    num2 = random.randint(1, 10)
    resultado = num1 * num2
    operacion_texto = f"{num1} × {num2}"
    return operacion_texto, resultado

# Título de la aplicación
st.title("🧮 Cuentas Rápidas")

# Generar operación inicial si no existe
if st.session_state.operacion is None:
    st.session_state.operacion, st.session_state.resultado = generar_operacion()
    st.session_state.mostrar_resultado = False

# Mostrar la operación en grande
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.session_state.mostrar_resultado:
        st.markdown(f"<h1 style='text-align: center; color: #4CAF50; font-size: 60px;'>{st.session_state.operacion} = {st.session_state.resultado}</h1>", 
                    unsafe_allow_html=True)
    else:
        st.markdown(f"<h1 style='text-align: center; color: #2196F3; font-size: 60px;'>{st.session_state.operacion} = ?</h1>", 
                    unsafe_allow_html=True)

st.markdown("---")

# Botones de acción
col1, col2 = st.columns(2)

with col1:
    boton_texto = "Ocultar Resultado" if st.session_state.mostrar_resultado else "Mostrar Resultado"
    if st.button(boton_texto, use_container_width=True):
        st.session_state.mostrar_resultado = not st.session_state.mostrar_resultado
        st.rerun()

with col2:
    if st.button("🔄 Nueva Operación", use_container_width=True):
        st.session_state.operacion, st.session_state.resultado = generar_operacion()
        st.session_state.mostrar_resultado = False
        st.rerun()

# Información adicional en el sidebar
with st.sidebar:
    st.header("ℹ️ Información")
    st.markdown("---")
    st.write("**Instrucciones:**")
    st.write("1. Lee la operación")
    st.write("2. Intenta resolverla mentalmente")
    st.write("3. Haz clic en 'Mostrar Resultado' para ver la respuesta")
    st.write("4. Usa 'Nueva Operación' para practicar más")
