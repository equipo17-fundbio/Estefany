import streamlit as st
import numpy as np
import time

# Función de inicio de sesión
def login():
    st.title("🩺 RehabGest EMG")
    st.subheader("Inicio de Sesión")
    st.markdown("Por favor, ingresa tus credenciales para continuar.")
    username = st.text_input("👤 Usuario", placeholder="Ingresa tu usuario")
    password = st.text_input("🔒 Contraseña", type="password", placeholder="Ingresa tu contraseña")
    
    if st.button("Iniciar sesión"):
        if username == "doctor" and password == "password":  # Placeholder de autenticación
            st.session_state["logged_in"] = True
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

    # Información del proyecto
    st.markdown(""" 
    ## Desarrollo de una plataforma Web para el Reconocimiento de Gestos con EMG para Aplicaciones en Rehabilitación Remota
    ### Introducción
    La rehabilitación física, especialmente en pacientes con discapacidades motoras o aquellos en proceso de recuperación tras lesiones, representa un desafío significativo...
    """)

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
            if name and dni:
                st.success(f"✅ Paciente **{name}** añadido exitosamente.")
                # Simulamos agregar el paciente a una base de datos
                st.session_state["patients"] = st.session_state.get("patients", []) + [{"name": name, "dni": dni}]
            else:
                st.error("⚠️ Nombre y DNI son obligatorios.")
    
    elif action == "Seleccionar paciente":
        st.subheader("Seleccionar Paciente")
        search = st.text_input("Buscar paciente por nombre o DNI", placeholder="Ejemplo: Juan Pérez")
        
        if search:
            found_patients = [patient for patient in st.session_state.get("patients", []) if search.lower() in patient["name"].lower() or search.lower() in patient["dni"]]
            if found_patients:
                st.write("Resultados de búsqueda:")
                for patient in found_patients:
                    st.write(f"👤 Paciente encontrado: **{patient['name']}**")
                    if st.button(f"Seleccionar {patient['name']}"):
                        st.session_state["selected_patient"] = patient
                        st.success(f"✅ Paciente **{patient['name']}** seleccionado.")
            else:
                st.warning("⚠️ No se encontró ningún paciente con ese nombre o DNI.")

# Perfil del paciente
def patient_profile():
    st.title("Perfil del Paciente 📋")
    
    if "selected_patient" not in st.session_state:
        st.warning("⚠️ No se ha seleccionado un paciente.")
        return
    
    patient = st.session_state["selected_patient"]
    st.markdown(f"### Paciente: {patient['name']}")
    st.markdown("#### Información básica:")
    st.write(f"Edad: 35 años")  # Ejemplo, puedes conectar con una base de datos real
    st.write(f"DNI: {patient['dni']}")
        
    # Subir archivo TXT
    st.markdown("### Subir archivo de señales EMG (.txt)")
    uploaded_file = st.file_uploader("Subir archivo TXT", type="txt")
    
    if uploaded_file:
        st.success("📁 Carga de archivo completa.")
            
        # Selección del gesto a analizar
        gesture = st.selectbox(
            "Selecciona el gesto a analizar",
            ["Mano en reposo", "Mano cerrada en un puño", "Flexión de la muñeca", "Extensión de la muñeca", "Desviación radial", "Desviación cubital"]
        )
        
        # Simular procesamiento
        if gesture:
            with st.spinner("Procesando datos..."):
                time.sleep(3)  # Simula el tiempo de procesamiento
                
            # Simular resultado de análisis
            similarity_percentage = round(np.random.uniform(50, 100), 2)  # Simulación de porcentaje
            st.success(f"El paciente realizó un **{similarity_percentage}%** del gesto esperado: **{gesture}**.")

# Historial del paciente
def patient_history():
    st.title("Historial del Paciente 📜")
    st.markdown("### Progreso registrado:")
    
    if "selected_patient" in st.session_state:
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
                st.error("⚠️ Las contraseñas no coinciden o son inválidas.")

# Main function to control the app flow
def main():
    if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
        if not login():
            return
    
    # Menu principal del doctor
    menu = st.sidebar.selectbox("Seleccione una opción", ["Panel del Doctor", "Gestión de Pacientes", "Perfil del Paciente", "Historial del Paciente", "Configuración de Cuenta"])
    
    if menu == "Panel del Doctor":
        doctor_panel()
    elif menu == "Gestión de Pacientes":
        manage_patients()
    elif menu == "Perfil del Paciente":
        patient_profile()
    elif menu == "Historial del Paciente":
        patient_history()
    elif menu == "Configuración de Cuenta":
        account_settings()

if __name__ == "__main__":
    main()
