"""
This module is used to run python code.
"""
import streamlit as st
from tools.StreamlitTools.PageTools import PageTools
from tools.StreamlitTools.InputTools import InputTools

def run_python_code(code: str):
    """
    This function is used to run a python code.
    :param code: The code to run.
    """
    if 'os' in code or 'sys' in code:
        st.error("You can't use os or sys in your code.")
    else:
        code = compile(code, '<string>', 'exec')
        exec(code)        

PageTools().set_title('Python Runner')
PageTools().load_markdown_file('./markdown/python_runner.md')
code = InputTools().input_text('Input your Python code:')
InputTools().button('Run', run_python_code(code))
