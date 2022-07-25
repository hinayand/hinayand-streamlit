from tools.StreamlitTools.PageTools import PageTools
from tools.StreamlitTools.InputTools import InputTools
from tools.StreamlitTools.MediaTools import MediaTools
import streamlit as st
import os


class Shell(object):
    def __init__(self):
        command = InputTools().input_text_area('Command', '')
        InputTools().button('Execute', lambda: self.run_command(command))

    @staticmethod
    def run_command(command):
        if st.session_state['LoginStatus']:
            try:
                if command == 'logout':
                    st.session_state.clear()
                    st.success('Logout Success')
                else:
                    exec(command[1:])
            except Exception as e:
                st.error(e)
            except PermissionError as e:
                st.error(e)
            finally:
                pass
        else:
            st.error('Need to login')


PageTools().set_title('Admin Shell')
PageTools().load_markdown_file('./markdown/admin_shell.md')
