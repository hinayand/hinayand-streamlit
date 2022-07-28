import streamlit as st
import requests


class MediaTools(object):
    """
    This class is used to show text.
    """
    def __init__(self):
        pass

    @staticmethod
    def show_text(text: str):
        """
        This function is used to show a text.
        param text: The text to show.
        """
        st.write(text)

    @staticmethod
    def show_html(html: str):
        """
        This function is used to show a html.
        param html: The html to show.
        """
        st.markdown(html)

    @staticmethod
    def show_md(md: str):
        """
        This function is used to show a markdown.
        param md: The markdown to show.
        """
        st.markdown(md)

    @staticmethod
    def show_json(json_data: dict):
        """
        This function is used to show a json.
        param json_data: The json to show.
        """
        st.json(json_data)

    @staticmethod
    def show_table(data: list, columns: list):
        """
        This function is used to show a table.
        param data: The data to show.
        param columns: The columns to show.
        """
        st.table(data, columns)

    @staticmethod
    def show_chart(data: list):
        """
        This function is used to show a chart.
        param data: The data to show.
        """
        st.bar_chart(data)

    @staticmethod
    def show_map(data: list):
        """
        This function is used to show a map.
        param data: The data to show.
        """
        st.map(data)

    @staticmethod
    def show_video(video_url: str):
        """
        This function is used to show a video.
        param video_url: The video url to show.
        """
        st.video(video_url)

    @staticmethod
    def show_audio(audio_url: str):
        """
        This function is used to show an audio.
        param audio
        """
        st.audio(audio_url)
    
    @staticmethod
    def show_image(image_url: str):
        """
        This function is used to show an image.
        param image_url: The image url to show.
        """
        st.image(image_url)
