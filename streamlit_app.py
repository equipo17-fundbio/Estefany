import streamlit as st

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
    
    # Botón de configuración de cuenta
    st.markdown("---")
    if st.button("⚙️ Configuración de Cuenta"):
        st.info("Aquí puedes modificar tus datos, como usuario y contraseña. (Función por implementar)")

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
    st.title("Historial del Paciente 📜")
    st.markdown("### Progreso registrado:")
    st.table({"Fecha": ["2024-11-20", "2024-11-15"], "Avance (%)": [80, 70]})
    if st.button("Guardar y cerrar"):
        st.success("✅ Datos guardados exitosamente. Puede cerrar la sesión.")

# Integración principal
def main():
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    if not st.session_state["authenticated"]:
        st.session_state["authenticated"] = login()
    else:
        st.markdown("<h1 style='text-align: center; color: white;'>RehabGest EMG</h1>", unsafe_allow_html=True)
        st.markdown("## Selecciona una opción para continuar:")
        
        option = st.selectbox(
            "Opciones",
            ["Panel del Doctor", "Gestión de Pacientes", "Perfil del Paciente", "Historial del Paciente"],
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

# Punto de entrada
if __name__ == "__main__":
    main()
