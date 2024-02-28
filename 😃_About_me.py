import pandas as pd 
import streamlit as st

#st.set_page_config(layout="wide")
#😃_About_me.py

st.header("What's up guys!, welcome to my portifolio", divider='rainbow')
st.header("")

col1, col2 = st.columns(2)

with col1:
    st.image('img/perfil_2.png',width=200)
with col2:
    st.subheader("Hi, my name is Geovani 😀")
    st.markdown("I'm a Business Intelligence analyst, and through this portfolio I want to try to tell you more about myself and what I'm doing")

st.subheader("")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.link_button("Linkedin", "https://www.linkedin.com/in/geovani-lima-cardoso-760212158/")
with col2:
    st.link_button("GitHub", "https://github.com/geovani2311")
with col3:
    st.link_button("Medium", "https://medium.com/@geovani.cardoso1")
with col4:
    st.link_button("Youtube", "https://www.youtube.com/channel/UCe5tUK2qlAHSzJaovHX1Rww")


st.header("")
st.subheader("📄 Sumary", divider='gray')
st.markdown("Beginning my journey in the data field in 2019, I have gained experience in various companies. Among them is Unilever, a multinational consumer goods company, where I took my first steps in Business Intelligence as a young apprentice and intern, exploring and manipulating data. Subsequently, I joined the DPSP team, one of the largest pharmaceutical retail networks, and currently, I am engaged with Vidalink, a wellness company, where I continue to expand my knowledge and skills. My journey in this field has been marked by continuous improvement, driven by my passion for the data universe")
st.header("")


st.subheader("👔 Work Experience", divider='gray')


#job 1
st.write("")
st.write("**Data analyst junior | Grupo DPSP**")
st.text("Sep/22 to Jan/23")
st.write(
    """
    - Desenvolvimento e criaçao de dashboard para acompanhamento das campanhas, 
    industrias
    - Extraço es e analises ad hoc utilizando SQL e Python
    - Criaça o de KPI's - relato rio analí tico para prevença o de perdas
    - Automatizaça o de report's e demais tarefas utilizando Python, Knime e 
    power automate
    """ 
    )

#job 2
st.write("")
st.write("**Data analyst junior | Grupo DPSP**")
st.text("Sep/22 to Jan/23")
st.write(
    """
    - Desenvolvimento e criaçao de dashboard para acompanhamento das campanhas, 
    industrias
    - Extraço es e analises ad hoc utilizando SQL e Python
    - Criaça o de KPI's - relato rio analí tico para prevença o de perdas
    - Automatizaça o de report's e demais tarefas utilizando Python, Knime e 
    power automate
    """ 
    )
#job 3
st.write("")
st.write("**Data analyst junior | Grupo DPSP**")
st.text("Sep/22 to Jan/23")
st.write(
    """
    - Desenvolvimento e criaçao de dashboard para acompanhamento das campanhas, 
    industrias
    - Extraço es e analises ad hoc utilizando SQL e Python
    - Criaça o de KPI's - relato rio analí tico para prevença o de perdas
    - Automatizaça o de report's e demais tarefas utilizando Python, Knime e 
    power automate
    """ 
    )




st.subheader("Skills 🐱‍👤", divider='gray')
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.image("img/python.gif") 
with col2:
    st.image("img/sql.gif")    
with col3:
    st.image("img/excel.gif")
with col4:
    st.image("img/pbi.gif")
with col5:
    st.image("img/alteryx-inc.png")
st.subheader("")
st.text("Others that I worked too a little bit")
col1, col2, col3 = st.columns(3)
with col1:
    st.image("img/knime.jpg",width=145) 
with col2:
    st.image("img/tableau.png",width=145)    
with col3:
    st.image("img/qlik.png",width=145)
st.subheader("")
