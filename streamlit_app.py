import streamlit as st

# Función para mostrar el logo y título clickeable en todas las páginas
def show_header():
    st.markdown("""
        <div style="display: flex; align-items: center; justify-content: center; gap: 10px; margin-bottom: 20px;">
            <a href="/" style="text-decoration: none; color: white; display: flex; align-items: center;">
                <img src="logo.png" alt="Logo" style="height: 50px; vertical-align: middle;">
                <h1 style="margin: 0; font-size: 24px; color: white;">RehabGest EMG</h1>
            </a>
        </div>
    """, unsafe_allow_html=True)

# Función de inicio de sesión
def login():
    show_header()  # Mostrar el encabezado con el logo
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
    show_header()  # Mostrar el encabezado con el logo
    st.title("Panel del Doctor 🩺")
    st.markdown("### Bienvenido al panel principal del doctor.")
    st.markdown("Desde aquí puedes acceder a las opciones disponibles para gestionar a tus pacientes y datos.")
    
    # Botón de configuración de cuenta
    st.markdown("---")
    if st.button("⚙️ Configuración de Cuenta"):
        st.info("Puedes modificar tu información de cuenta en la sección dedicada.")

# Gestión de pacientes
def manage_patients():
    show_header()  # Mostrar el encabezado con el logo
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
    show_header()  # Mostrar el encabezado con el logo
    st.title("Perfil del Paciente 📋")
    patient = st.session_state.get("selected_patient", "Ninguno")
    if patient == "Ninguno":
        st.warning("⚠️ No se ha seleccionado un paciente.")
    else:
        st.markdown(f"### Paciente: {patient}")
        st.markdown("#### Información básica:")
        st.write("Edad: 35 años")  # Ejemplo, puedes conectar con una base de datos
        st.write("DNI: 74110803")
        
        # Subir archivo TXT
        st.markdown("### Subir archivo de señales EMG")
        uploaded_file = st.file_uploader("Subir archivo TXT", type="txt")
        if uploaded_file:
            st.success("📁 Archivo cargado exitosamente.")
            data = uploaded_file.read().decode("utf-8")  # Procesar archivo
            st.text_area("Vista previa del archivo:", data[:500], height=200)
            
            # Visualización de resultados
            st.markdown("### Resultados del modelo:")
            progress = st.slider("Porcentaje del gesto realizado correctamente:", 0, 100, 80)
            st.info(f"El paciente realizó un **{progress}%** del gesto esperado.")

# Historial del paciente
def patient_history():
    show_header()  # Mostrar el encabezado con el logo
    st.title("Historial del Paciente 📜")
    st.markdown("### Progreso registrado:")
    st.table({"Fecha": ["2024-11-20", "2024-11-15"], "Avance (%)": [80, 70]})
    if st.button("Guardar y cerrar"):
        st.success("✅ Datos guardados exitosamente. Puede cerrar la sesión.")

# Configuración de cuenta
def account_settings():
    show_header()  # Mostrar el encabezado con el logo
    st.title("⚙️ Configuración de Cuenta")
    st.markdown("### Aquí puedes modificar tu información de cuenta.")
    
    # Sección de cambio de datos
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
