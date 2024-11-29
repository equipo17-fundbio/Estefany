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
    La rehabilitación física, especialmente en pacientes con discapacidades motoras o aquellos en proceso de recuperación tras lesiones, representa un desafío significativo debido a la necesidad de monitoreo y evaluación constante a lo largo del tratamiento. Según la Organización Mundial de la Salud (OMS), aproximadamente 2.41 mil millones de personas en el mundo presentan condiciones que afectan su movilidad. Sin embargo, solo 1 de cada 5 personas que requieren rehabilitación recibe los servicios necesarios debido a barreras de acceso y recursos limitados [1].

    En el ámbito laboral, sectores como manufactura, transporte e inmobiliaria registran una alta incidencia de accidentes laborales. Según el Ministerio de Trabajo y Promoción del Empleo (MTPE), se reportaron más de 10,800 casos en un periodo de apenas cuatro meses en 2022. De estos, el 36% de las atenciones médicas por accidentes de trabajo corresponden a lesiones en brazos y manos, subrayando la importancia de abordar estas lesiones [2].

    En la última década, la electromiografía (EMG) ha emergido como una herramienta crucial para evaluar y monitorear la actividad muscular en tiempo real en contextos clínicos y de investigación. Estudios recientes han demostrado que los sistemas de reconocimiento de gestos basados en EMG alcanzan precisiones superiores al 90 % en condiciones controladas [3][4], lo cual es clave para aplicaciones en telemedicina y rehabilitación remota.

    La integración de tecnologías avanzadas ha optimizado las estrategias de tratamiento personalizado, mejorando la calidad de vida de personas con discapacidades motrices. Los modelos de redes neuronales destacan como herramientas revolucionarias para analizar datos complejos, particularmente en el procesamiento de señales EMG para aplicaciones de rehabilitación [5]. Estas plataformas permiten a los profesionales de la salud realizar evaluaciones continuas desde cualquier lugar, fomentando la telemedicina y mejorando la accesibilidad a los servicios de rehabilitación.

    ### Planteamiento de la problemática
    La rehabilitación física de pacientes con lesiones en extremidades superiores, particularmente en manos y muñecas, enfrenta desafíos significativos debido a la ausencia de monitoreo constante y evaluación precisa en cada etapa del tratamiento. Aunque la electromiografía ha demostrado ser eficaz en la medición de actividad muscular y reconocimiento de gestos, los sistemas actuales no ofrecen una evaluación continua accesible para pacientes y profesionales de la salud.
    
    Adicionalmente, la implementación de redes neuronales en el análisis de señales EMG aún es limitada, dificultando evaluaciones precisas en tiempo real. Ante esta problemática, se propone el desarrollo de una plataforma web accesible que integre modelos de redes neuronales para clasificar gestos musculares a partir de señales EMG. Este sistema permitirá diferenciar movimientos como puño cerrado, mano abierta, flexión y extensión de muñeca, optimizando el monitoreo continuo en rehabilitación.

    ### Solución propuesta
    Basándose en una base de datos previa, se propone desarrollar un modelo de red neuronal para clasificar señales EMG asociadas a gestos musculares específicos, integrándolo en una plataforma web interactiva. Este enfoque permitirá a los profesionales de la salud monitorear el progreso de los pacientes en tiempo real, optimizando tratamientos terapéuticos.
    
    La implementación incluye un modelo de red neuronal profunda, con transferencia de aprendizaje para maximizar la precisión y generalización. Este sistema se integrará en una página web accesible, desarrollada con Streamlit, para facilitar la interacción y análisis inmediato de las señales EMG.
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
