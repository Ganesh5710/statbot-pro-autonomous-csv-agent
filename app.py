# =========================================================
# STATBOT PRO X - NEXT GEN ULTRA PREMIUM AI DASHBOARD
# CINEMATIC ENTERPRISE EDITION
# =========================================================

from core.insight_engine import generate_insights
from core.outlier_detection import detect_outliers_for_column
from core.kpi_calculator import calculate_kpis
from dashboard.filters import apply_filters

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
from datetime import datetime
import numpy as np

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="StatBot Pro ",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# ULTRA PREMIUM CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

html, body, [class*="css"]{
    font-family: 'Inter', sans-serif;
}

/* =========================================================
BACKGROUND
========================================================= */

.stApp{

    background:
    radial-gradient(circle at top left, rgba(37,99,235,0.28), transparent 24%),
    radial-gradient(circle at top right, rgba(168,85,247,0.24), transparent 24%),
    radial-gradient(circle at bottom left, rgba(14,165,233,0.18), transparent 22%),
    linear-gradient(
    135deg,
    #020617 0%,
    #081120 40%,
    #0f172a 70%,
    #111827 100%
    );

    color:white;
}

/* =========================================================
REMOVE STREAMLIT
========================================================= */

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

header{
    background:transparent !important;
}

/* =========================================================
SIDEBAR
========================================================= */

section[data-testid="stSidebar"]{

    min-width:330px !important;
    max-width:330px !important;

    background:
    linear-gradient(
    180deg,
    rgba(7,12,25,0.98),
    rgba(4,8,18,0.98)
    );

    border-right:1px solid rgba(255,255,255,0.08);

    backdrop-filter:blur(30px);
}

/* HIDE SIDEBAR COLLAPSE */

button[kind="header"]{
    display:none !important;
}

/* =========================================================
HERO
========================================================= */

.hero{

    position:relative;

    overflow:hidden;

    padding:60px;

    border-radius:38px;

    background:
    linear-gradient(
    135deg,
    rgba(37,99,235,0.32),
    rgba(124,58,237,0.22)
    );

    border:1px solid rgba(255,255,255,0.08);

    box-shadow:
    0 25px 80px rgba(0,0,0,0.45);

    margin-bottom:35px;
}

.hero::before{

    content:"";

    position:absolute;

    width:400px;
    height:400px;

    background:rgba(255,255,255,0.08);

    border-radius:50%;

    top:-160px;
    right:-120px;

    filter:blur(120px);
}

.hero-title{

    font-size:80px;

    font-weight:900;

    color:white;

    letter-spacing:-3px;
}

.hero-sub{

    color:#cbd5e1;

    font-size:24px;

    margin-top:14px;

    max-width:850px;

    line-height:1.6;
}

/* =========================================================
GLASS CARDS
========================================================= */

.glass{

    background:
    linear-gradient(
    135deg,
    rgba(255,255,255,0.07),
    rgba(255,255,255,0.03)
    );

    border-radius:30px;

    padding:30px;

    border:1px solid rgba(255,255,255,0.08);

    backdrop-filter:blur(30px);

    box-shadow:
    0 15px 50px rgba(0,0,0,0.35);

    margin-bottom:28px;

    transition:0.35s ease;
}

.glass:hover{

    transform:translateY(-5px);

    box-shadow:
    0 18px 55px rgba(59,130,246,0.16);
}

/* =========================================================
KPI CARDS
========================================================= */

.kpi-card{

    background:
    linear-gradient(
    135deg,
    rgba(255,255,255,0.08),
    rgba(255,255,255,0.03)
    );

    border-radius:26px;

    padding:26px;

    border:1px solid rgba(255,255,255,0.08);

    box-shadow:
    0 10px 40px rgba(0,0,0,0.35);
}

.kpi-title{

    color:#94a3b8;

    font-size:15px;

    font-weight:600;

    text-transform:uppercase;

    letter-spacing:1px;
}

.kpi-value{

    color:white;

    font-size:42px;

    font-weight:900;

    margin-top:12px;
}

/* =========================================================
SECTION TITLES
========================================================= */

.section-title{

    color:white;

    font-size:32px;

    font-weight:800;

    margin-bottom:20px;
}

/* =========================================================
UPLOAD
========================================================= */

[data-testid="stFileUploader"]{

    background:
    rgba(255,255,255,0.05);

    border-radius:20px;

    padding:14px;

    border:1px solid rgba(255,255,255,0.08);
}

/* =========================================================
BUTTONS
========================================================= */

.stButton > button{

    width:100%;

    border:none;

    padding:16px;

    border-radius:18px;

    background:
    linear-gradient(
    90deg,
    #2563eb,
    #7c3aed
    );

    color:white;

    font-weight:700;

    font-size:16px;

    transition:0.3s ease;
}

.stButton > button:hover{

    transform:translateY(-3px);
}

/* =========================================================
DATAFRAME
========================================================= */

[data-testid="stDataFrame"]{

    border-radius:22px;

    overflow:hidden;

    border:1px solid rgba(255,255,255,0.08);
}

/* =========================================================
OPTION MENU
========================================================= */

.nav-link-selected{
    background:linear-gradient(90deg,#2563eb,#7c3aed)!important;
}

/* =========================================================
SCROLLBAR
========================================================= */

::-webkit-scrollbar{
    width:10px;
}

::-webkit-scrollbar-thumb{
    background:#3b82f6;
    border-radius:20px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:
    selected = option_menu(
        menu_title=None,

        options=[
            "Overview",
            "Analytics",
            "Outliers",
            "Visualization",
            "AI Assistant"
        ],

        icons=[
            "house-fill",
            "bar-chart-fill",
            "activity",
            "pie-chart-fill",
            "robot"
        ],

        default_index=0,

        styles={

            "container": {
                "padding": "0!important",
                "background-color": "transparent",
            },

            "icon": {
                "color": "white",
                "font-size": "18px"
            },

            "nav-link": {

                "font-size": "17px",

                "font-weight": "600",

                "text-align": "left",

                "margin": "10px 0",

                "padding": "14px",

                "border-radius": "16px",

                "background-color": "rgba(255,255,255,0.05)",

                "--hover-color": "rgba(255,255,255,0.08)",
            },

            "nav-link-selected": {

                "background": "linear-gradient(90deg,#2563eb,#7c3aed)",

                "color": "white",

                "font-weight": "700",
            },
        }
    )

    st.markdown("---")

    uploaded_file = st.file_uploader(
        "📂 Upload CSV Dataset",
        type=["csv"]
    )

# =========================================================
# HERO
# =========================================================

st.markdown(f"""
<div class="hero">

<div class="hero-title">
StatBot Pro 
</div>

<div class="hero-sub">
 Enterprise AI Analytics Platform

<br>

<div style="color:#94a3b8;font-size:16px;">
{datetime.now().strftime("%A • %d %B %Y")}
</div>

</div>
""", unsafe_allow_html=True)

# =========================================================
# MAIN
# =========================================================

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    df = apply_filters(df)

    # =====================================================
    # OVERVIEW
    # =====================================================

    if selected == "Overview":

        kpis = calculate_kpis(df)

        c1,c2,c3,c4 = st.columns(4)

        with c1:
            st.markdown(f"""
            <div class="kpi-card">
            <div class="kpi-title">Total Rows</div>
            <div class="kpi-value">{kpis["Total Rows"]}</div>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown(f"""
            <div class="kpi-card">
            <div class="kpi-title">Total Columns</div>
            <div class="kpi-value">{kpis["Total Columns"]}</div>
            </div>
            """, unsafe_allow_html=True)

        with c3:
            st.markdown(f"""
            <div class="kpi-card">
            <div class="kpi-title">Numeric Columns</div>
            <div class="kpi-value">{kpis["Numeric Columns"]}</div>
            </div>
            """, unsafe_allow_html=True)

        with c4:
            st.markdown(f"""
            <div class="kpi-card">
            <div class="kpi-title">Top Column</div>
            <div class="kpi-value" style="font-size:22px;">
            {kpis["Highest Avg Column"]}
            </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        left,right = st.columns([1.8,1])

        with left:

            st.markdown("""
            <div class="glass">
            <div class="section-title">
            📈 Revenue Analytics
            </div>
            """, unsafe_allow_html=True)

            numeric_cols = df.select_dtypes(include="number").columns

            if len(numeric_cols) > 0:

                fig = px.area(
                    df,
                    y=numeric_cols[0],
                    template="plotly_dark"
                )

                fig.update_traces(
                    line=dict(width=4)
                )

                fig.update_layout(
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    height=480,
                    font=dict(color='white')
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            st.markdown("</div>", unsafe_allow_html=True)

        with right:

            st.markdown("""
            <div class="glass">
            <div class="section-title">
            🧠 AI Insights
            </div>
            """, unsafe_allow_html=True)

            insights = generate_insights(df)

            for insight in insights[:6]:
                st.success(insight)

            st.markdown("</div>", unsafe_allow_html=True)

        b1,b2 = st.columns([1.5,1])

        with b1:

            st.markdown("""
            <div class="glass">
            <div class="section-title">
            📄 Dataset Preview
            </div>
            """, unsafe_allow_html=True)

            st.dataframe(
                df.head(20),
                use_container_width=True
            )

            st.markdown("</div>", unsafe_allow_html=True)

        with b2:

            st.markdown("""
            <div class="glass">
            <div class="section-title">
            ⚡ Dataset Health
            </div>
            """, unsafe_allow_html=True)

            missing = df.isnull().sum().sum()

            health = max(0, 100 - (missing * 2))

            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=health,
                title={'text': "Health Score"},
                gauge={
                    'axis': {'range': [None, 100]},
                    'bar': {'color': "#3b82f6"},
                }
            ))

            fig.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white'),
                height=350
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            st.markdown("</div>", unsafe_allow_html=True)

    # =====================================================
    # ANALYTICS
    # =====================================================

    elif selected == "Analytics":

        st.markdown("""
        <div class="glass">
        <div class="section-title">
        📊 Correlation Intelligence
        </div>
        """, unsafe_allow_html=True)

        numeric_cols = df.select_dtypes(include="number").columns.tolist()

        corr = df[numeric_cols].corr()

        fig = px.imshow(
            corr,
            text_auto=True,
            color_continuous_scale="RdBu",
            template="plotly_dark"
        )

        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            height=720
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.markdown("</div>", unsafe_allow_html=True)

    # =====================================================
    # OUTLIERS
    # =====================================================

    elif selected == "Outliers":

        st.markdown("""
        <div class="glass">
        <div class="section-title">
        🚨 Outlier Detection Engine
        </div>
        """, unsafe_allow_html=True)

        numeric_cols = df.select_dtypes(include="number").columns.tolist()

        col = st.selectbox(
            "Select Column",
            numeric_cols
        )

        outliers = detect_outliers_for_column(df, col)

        st.metric(
            "Detected Outliers",
            len(outliers)
        )

        fig = px.box(
            df,
            y=col,
            template="plotly_dark"
        )

        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            height=520
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.dataframe(
            outliers,
            use_container_width=True
        )

        st.markdown("</div>", unsafe_allow_html=True)

    # =====================================================
    # VISUALIZATION
    # =====================================================

    elif selected == "Visualization":

        st.markdown("""
        <div class="glass">
        <div class="section-title">
        📈 Visualization Studio
        </div>
        """, unsafe_allow_html=True)

        col = st.selectbox(
            "Select Column",
            df.columns
        )

        chart = st.selectbox(
            "Chart Type",
            ["Histogram","Bar","Pie","Line","Scatter"]
        )

        if st.button("Generate Visualization"):

            if chart == "Histogram":

                fig = px.histogram(
                    df,
                    x=col,
                    template="plotly_dark"
                )

            elif chart == "Bar":

                fig = px.bar(
                    df[col].value_counts(),
                    template="plotly_dark"
                )

            elif chart == "Pie":

                fig = px.pie(
                    names=df[col].value_counts().index,
                    values=df[col].value_counts().values
                )

            elif chart == "Scatter":

                numeric_cols = df.select_dtypes(include="number").columns

                fig = px.scatter(
                    df,
                    x=numeric_cols[0],
                    y=numeric_cols[1],
                    template="plotly_dark"
                )

            else:

                fig = px.line(
                    df,
                    y=col,
                    template="plotly_dark"
                )

            fig.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                height=680
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        st.markdown("</div>", unsafe_allow_html=True)

    # =====================================================
    # AI ASSISTANT
    # =====================================================

    elif selected == "AI Assistant":

        st.markdown("""
        <div class="glass">
        <div class="section-title">
        🤖 AI Assistant
        </div>
        """, unsafe_allow_html=True)

        query = st.chat_input(
            "Ask AI about your dataset..."
        )

        if query:

            st.chat_message("user").write(query)

            numeric_cols = df.select_dtypes(include='number').columns

            response = ""

            if "average" in query.lower():

                for col in numeric_cols:
                    response += f"Average of {col}: {df[col].mean()} \n"

            elif "max" in query.lower():

                for col in numeric_cols:
                    response += f"Maximum of {col}: {df[col].max()} \n"

            elif "min" in query.lower():

                for col in numeric_cols:
                    response += f"Minimum of {col}: {df[col].min()} \n"

            else:

                response = "⚡ AI could not understand your query."

            st.chat_message("assistant").write(response)

        st.markdown("</div>", unsafe_allow_html=True)

# Responsive chart layout padding updated

import streamlit as st

st.set_page_config(page_title='StatBot Pro', layout='wide')

# File upload handler

# Executive KPI cards
