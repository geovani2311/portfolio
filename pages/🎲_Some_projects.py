import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Project about analyse about prices of gasoline in Brazil")
    st.text("Cleaning and preprocessing the data")
    st.link_button('https://github.com/geovani2311/Pandas_Exercises/blob/main/exercicios-pandas.ipynb','https://github.com/geovani2311/Pandas_Exercises/blob/main/exercicios-pandas.ipynb')
with col2:
    st.image('img/gasoline.jpg',width=250)

st.subheader(" ", divider='gray')

col1, col2 = st.columns(2)
with col1:
    st.subheader("Project about analyse about Obesity among adults by country, 1975-2016")
    st.text("Cleaning and preprocessing the data")
    st.link_button('https://github.com/geovani2311/Pandas_Exercises/blob/main/projeto-analise-de-dados.ipynb','https://github.com/geovani2311/Pandas_Exercises/blob/main/projeto-analise-de-dados.ipynb')
with col2:
    st.image('img/obesidity.jpg',width=250)

st.subheader(" ", divider='gray')

col1, col2 = st.columns(2)
with col1:
    st.subheader("Project about analyse about Obesity among adults by country, 1975-2016")
    st.text("Cleaning and preprocessing the data")
    st.link_button('https://github.com/geovani2311/Pandas_Exercises/blob/main/projeto-analise-de-dados.ipynb','https://github.com/geovani2311/Pandas_Exercises/blob/main/projeto-analise-de-dados.ipynb')
with col2:
    st.image('img/obesidity.jpg',width=250)
