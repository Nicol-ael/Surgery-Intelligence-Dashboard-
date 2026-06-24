import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_plotly_events import plotly_events



# ==========================================================
# CONFIG
# ==========================================================
st.set_page_config(
    layout="wide",
    page_title="Surgery Analytics Pro",
    initial_sidebar_state="collapsed"
)


# ==========================================================
# PREMIUM MEDICAL UI
# ==========================================================


st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap" rel="stylesheet">
<style>
            <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">

<style>

/* =========================
GLOBAL
========================= */

html, body, [class*="css"]{
    font-family:'Inter',sans-serif;
}

.stApp{
    background:#F8F5F2;
}

.block-container{

    max-width:1500px;

    padding-top:3rem;

    padding-bottom:5rem;

    padding-left:5rem;

    padding-right:5rem;

}

/* =========================
SIDEBAR
========================= */

[data-testid="stSidebar"]{

    background:#F2EEEA !important;

    border-right:1px solid #E3DDD7 !important;

}

[data-testid="stSidebar"] h1{

    font-family:'Playfair Display';

    color:#2B2A29;

    font-size:26px;

}

/* =========================
HEADER
========================= */

.header-box{

    background:transparent;

    border:none;

    text-align:center;

    margin-bottom:48px;

}

.header-title{

    font-family:'Playfair Display';

    font-size:62px;

    font-weight:700;

    color:#2B2A29;

    letter-spacing:-2px;

    line-height:1.05;

}

.header-sub{

    margin-top:14px;

    color:#9A958F;

    font-size:12px;

    text-transform:uppercase;

    letter-spacing:3px;

}

/* =========================
TYPOGRAPHY
========================= */

h1,h2,h3{

    font-family:'Playfair Display';

    color:#2B2A29;

}

p,label{

    color:#8D8882;

}

/* =========================
METRICS
========================= */

[data-testid="stMetric"]{

    background:#FCFBF9;

    border:1px solid #E6E0D9;

    border-radius:30px;

    padding:34px;

    min-height:180px;

    box-shadow:none;

    transition:.15s;

}

[data-testid="stMetric"]:hover{

    border-color:#CEC6BE;

    transform:translateY(-1px);

}

[data-testid="stMetricLabel"]{

    color:#9A958F;

    text-transform:uppercase;

    font-size:11px;

    letter-spacing:2px;

}

[data-testid="stMetricValue"]{

    font-family:'Playfair Display';

    color:#2B2A29;

    font-size:44px;

    font-weight:600;

}

/* =========================
BUTTON
========================= */

.stButton button{

    background:#2B2A29;

    color:#F8F5F2;

    border:none;

    border-radius:0;

    height:54px;

    letter-spacing:2px;

    font-size:12px;

    font-weight:500;

}

.stButton button:hover{

    background:#55504B;

}

/* =========================
INPUTS
========================= */

div[data-baseweb="select"],
.stSlider{

    background:transparent !important;

    border:none !important;

    border-bottom:1px solid #D8D1CA !important;

    border-radius:0 !important;

}

/* =========================
PLOTLY
========================= */

.stPlotlyChart{

    background:#FCFBF9;

    border:1px solid #E6E0D9;

    border-radius:34px;

    padding:24px;

    margin-bottom:28px;

    box-shadow:none;

}

.stPlotlyChart:hover{

    border-color:#CEC6BE;

}

/* =========================
DIVIDER
========================= */

hr{

    display:none;

}
.stPlotlyChart:hover{
border-color:#CEC6BE;
}

            /* =========================
CAMBIAR ROJO DEL SLIDER
========================= */

:root{
--primary-color:#2563EB !important;
}

/* fuerza azul */
.stSlider{
color:#2563EB !important;
}

.stSlider [data-baseweb="slider"]{
color:#2563EB !important;
}

.stSlider [role="slider"]{
border-color:#2563EB !important;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# DATA
# ==========================================================
from pathlib import Path

@st.cache_data
def load_data():

    ruta = Path(__file__).parent / "surgeryplastic.csv"

    df = pd.read_csv(ruta)

    df.columns = df.columns.str.strip()

    return df


df = load_data()

# ==========================================================
# SESSION
# ==========================================================
if "pais_sel" not in st.session_state:
    st.session_state.pais_sel = None

if "proc_sel" not in st.session_state:
    st.session_state.proc_sel = None


# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:


    # ------------------
    # LOGO
    # ------------------

    st.markdown(
    """
    <div style='height:18px'></div>
    """,
    unsafe_allow_html=True
    )

    st.image(
        "./image2.png",
        use_container_width=True
    )

    st.markdown(
    """
    <div style='height:22px'></div>
    """,
    unsafe_allow_html=True
    )


    # ------------------
    # FILTER TITLE
    # ------------------

    st.markdown("""
    <div style="
    margin-bottom:18px;
    font-size:11px;
    letter-spacing:2px;
    color:#9A958F;
    text-transform:uppercase;
    ">
    Filters
    </div>
    """,
    unsafe_allow_html=True)


    # =====================
    # COUNTRY
    # =====================

    f_pais = st.selectbox(

        "Country",

        options=[

            "Select all"

        ]

        +

        sorted(

            df["pais"]

            .dropna()

            .unique()

        ),

        key="country_filter"

    )



    # =====================
    # GENDER
    # =====================

    f_genero = st.selectbox(

        "Gender",

        options=[

            "Select all"

        ]

        +

        sorted(

            df["genero"]

            .dropna()

            .unique()

        ),

        key="gender_filter"

    )



    # =====================
    # AGE RANGE
    # =====================

    st.markdown("Age Range")


    edades = list(
        range(
            int(df["edad"].min()),
            int(df["edad"].max()) + 1
        )
    )


    c1, c2 = st.columns(2)


    with c1:

        edad_min = st.selectbox(

            "From",

            options=edades,

            index=0

        )


    with c2:

        edad_max = st.selectbox(

            "To",

            options=edades,

            index=len(edades)-1

        )


    f_edad = (

        min(
            edad_min,
            edad_max
        ),

        max(
            edad_min,
            edad_max
        )

    )







# =====================
# FILTER
# =====================

df_filt = df.copy()


# AGE
df_filt = df_filt[
    df_filt["edad"].between(*f_edad)
]

# --- FILTRO DE PROCEDIMIENTO EN LA BARRA LATERAL ---
# Obtenemos la lista única de procedimientos disponibles
lista_procedimientos = ["Select all"] + sorted(df["tipo_procedimiento"].unique().tolist())

f_procedimiento = st.sidebar.selectbox(
    "Procedimiento",
    lista_procedimientos
)

# Aplicar el filtro al DataFrame
if f_procedimiento != "Select all":
    df_filt = df_filt[
        df_filt["tipo_procedimiento"] == f_procedimiento
    ]

# COUNTRY
if f_pais != "Select all":

    df_filt = df_filt[
        df_filt["pais"]
        ==
        f_pais
    ]



# GENDER
if f_genero != "Select all":

    df_filt = df_filt[
        df_filt["genero"]
        ==
        f_genero
    ]


# COUNTRY CLICK
if st.session_state.pais_sel:

    df_filt = df_filt[
        df_filt["pais"]
        ==
        st.session_state.pais_sel
    ]



# ==========================================================
# HEADER
# ==========================================================
st.markdown("""
<div class="header-box">

<div class="header-title">
Surgery Analytics Dashboard
</div>

<div class="header-sub">
Premium surgery intelligence dashboard
</div>

</div>
""", unsafe_allow_html=True)


# ==========================================================
# KPI
# ==========================================================
# Cálculos actualizados con el nombre correcto de la columna
total_patients = len(df_filt)
avg_cost = df_filt['coste_usd'].mean() if not df_filt.empty else 0
avg_satisfaction = df_filt['indice_satisfaccion'].mean() if not df_filt.empty else 0
avg_recovery = df_filt['dias_recuperacion'].mean() if not df_filt.empty else 0

# Renderizado de KPIs
k1, k2, k3, k4 = st.columns(4, gap="large")

with k1:
    st.metric("Total Patients", f"{total_patients:,}")

with k2:
    st.metric("Avg. Cost", f"${avg_cost:,.0f}")

with k3:
    st.metric("Avg. Satisfaction", f"{avg_satisfaction:.1f} / 10")

with k4:
    st.metric("Avg. Recovery", f"{avg_recovery:.1f} ")

st.markdown("""
<style>
.section-divider{
    margin-top:-200px;   /* súbela */
    margin-bottom:30px;
    border:none;
    border-top:2px solid #2f3640;
}
</style>

<hr class="section-divider">
""", unsafe_allow_html=True)


# ==========================================================
# GRAPH STYLE
# ==========================================================
def clean(fig):

    fig.update_layout(

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            family="Inter",
            color="#111827"
        ),

        title=dict(
            x=0,
            font=dict(
                size=18
            )
        ),

        margin=dict(
            l=10,
            r=10,
            t=60,
            b=10
        ),

        showlegend=False,

        xaxis=dict(
            showgrid=False,
            zeroline=False,
            linecolor="rgba(0,0,0,0)"
        ),

        yaxis=dict(
            showgrid=False,
            zeroline=False,
            linecolor="rgba(0,0,0,0)"
        )
    )

    return fig


# ==========================================================
# CABECERA: EL MUÑECO (Centrado y arriba)
# ==========================================================
# Quitamos las columnas left/right para que el muñeco ocupe el ancho superior
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
import streamlit as st
import plotly.express as px

# CSS para el posicionamiento del muñeco y transparencia global
st.markdown("""
    <style>
    .muñeco-ajustado {
        margin-left: -150px; 
    }
    .stPlotlyChart { background-color: transparent !important; }
    </style>
""", unsafe_allow_html=True)

# ===================================
# MUÑECO + PROCEDURE DONUT
# ===================================
# Ajuste: usamos 'top' en el align para que estén alineados desde arriba



body_col, donut_col = st.columns([0.8, 1.2], gap="small")

# ------------------
# MUÑECO
# ------------------


with body_col:

    # Detecta procedimiento dominante
    if len(df_filt):

        proc_chart = (
            df_filt
            .groupby(
                "tipo_procedimiento"
            )
            .size()
            .reset_index(
                name="patients"
            )
        )

        proc = (
            proc_chart
            .sort_values(
                "patients",
                ascending=False
            )
            .iloc[0][
                "tipo_procedimiento"
            ]
        )

    else:

        proc = None


    # Glow por procedimiento
    glow_map = {

        "Aumento de mamas":
        "rgba(37,99,235,.18)",

        "Rinoplastia":
        "rgba(146,64,14,.20)",

        "Liposucción":
        "rgba(100,116,139,.22)",

        "Lifting":
        "rgba(245,230,211,.40)",

        "Botox":
        "rgba(160,65,0,.20)"
    }


    glow = glow_map.get(
        proc,
        "rgba(180,180,180,.10)"
    )


    st.markdown(
        f"""
        <style>

        .muñeco-ajustado{{

            position:relative;

            display:flex;

            justify-content:center;

            margin-left:-120px;

            margin-top:-10px;

        }}




        /* MUÑECO */

        .muñeco-ajustado img{{

            position:relative;

            z-index:999;

            display:block;

            opacity:.95;

        }}

        </style>
        """,

        unsafe_allow_html=True
    )


    st.markdown(
        '<div class="muñeco-ajustado">',
        unsafe_allow_html=True
    )


    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Paleta estilo "Premium/Aesthetic"
colors = ["rgba(30, 58, 138, 0.8)", "rgba(100, 116, 139, 0.8)", 
          "rgba(146, 64, 14, 0.8)", "rgba(180, 160, 140, 0.8)", "rgba(250, 235, 215, 0.8)"]

def style_chart(fig):
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Georgia, serif", size=12),
        margin=dict(l=10, r=10, t=30, b=10),
        xaxis=dict(showgrid=False), # Estilo minimalista
        yaxis=dict(showgrid=False)
    )
    return fig
# --- NUEVA FILA: DEMOGRAPHIC OVERVIEW ---
st.markdown("### *______________________________________________________________________________*")
col_a, col_b = st.columns(2)

with col_a:
    st.markdown("##### *Patients by Country*")
    # Usamos 'pais' según lo que comentaste
    pais_data = df_filt.groupby('pais').size().reset_index(name='count') 
    fig_country = px.bar(pais_data, x='count', y='pais', orientation='h', 
                         color_discrete_sequence=[colors[0]])
    st.plotly_chart(style_chart(fig_country), use_container_width=True)

with col_b:
    st.markdown("##### *Age Distribution*")
    # Usamos 'edad' (si tu columna tiene otro nombre, cámbialo aquí)
    fig_age = px.histogram(df_filt, x='edad', nbins=15, 
                           color_discrete_sequence=[colors[1]])
    st.plotly_chart(style_chart(fig_age), use_container_width=True)

st.markdown("---")

# --- FILA 1: PORTFOLIO + COST PROFILE ---
c1, c2 = st.columns(2)

with c1:
    st.markdown("### *Procedure Portfolio*")
    st.caption("Distribution of surgical procedures")
    proc_mix = df_filt.groupby("tipo_procedimiento").size().reset_index(name="count")
    fig1 = px.pie(proc_mix, names="tipo_procedimiento", values="count", hole=0.7, color_discrete_sequence=colors)
    st.plotly_chart(style_chart(fig1), use_container_width=True)

with c2:
    st.markdown("### *Cost Profile by Procedure*")
    st.caption("Average expenditure across procedures")
    df_cost = df_filt.groupby('tipo_procedimiento')['coste_usd'].mean().reset_index()
    fig2 = px.bar(df_cost, x='coste_usd', y='tipo_procedimiento', orientation='h', color_discrete_sequence=[colors[0]])
    st.plotly_chart(style_chart(fig2), use_container_width=True)

# --- FILA 2: RECOVERY TIMELINE + PERFORMANCE MATRIX ---
c3, c4 = st.columns(2)

with c3:
    st.markdown("### *Recovery Timeline by Procedure*")
    st.caption("Variability in post-operative recovery")
    fig3 = px.box(df_filt, x='tipo_procedimiento', y='dias_recuperacion', color_discrete_sequence=[colors[2]])
    st.plotly_chart(style_chart(fig3), use_container_width=True)

with c4:
    st.markdown("### *Procedure Performance Matrix*")
    st.caption("Balancing cost, recovery and patient satisfaction")
    fig5 = px.scatter(
        df_filt, x="coste_usd", y="indice_satisfaccion", 
        size="dias_recuperacion", color="tipo_procedimiento",
        size_max=15, color_discrete_sequence=colors
    )
    st.plotly_chart(style_chart(fig5), use_container_width=True)
    # ==========================================================
# KEY PROCEDURE INSIGHTS - AUTOMATED MOTOR
# ==========================================================

# 1. Definición de la función (Textos en inglés, sin emojis)
def get_smart_insights(df):
    stats = df.groupby('tipo_procedimiento').agg({
        'indice_satisfaccion': 'mean', 'dias_recuperacion': 'mean',
        'coste_usd': 'mean', 'nivel_dolor': 'mean',
        'complicacion_postoperatoria': lambda x: (x == 'Si').mean(),
        'reintervencion': lambda x: (x == 'Si').mean()
    })
    
    potential = [
        {"Category": "Experience", "Text": "Procedures with higher satisfaction tend to have shorter recovery times.", "score": abs(df['indice_satisfaccion'].corr(df['dias_recuperacion'])) if len(df) > 1 else 0},
        {"Category": "Efficiency", "Text": "Higher costs did not show proportional improvements in patient satisfaction.", "score": abs(df['coste_usd'].corr(df['indice_satisfaccion'])) if len(df) > 1 else 0},
        {"Category": "Recovery", "Text": f"Significant variance detected: {df['dias_recuperacion'].std():.1f} days standard deviation.", "score": df['dias_recuperacion'].std()},
        {"Category": "Clinical Burden", "Text": "Longer recovery periods correlate with higher complication rates.", "score": abs(df['dias_recuperacion'].corr(df['complicacion_postoperatoria'])) if len(df) > 1 else 0},
        {"Category": "Follow-up", "Text": "Procedures with higher reintervention rates require tighter post-op control.", "score": df['reintervencion'].mean()},
        {"Category": "Clinical Value", "Text": "Identified high-satisfaction procedures with optimal cost-recovery balance.", "score": (stats['indice_satisfaccion'] / stats['coste_usd']).std() if not stats.empty else 0}
    ]
    
    sorted_insights = sorted(potential, key=lambda x: x['score'], reverse=True)
    return sorted_insights[:4]

# 2. Renderizado ejecutivo
st.markdown("---")
st.markdown("### *Key Procedure Insights*")
st.caption("Insights generated automatically based on current selection")

# Inyección CSS
st.markdown("""
<style>
.insight-card { background-color: rgba(245, 245, 245, 0.5); border-radius: 15px; padding: 20px; margin-bottom: 15px; border: 1px solid rgba(200, 200, 200, 0.2); }
</style>
""", unsafe_allow_html=True)

insights = get_smart_insights(df_filt)

cols = st.columns(2)
for i, insight in enumerate(insights[:4]):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="insight-card">
            <h4 style="font-style: italic; color: #1e3a9a;">{insight['Category']}</h4>
            <p style="font-size: 14px; color: #334159;">{insight['Text']}</p>
        </div>
        """, unsafe_allow_html=True)