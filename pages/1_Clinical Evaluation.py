import streamlit as st
import pandas as pd
import pickle
import os

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Medical Aesthetic", layout="centered")

# 2. CSS ESTÉTICA LUXURY (Fondos neutros, tipografía elegante)
st.markdown("""
<style>
    /* Usamos una fuente tipo Serif para ese look "Luxury" */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;500&display=swap');
    
    .stApp { 
        background-color: #F8F5F2 !important; /* Fondo crema suave, nada de negro agresivo */
        font-family: 'Inter', sans-serif !important; 
    }
    
    h1, h2, h3 { font-family: 'Playfair Display', serif !important; color: #2C2C2C !important; }
    
    /* Inputs: Minimalistas, fondo transparente, solo borde inferior */
    input, div[data-baseweb="input"], div[data-baseweb="select"] {
        background-color: transparent !important;
        color: #4A4A4A !important;
        border: none !important;
        border-bottom: 1px solid #D1CCC7 !important;
        border-radius: 0px !important;
        padding-left: 0 !important;
    }
    
    label { color: #8C8C8C !important; font-size: 12px !important; text-transform: uppercase; letter-spacing: 1px; }

    /* Botón Aesthetic: Minimalista, nada de gradientes de juego */
    div.stButton > button, div.stFormSubmitButton > button {
        background-color: #2C2C2C !important;
        color: #F8F5F2 !important;
        border: none !important;
        border-radius: 0px !important;
        font-weight: 400 !important;
        letter-spacing: 2px !important;
        height: 50px !important;
        width: 100% !important;
        transition: 0.4s !important;
    }
    div.stButton > button:hover { background-color: #5C5C5C !important; cursor: pointer; }

    /* Tarjetas de resultados */
    .aesthetic-card { 
        background: #FFFFFF; 
        padding: 40px; 
        border-radius: 0px; 
        border: 1px solid #EAEAEA;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# 3. CARGA DE MODELO (Misma lógica)
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(os.path.dirname(current_dir))
ruta_modelo = os.path.join(root_dir, "models", "modelo_coste.pkl")
with open(ruta_modelo, "rb") as f:
    modelo = pickle.load(f)

# 4. LÓGICA 
# 4. LÓGICA
def obtener_clasificacion_y_kpis(
    edad,
    procedimiento,
    seguro,
    prob_modelo
):

    # Costes base
    precios = {
        "Botox": 800,
        "Rinoplastia": 4500,
        "Lifting": 6000,
        "Liposucción": 3500,
        "Aumento mamario": 5000
    }

    # Recuperación base
    recuperacion_base = {
        "Botox": 2,
        "Rinoplastia": 14,
        "Lifting": 21,
        "Liposucción": 10,
        "Aumento mamario": 14
    }

    # Satisfacción esperada
    satisfaccion_base = {
        "Botox": 96,
        "Rinoplastia": 92,
        "Lifting": 90,
        "Liposucción": 88,
        "Aumento mamario": 91
    }

    precio_base = precios.get(
        procedimiento,
        3000
    )

    recup_base = recuperacion_base.get(
        procedimiento,
        10
    )

    sat_base = satisfaccion_base.get(
        procedimiento,
        90
    )

    # ==================================
    # REGLAS DE RIESGO
    # ==================================

    procedimientos_alto_riesgo = [

        "Rinoplastia",

        "Aumento mamario",

        "Lifting"

    ]

    if (

        edad >= 70

        and

        procedimiento in procedimientos_alto_riesgo

    ):

        res = "Riesgo Operativo"

        prob = 0.95

    elif edad >= 80:

        res = "Riesgo Operativo"

        prob = 0.98

    else:

        res = (

            "Riesgo Operativo"

            if prob_modelo >= 0.5

            else

            "Beneficio Operativo"

        )

        prob = prob_modelo

    # ==================================
    # KPI SEGÚN RESULTADO
    # ==================================

    if res == "Riesgo Operativo":

        coste = (

            precio_base

            + 2000

            + (edad * 15)

        )

        recup = (

            recup_base

            + int(edad / 12)

        )

        sat = max(

            55,

            sat_base - (edad // 6)

        )

    else:

        coste = (

            precio_base

            + (edad * 4)

        )

        recup = (

            recup_base

            + int(edad / 25)

        )

        sat = max(

            75,

            sat_base - (edad // 18)

        )

    # Seguro

    if seguro:

        coste *= 0.7

    return (

        res,

        round(prob, 2),

        int(coste),

        int(recup),

        int(sat)

    )
# 5. UI ESTÉTICA
st.markdown('<h1 style="text-align: center;">Medical Evaluation</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #8C8C8C; margin-bottom: 50px;">Private Clinical Assessment</p>', unsafe_allow_html=True)

with st.form("unico_formulario"):
    nombre = st.text_input("Full Name")
    c1, c2 = st.columns(2)
    with c1:
        edad = st.number_input("Age", 18, 99, 35)
        genero = st.selectbox("Gender", ["Female", "Male", "Non-binary"])
    with c2:
        procedimiento = st.selectbox("Procedure", ["Botox", "Rinoplastia", "Lifting", "Liposucción", "Aumento mamario"])
        seguro = st.selectbox("Insurance", [True, False])
    st.write("")
    enviar = st.form_submit_button("PROCESS ASSESSMENT")

# 6. RESULTADOS
if enviar:
    paciente = pd.DataFrame({"edad": [edad], "genero": [genero], "procedimiento": [procedimiento], "tiene_seguro": [seguro]})
    paciente = pd.get_dummies(paciente).reindex(columns=modelo.feature_names_in_, fill_value=0)
    prob_modelo = modelo.predict_proba(paciente)[0][list(modelo.classes_).index("Riesgo Operativo")]
    res, prob, coste, recup, sat = obtener_clasificacion_y_kpis(edad, procedimiento, seguro, prob_modelo)
    
    st.markdown("---")
    st.markdown(f"<h2 style='text-align:center;'>{res}</h2>", unsafe_allow_html=True)
    
    # KPIs en formato minimalista
    c1, c2, c3 = st.columns(3)
    c1.metric("Cost", f"${coste:,}")
    c2.metric("Recovery", f"{recup} Days")
    c3.metric("Satisfaction", f"{sat}%")