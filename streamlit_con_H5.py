import streamlit as st
import numpy as np
import h5py
import requests
from io import BytesIO

# Función para descargar el archivo .h5 desde GitHub
def download_h5_from_github(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BytesIO(response.content)
    else:
        st.error("No se pudo descargar el archivo desde GitHub.")
        return None

# Función de inicio de sesión
def login():
    st.title("🩺 RehabGest EMG")
    st.subheader("Inicio de Sesión")
    st.markdown("Por favor, ingresa tus credenciales para continuar.")
    username = st.text_input("👤 Usuario", placeholder="Ingresa tu usuario")
    password = st.text_input("🔒 Contraseña", type="password", placeholder="Ingresa tu contraseña")
    
    if st.button("Iniciar sesión"):
        if username == "doctor" and password == "password":  # Placeholder de autenticación
            st.success("Inicio de sesión exitoso 🎉")
            return True
        else:
            st.error("❌ Usuario o contraseña incorrectos")
    return False

# Panel del doctor
def doctor_panel():
    st.title("Panel del Doctor 🩺")
    st.markdown("### Bienvenido al panel principal del doctor.")
    st.markdown("Desde aquí puedes acceder a las opciones disponibles para gestionar a tus pacientes y datos.")

# Gestión de pacientes
def manage_patients():
    st.title("Gestión de Pacientes 👥")
    st.markdown("### Aquí puedes gestionar toda la información relacionada con tus pacientes.")
    action = st.radio("Seleccione una acción:", ["Añadir nuevo paciente", "Seleccionar paciente"], horizontal=True)
    
    if action == "Añadir nuevo paciente":
        st.subheader("Añadir Nuevo Paciente")
        name = st.text_input("Nombre completo")
        age = st.number_input("Edad", min_value=0)
        sex = st.radio("Sexo", ["Masculino", "Femenino"], horizontal=True)
        dni = st.text_input("DNI")
        if st.button("Guardar Paciente"):
            st.success(f"✅ Paciente **{name}** añadido exitosamente.")
    
    elif action == "Seleccionar paciente":
        st.subheader("Seleccionar Paciente")
        search = st.text_input("Buscar paciente por nombre o DNI", placeholder="Ejemplo: Juan Pérez")
        if search:
            st.write("Resultados de búsqueda:")
            st.write(f"👤 Paciente encontrado: **{search}**")  # Simula un resultado
            if st.button("Seleccionar"):
                st.session_state["selected_patient"] = search
                st.success(f"✅ Paciente **{search}** seleccionado.")

# Perfil del paciente
def patient_profile():
    st.title("Perfil del Paciente 📋")
    patient = st.session_state.get("selected_patient", "Ninguno")
    if patient == "Ninguno":
        st.warning("⚠️ No se ha seleccionado un paciente.")
    else:
        st.markdown(f"### Paciente: {patient}")
        st.markdown("#### Información básica:")
        st.write("Edad: 35 años")  # Ejemplo, puedes conectar con una base de datos
        st.write("DNI: 74110803")
        
        # Descargar archivo H5 desde GitHub
        st.markdown("### Cargar archivo de modelo EMG desde GitHub (.h5)")
        if st.button("Cargar modelo .h5"):
            github_h5_url = "https://github.com/equipo17-fundbio/Estefany/raw/main/model1/emg_1.h5"  # Reemplaza con tu enlace real
            file = download_h5_from_github(github_h5_url)
            if file:
                try:
                    # Leer y procesar el archivo H5
                    with h5py.File(file, 'r') as f:
                        # Supongamos que las señales EMG están bajo la clave 'signals' en el archivo H5
                        signals = np.array(f['signals'])  # Ajusta esta clave a la estructura real de tu archivo H5
                        st.write(f"Se cargaron {signals.shape[0]} muestras de señales EMG.")
                        
                        # Mostrar un gráfico de las señales (si son 1D o 2D)
                        st.line_chart(signals[:100])  # Solo mostrando las primeras 100 muestras para visualización
                        
                        # Procesar señales y mostrar resultados
                        st.markdown("### Resultados del modelo:")
                        similarity_percentage = round(np.random.uniform(50, 100), 2)  # Simulación de porcentaje
                        st.info(f"El paciente realizó un **{similarity_percentage}%** del gesto esperado.")
                except Exception as e:
                    st.error(f"Error al procesar el archivo H5: {e}")

# Historial del paciente
def patient_history():
    st.title("Historial del Paciente 📜")
    st.markdown("### Progreso registrado:")
    st.table({"Fecha": ["2024-11-20", "2024-11-15"], "Avance (%)": [80, 70]})
    if st.button("Guardar y cerrar"):
        st.success("✅ Datos guardados exitosamente. Puede cerrar la sesión.")

# Configuración de cuenta
def account_settings():
    st.title("⚙️ Configuración de Cuenta")
    st.markdown("### Aquí puedes modificar tu información de cuenta.")
    
    with st.expander("Cambiar Nombre de Usuario"):
        new_username = st.text_input("Nuevo nombre de usuario", placeholder="Ingresa tu nuevo nombre de usuario")
        if st.button("Actualizar Nombre de Usuario"):
            if new_username.strip():
                st.success(f"✅ Nombre de usuario actualizado a: **{new_username}**")
            else:
                st.error("⚠️ Por favor, ingresa un nombre de usuario válido.")
    
    with st.expander("Cambiar Contraseña"):
        current_password = st.text_input("Contraseña actual", type="password", placeholder="Ingresa tu contraseña actual")
        new_password = st.text_input("Nueva contraseña", type="password", placeholder="Ingresa tu nueva contraseña")
        confirm_password = st.text_input("Confirmar nueva contraseña", type="password", placeholder="Confirma tu nueva contraseña")
        if st.button("Actualizar Contraseña"):
            if new_password == confirm_password and new_password.strip():
                st.success("✅ Contraseña actualizada exitosamente.")
            else:
                st.error("⚠️ Las contraseñas no coinciden o no son válidas.")
    
    with st.expander("Cambiar Correo Electrónico"):
        new_email = st.text_input("Nuevo correo electrónico", placeholder="Ingresa tu nuevo correo electrónico")
        if st.button("Actualizar Correo Electrónico"):
            if "@" in new_email and "." in new_email:
                st.success(f"✅ Correo electrónico actualizado a: **{new_email}**")
            else:
                st.error("⚠️ Por favor, ingresa un correo electrónico válido.")

# Integración principal
def main():
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    if not st.session_state["authenticated"]:
        st.session_state["authenticated"] = login()
    else:
        option = st.selectbox(
            "Opciones",
            ["Panel del Doctor", "Gestión de Pacientes", "Perfil del Paciente", "Historial del Paciente", "Configuración de Cuenta"],
            index=0,
            key="main_menu"
        )
        
        if option == "Panel del Doctor":
            doctor_panel()
        elif option == "Gestión de Pacientes":
            manage_patients()
        elif option == "Perfil del Paciente":
            patient_profile()
        elif option == "Historial del Paciente":
            patient_history()
        elif option == "Configuración de Cuenta":
            account_settings()

# Punto de entrada
if __name__ == "__main__":
    main()

