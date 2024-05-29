import streamlit as st

#st.set_page_config(layout="wide")
st.header("Projects 🎲", divider='rainbow')
st.header("")


col1, col2 = st.columns(2)
with col1:
    st.subheader("Prices of gasoline in Brazil")
    st.write("""
            - Project about analyse about prices of gasoline in Brazil, cleaning and preprocessing the data | Pandas 
            """)
    st.link_button('link of project','https://github.com/geovani2311/Pandas_Exercises/blob/main/exercicios-pandas.ipynb')
with col2:
    st.image('img/gasoline.jpg',width=250)
st.subheader(" ", divider='gray')
#-------------------//-----------------//------------------
col1, col2 = st.columns(2)
with col1:
    st.subheader("Is this a Pokemon dashboard in Excel?")
    st.write("""
            - Project about development dashboard | Excel)
             """)
    st.link_button('link of project','https://www.youtube.com/watch?v=cZsKflYIvdM')
with col2:
    st.image('img/pokemon_excel.jpg',width=250)
st.subheader(" ", divider='gray')
#-------------------//-----------------//------------------
col1, col2 = st.columns(2)
with col1:
    st.subheader("Obesity among adults by country, 1975-2016")
    st.write("""
            - Project about analyse about Obesity among adults by country, 1975-2016 | Pandas, matplotlib, plotly)
             """)
    st.link_button('link of project','https://github.com/geovani2311/Pandas_Exercises/blob/main/projeto-analise-de-dados.ipynb')
with col2:
    st.image('img/obesidity.jpg',width=250)
st.subheader(" ", divider='gray')
#-------------------//-----------------//------------------
col1, col2 = st.columns(2)
with col1:
    st.subheader("League of legends dashboard in Power Bi")
    st.write("""
            - Project about development dashboard | Power Bi
             """)
    st.link_button('link of project','https://www.linkedin.com/feed/update/urn:li:activity:6963588489695125504/')
with col2:
    st.image('img/lol_pbi.jpg',width=250)
st.subheader(" ", divider='gray')
#-------------------//-----------------//------------------
col1, col2 = st.columns(2)
with col1:
    st.subheader("Pilot Dog")
    st.write("""
            - Project about a game that I've created | Unity engine, C#
             """)
    st.link_button('link of project','https://geovani-lima.itch.io/pilot-dog')
with col2:
    st.image('img/game.jpg',width=250)
