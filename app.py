import streamlit as st

st.title("전라남도교육지원청")
col1, col2 = st.columns(2)
with col1:
    st.image("https://preview.redd.it/jpiwcf6r1rx31.jpg?width=479&format=pjpg&auto=webp&s=c9973c18f74c40ea364144611ec76001c167708b")
with col2:
    st.link_button("티스토리", "https://celbeing.tistory.com/")
    st.link_button("백준", "https://www.acmicpc.net/user/kimsd1983")
    st.link_button("atCoder", "https://atcoder.jp/users/kimsd1983")