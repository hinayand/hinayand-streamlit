import streamlit as st


class InputTools(object):
    """
    This class is used to get user`s input.
    """

    def __init__(self):
        pass

    @staticmethod
    def input_text(label: str, value: str) -> str:
        """
        This function is used to input a text.
        param label: The label of the text.
        param value: The value of the text.
        """
        return st.text_input(label, value)

    @staticmethod
    def input_password(label: str, value: str) -> str:
        """
        This function is used to input a password.
        param label: The label of the password.
        param value: The value of the password.
        """
        return st.text_input(label, value, password=True)

    @staticmethod
    def input_number(label: str, value: int) -> int:
        """
        This function is used to input a number.
        param label: The label of the number.
        param value: The value of the number.
        """
        return st.number_input(label, value)

    @staticmethod
    def input_checkbox(label: str, value: bool) -> bool:
        """
        This function is used to input a checkbox.
        param label: The label of the checkbox.
        param value: The value of the checkbox.
        """
        return st.checkbox(label, value)

    @staticmethod
    def input_radio(label: str, value: str, options: list) -> str:
        """
        This function is used to input a radio.
        param label: The label of the radio.
        param value: The value of the radio.
        param options: The options of the radio.
        """
        return st.radio(label, options, value)

    @staticmethod
    def input_selectbox(label: str, value: str, options: list) -> str:
        """
        This function is used to input a selectbox.
        param label: The label of the selectbox.
        param value: The value of the selectbox.
        param options: The options of the selectbox.
        """
        return st.selectbox(label, options, value)

    @staticmethod
    def input_multiselect(label: str, value: list, options: list) -> list:
        """
        This function is used to input a multiselect.
        param label: The label of the multiselect.
        param value: The value of the multiselect.
        param options: The options
        """
        return st.multiselect(label, options, value)

    @staticmethod
    def input_text_area(label: str, value: str) -> str:
        """
        This function is used to input a text area.
        param label: The label of the text area.
        param value: The value of the text area.
        """
        return st.text_area(label, value)

    @staticmethod
    def button(label: str, click_callback: callable) -> None:
        """
        This function is used to input a button.
        param label: The label of the button.
        """
        st.button(label, on_click=click_callback)
