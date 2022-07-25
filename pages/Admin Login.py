from tools.StreamlitTools.PageTools import PageTools
from tools.StreamlitTools.InputTools import InputTools
from tools.PyTools.UserManageTools import UserManager
import streamlit as st


def login(login_username: str, login_password: str):
    if umt_object.check_user(login_username, login_password):
        st.success('Login Success')
        st.session_state.clear()
        st.session_state['LoginStatus'] = True
    else:
        if umt_object.users == {}:
            umt_object.add_user(login_username, login_password)
            umt_object.save_users()
            st.success('Login Success')
        else:
            st.error('Login Failed')


umt_object = UserManager(path='./users.json')
umt_object.load_users()

st.session_state['LoginStatus'] = False

PageTools().set_title('Admin Login')
PageTools().load_markdown_file('./markdown/admin_login.md')

username = InputTools().input_text('Username', '')
password = InputTools().input_password('Password', '')
InputTools().button('Login', lambda: login(username, password))
