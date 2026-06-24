import streamlit as st

st.set_page_config(
    page_title="About",
    layout="wide"
)

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html,body{
background:#F7F8FA;
}

*{
font-family:'Inter',sans-serif;
}

.block-container{
max-width:1500px;
padding-top:1rem;
padding-bottom:5rem;
}

.page{
padding:40px 80px 120px;
}


/* HERO */

.hero{
display:grid;
grid-template-columns:
minmax(700px,1.5fr)
minmax(320px,.7fr);
gap:90px;
align-items:start;
padding-top:60px;
padding-bottom:150px;
}

.left{
min-width:0;
}

.kicker{
font-size:12px;
letter-spacing:5px;
font-weight:600;
color:#90A0B2;
margin-bottom:40px;
}

.title{
font-size:clamp(72px,7vw,100px);
line-height:.88;
font-weight:700;
letter-spacing:-4px;
color:#111827;
max-width:850px;
}

.subtitle{
margin-top:40px;
font-size:24px;
line-height:1.8;
color:#6B7280;
max-width:620px;
}

.right{
display:flex;
align-items:flex-start;
justify-content:flex-start;
}

.abstract{
max-width:380px;
padding-left:40px;
border-left:1px solid #DCE2E8;
}

.abstract-title{
font-size:12px;
letter-spacing:4px;
color:#8A98A8;
margin-bottom:20px;
}

.abstract-text{
font-size:18px;
line-height:2;
color:#4B5563;
}


/* QUESTION */

.question{
padding:130px 0;
}

.question-title{
font-size:12px;
letter-spacing:5px;
color:#95A0AD;
margin-bottom:25px;
}

.question-text{
font-size:56px;
line-height:1.35;
font-weight:600;
max-width:1100px;
color:#111827;
}

.question-sub{
margin-top:35px;
font-size:22px;
line-height:1.9;
color:#667085;
max-width:850px;
}


/* SOLUTION */

.solution{
padding-top:60px;
padding-bottom:80px;
}

.solution-label{
font-size:12px;
letter-spacing:4px;
color:#8C99A8;
margin-bottom:30px;
}

.solution-text{
font-size:26px;
color:#475467;
}


/* PROCESS */

.grid{
display:grid;
grid-template-columns:1fr 1fr;
gap:100px;
margin-top:80px;
}

.card{
padding-top:30px;
border-top:1px solid #DCE2E8;
}

.number{
font-size:18px;
font-weight:600;
color:#98A3AF;
margin-bottom:18px;
}

.card-title{
font-size:40px;
line-height:1.2;
font-weight:700;
color:#111827;
margin-bottom:35px;
}

.card-body{
font-size:19px;
line-height:2.1;
color:#4B5563;
}

.card-body ul{
margin-top:25px;
line-height:2.2;
}


/* DISCLAIMER */

.note{
margin-top:130px;
padding:70px;
background:#EEF2F6;
border-left:6px solid #5A6B7D;
}

.note-title{
font-size:14px;
letter-spacing:4px;
color:#516273;
margin-bottom:30px;
}

.note-text{
font-size:20px;
line-height:2;
color:#344054;
}


/* RESULT */

.result{
margin-top:180px;
padding-top:70px;
border-top:1px solid #DCE2E8;
}

.result-title{
font-size:14px;
letter-spacing:5px;
color:#8A97A8;
margin-bottom:40px;
}

.result-text{
font-size:40px;
line-height:1.8;
max-width:1000px;
font-weight:500;
color:#111827;
}

.footer{
margin-top:100px;
font-size:12px;
letter-spacing:4px;
color:#98A3AF;
}


@media(max-width:1200px){

.hero{
grid-template-columns:1fr;
}

.grid{
grid-template-columns:1fr;
}

.title{
font-size:70px;
}

.question-text{
font-size:42px;
}

.result-text{
font-size:28px;
}

}

</style>
""", unsafe_allow_html=True)



st.markdown("""

<div class='page'>

<div class='hero'>

<div class='left'>

<div class='kicker'>
SURGICAL ANALYTICS
</div>

<div class='title'>
Surgical Outcomes &
Procedure Performance
</div>

<div class='subtitle'>

From descriptive statistics to predictive exploration through data analysis.

</div>

</div>

<div class='right'>

<div class='abstract'>

<div class='abstract-title'>
DATA SOURCE
</div>

<div class='abstract-text'>

This project was inspired by publicly available surgical procedure statistics reported by the American Society of Plastic Surgeons (ASPS), used as a foundation to build an analytical scenario focused on clinical, economic, and patient experience variables.

</div>

</div>

</div>

</div>




<div class='question'>

<div class='question-title'>
THE PROBLEM
</div>

<div class='question-text'>

What patterns emerge when integrating patient behavior, procedure preferences, and post-procedure outcomes?

</div>

<div class='question-sub'>

Healthcare decisions rarely depend on a single metric. This analysis explores how multiple outcome dimensions interact to identify procedures with more favorable overall profiles.

</div>

</div>




<div class='solution'>

<div class='solution-label'>
THE SOLUTION
</div>

<div class='solution-text'>

A two-stage analytical workflow was designed.

</div>

</div>

</div>

""", unsafe_allow_html=True)



c1,c2=st.columns(2)

with c1:

    st.markdown("""

<div class='card'>

<div class='number'>
01
</div>

<div class='card-title'>

Data Exploration &
Preparation

</div>

<div class='card-body'>

<ul>

<li>Data quality and consistency review</li>

<li>Missing value treatment</li>

<li>Standardization and feature renaming</li>

<li>Derived variable generation</li>

</ul>

Relationships between economic behavior, clinical outcomes, and patient experience were then explored through interactive visual analysis.

</div>

</div>

""", unsafe_allow_html=True)



with c2:

    st.markdown("""

<div class='card'>

<div class='number'>
02
</div>

<div class='card-title'>

Predictive Model

</div>

<div class='card-body'>

As an extension of the analysis, a Machine Learning model was developed to explore patterns and generate estimations.

<br><br>

<strong>Important:</strong>

This is an exploratory and educational model.

Predictions rely on a synthetic and simplified dataset and should not be used for real clinical decision-making.

</div>

</div>

""", unsafe_allow_html=True)



st.markdown("""

<div class='page'>

<div class='note'>

<div class='note-title'>
LIMITATIONS & FUTURE DEVELOPMENT
</div>

<div class='note-text'>

To improve predictive capability, future versions would require:

longitudinal clinical data · medical history · comorbidities · surgical technique · intraoperative variables · postoperative follow-up · population diversity · external validation

</div>

</div>




<div class='result'>

<div class='result-title'>
RESULT
</div>

<div class='result-text'>

The final outcome was an interactive dashboard designed to transform clinical data into visual decision-making, enabling procedure comparison and generating insights into cost, recovery, risk, and patient experience.

</div>

</div>




<div class='footer'>

EDUCATIONAL PROJECT · SYNTHETIC DATASET · EXPLORATORY ANALYTICS

</div>

</div>

""", unsafe_allow_html=True)