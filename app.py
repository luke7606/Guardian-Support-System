import streamlit as st

# Base de datos simple de usuarios
USERS = [
    {"username": "admin", "password": "admin123", "role": "admin"},
    {"username": "interno", "password": "interno123", "role": "internal"},
    {"username": "externo", "password": "externo123", "role": "external"}
]

def simple_login():
    st.sidebar.title("Iniciar Sesión")
    username = st.sidebar.text_input("Usuario")
    password = st.sidebar.text_input("Contraseña", type="password")

    if st.sidebar.button("Login"):
        user = next((u for u in USERS if u["username"] == username and u["password"] == password), None)
        if user:
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            st.session_state["role"] = user["role"]
            st.success(f"Bienvenido {username} ({user['role']})")
        else:
            st.error("Credenciales incorrectas")

def logout():
    if st.sidebar.button("Cerrar sesión"):
        st.session_state.clear()
        st.experimental_rerun()

# Inicialización del estado de sesión
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# Lógica principal
if not st.session_state["authenticated"]:
    simple_login()
else:
    logout()
    st.title("🔐 Guardian Support System")
    st.sidebar.write(f"Usuario: {st.session_state['username']}")
    st.sidebar.write(f"Rol: {st.session_state['role']}")

    if st.session_state["role"] == "admin":
        st.header("Panel de Administración ⚙️")
    elif st.session_state["role"] == "internal":
        st.header("Panel de Soporte Interno 🛠️")
    elif st.session_state["role"] == "external":
        st.header("Portal del Cliente 🌐")
    else:
        st.warning("Rol no asignado. Contacta al administrador.")
