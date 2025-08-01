import streamlit as st

st.title("我的第一个 Streamlit 应用")
st.write("欢迎来到我的网站！")

name = st.text_input("你的名字")
if name:
    st.write(f"你好, {name}!")

'---'
