import streamlit as st
st.write("https://celbeing.tistory.com/")
col1, col2 = st.columns([2,1])
with col1:
    st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExbzQ5OTY3dnMwZWdhNTNtOG5yeHRzMW4wZHB2N3lwNjdma2F5Mnh2eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/vPuszmHgeWnIhTkSr5/giphy.webp")
with col2:
    st.success("링크",icon = "👍")
    st.link_button("티스토리","https://celbeing.tistory.com/",)
    st.link_button("백준","https://www.acmicpc.net/user/kimsd1983")
    st.link_button("atCoder","https://atcoder.jp/users/kimsd1983")
name = st.text_input("누구세요?")

if len(name) > 0:
    if name in ["Jerry", "jerry", "JERRY", "제리"]:
        with col2:
            st.link_button("블로그","https://blog.naver.com/cel_being")

tab1, tab2, tab3, tab4 = st.tabs(["Spring", "Summer", "Autumn", "Winter"])
with tab1: st.write("봄")
with tab2: st.write("여름")
with tab3: st.write("가을")
with tab4: st.write("겨울")