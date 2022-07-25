import streamlit as st


class PageTools(object):
    """
    This class is used to create a Streamlit app.
    """
    def __init__(self):
        pass

    def set_title(self, page_title: str):
        """
        This function is used to set the title of the page.
        :param page_title: The title of the page.
        """
        st.set_page_config(
            page_title=page_title
        )
    
    def load_markdown_file(self, file_path: str):
        """
        This function is used to load a markdown file.
        :param file_path: The path of the markdown file.
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            st.markdown(f.read())
