import streamlit as st

# Función de inicio de sesión
def login():
    st.title("RehabGest EMG")
    st.subheader("Inicio de Sesión")
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    if st.button("Iniciar sesión"):
        if username == "doctor" and password == "password":  # Placeholder de autenticación
            st.success("Inicio de sesión exitoso")
            return True
        else:
            st.error("Usuario o contraseña incorrectos")
    return False

# Panel del doctor
def doctor_panel():
    st.sidebar.title("Panel del Doctor")
    st.sidebar.button("Gestión de Pacientes")
    st.sidebar.button("Configuración de Cuenta")

# Gestión de pacientes
def manage_patients():
    st.title("Gestión de Pacientes")
    action = st.radio("Seleccione una acción:", ["Añadir nuevo paciente", "Seleccionar paciente"])
    
    if action == "Añadir nuevo paciente":
        name = st.text_input("Nombre completo")
        age = st.number_input("Edad", min_value=0)
        sex = st.radio("Sexo", ["Masculino", "Femenino"])
        dni = st.text_input("DNI")
        if st.button("Guardar Paciente"):
            st.success(f"Paciente {name} añadido exitosamente.")
    
    elif action == "Seleccionar paciente":
        search = st.text_input("Buscar paciente por nombre o DNI")
        if search:
            st.write("Resultados de búsqueda:")
            st.write(f"Paciente: {search}")  # Simula un resultado
            if st.button("Seleccionar"):
                st.session_state["selected_patient"] = search
                st.success(f"Paciente {search} seleccionado")

# Subida de archivos y visualización
def patient_profile():
    st.title("Perfil del Paciente")
    st.write(f"Paciente: {st.session_state.get('selected_patient', 'Ninguno')}")
    uploaded_file = st.file_uploader("Subir archivo TXT de señales EMG", type="txt")
    
    if uploaded_file:
        st.write("Archivo cargado exitosamente")
        # Procesamiento de archivo
        data = uploaded_file.read()
        st.write("Datos:")
        st.text(data[:500])  # Muestra una vista previa del archivo
        
        # Simulación de clasificación
        st.write("Resultados del modelo:")
        progress = st.slider("Porcentaje del gesto realizado correctamente", 0, 100, 80)
        st.success(f"El paciente realizó un {progress}% del gesto esperado.")

# Historial y cierre
def history_and_save():
    st.title("Historial del Paciente")
    st.write("Aquí se mostrarán las fechas y porcentajes de avance:")
    st.table({"Fecha": ["2024-11-20", "2024-11-15"], "Avance (%)": [80, 70]})
    
    if st.button("Guardar y cerrar"):
        st.success("Datos guardados exitosamente. Puede cerrar la sesión.")

# Integración principal
def main():
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    if not st.session_state["authenticated"]:
        st.session_state["authenticated"] = login()
    else:
        st.sidebar.title("RehabGest EMG")
        option = st.sidebar.selectbox("Opciones", ["Panel del Doctor", "Gestión de Pacientes", "Perfil del Paciente", "Historial"])
        
        if option == "Panel del Doctor":
            doctor_panel()
        elif option == "Gestión de Pacientes":
            manage_patients()
        elif option == "Perfil del Paciente":
            patient_profile()
        elif option == "Historial":
            history_and_save()

# Punto de entrada
if __name__ == "__main__":
    main()
