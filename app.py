import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title

# 定义页面结构
show_pages(
    [
        Page("app.py", "主页", "🏠"),
        Section("用户管理", icon="👥"),
            Page("pages/user_profile.py", "用户资料"),
            Page("pages/admin.py", "管理员面板", in_section=False),  # 隐藏但保留路由
    ]
)

# 自动添加当前页面标题
add_page_title()

# 动态隐藏页面
if not st.session_state.get("is_admin"):
    hide_pages(["pages/admin.py"])

st.write("这里是主页内容...")
