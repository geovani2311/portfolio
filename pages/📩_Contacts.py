import streamlit as st

st.header("Contacts 📩", divider='rainbow')
st.header("")
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.link_button("Linkedin", "https://www.linkedin.com/in/geovani-lima-cardoso-760212158/")
with col2:
    st.link_button("GitHub", "https://github.com/geovani2311")
with col3:
    st.link_button("Medium", "https://medium.com/@geovani.cardoso1")
with col4:
    st.link_button("Youtube", "https://www.youtube.com/channel/UCe5tUK2qlAHSzJaovHX1Rww")



