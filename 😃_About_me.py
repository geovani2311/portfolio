import pandas as pd 
import streamlit as st

#st.set_page_config(layout="wide")

st.header("What's up guys!, welcome to my portifolio", divider='rainbow')
st.header("")

col1, col2 = st.columns(2)

with col1:
    st.image('img/perfil_2.png',width=200)
with col2:
    st.subheader("Hi, my name is Geovani 😀")
    st.markdown("I'm a Business Intelligence analyst, and through this portfolio I want to try to tell you more about myself and what I'm doing")

st.header("")
st.subheader("📄 Sumary", divider='gray')
st.markdown("Beginning my journey in the data field in 2019, I have gained experience in various companies. Among them is Unilever, a multinational consumer goods company, where I took my first steps in Business Intelligence as a young apprentice and intern, exploring and manipulating data. Subsequently, I joined the DPSP team, one of the largest pharmaceutical retail networks, and currently, I am engaged with Vidalink, a wellness company, where I continue to expand my knowledge and skills. My journey in this field has been marked by continuous improvement, driven by my passion for the data universe")
st.header("")


st.subheader("👔 Work Experience", divider='gray')


#job 1
st.write("")
st.write("**Intermediate Data Analyst | Vidalink**")
st.text("Jan/2024 to present")
st.write(
    """
    - Responsible for the development and maintenance of reports, indicators, and goals across various Vidalink areas
    - Modeling metrics and designing KPIs
    - Managing PostgreSQL database and creating query codes, views, procedures, and functions. Extracting and manipulating data for analysis/studies/audits using tools such as Excel,Metabase, PowerBI, Python
    - Presenting results and insights to different business areas
    """ 
    )

#job 2
st.write("")
st.write("**Junior Data Analyst | Grupo DPSP**")
st.text("Sep/22 to Jan/23")
st.write(
    """
    - Development and creation of dashboards for campaign and industry monitoring
    - Ad hoc extractions and analyses using SQL and Python
    - Creation of KPIs - analytical report for loss prevention
    - Automation of reports and other tasks using Python, Knime, and Power Automate
    """ 
    )

#job 3
st.write("")
st.write("**Intern | Unilever**")
st.text("Feb/2021 to Jun/2022")
st.write(
    """
    - Analysis of stock health of customers to avoid stockouts and overstock
    - Innovation analysis (incrementality, performance, turnover, and results)
    - Development of Power BI dashboards for Sell Out monitoring
    - ETL - Alteryx / R / Python for automation and consolidation of e-commerce data
    """ 
    )

#job 4
st.write("")
st.write("**Apprentice | Unilever**")
st.text("Jul/2019 to Jan/2021")
st.write(
    """
    - Responsible for receiving and sending e-commerce Sell Out data
    - Organization and validation of data for the team's use in decision-making, strategy, and results monitoring (Sell Out)
    - Criaça o de KPI's - relato rio analí tico para prevença o de perdas
    - Development of Market Share by category and client
    """ 
    )


st.subheader("Skills 🐱‍👤", divider='gray')
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.image("img/python.jpg") 
with col2:
    st.image("img/sql.jpg")    
with col3:
    st.image("img/excel.jpg")
with col4:
    st.image("img/pbi.jpg")
with col5:
    st.image("img/alteryx-inc.jpg")
st.subheader("")
st.text("Others that I worked too a little bit")
col1, col2, col3 = st.columns(3)
with col1:
    st.image("img/knime.jpg",width=145) 
with col2:
    st.image("img/tableau.jpg",width=145)    
with col3:
    st.image("img/qlik.jpg",width=145)
st.subheader("")
