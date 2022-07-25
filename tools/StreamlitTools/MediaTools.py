import streamlit as st


class TextTools(object):
    """
    This class is used to show text.
    """
    def __init__(self):
        pass

    def show_text(self, text: str):
        """
        This function is used to show a text.
        :param text: The text to show.
        """
        st.write(text)

    def show_html(self, html: str):
        """
        This function is used to show an html.
        :param html: The html to show.
        """
        st.markdown(html)

    def show_md(self, md: str):
        """
        This function is used to show a markdown.
        :param md: The markdown to show.
        """
        st.markdown(md)

    def show_json(self, json_data: dict):
        """
        This function is used to show a json.
        :param json_data: The json to show.
        """
        st.json(json_data)

    def show_table(self, data: list, columns: list):
        """
        This function is used to show a table.
        :param data: The data to show.
        :param columns: The columns to show.
        """
        st.table(data, columns)

    def show_chart(self, data: list):
        """
        This function is used to show a chart.
        :param data: The data to show.
        :param chart_type: The chart type to show.
        """
        st.bar_chart(data)

    def show_map(self, data: list):
        """
        This function is used to show a map.
        :param data: The data to show.
        """
        st.map(data)

    def show_video(self, video_url: str):
        """
        This function is used to show a video.
        :param video_url: The video url to show.
        """
        st.video(video_url)

    def show_audio(self, audio_url: str):
        """
        This function is used to show an audio.
        :param audio
        """
        st.audio(audio_url)
    
    def show_image(self, image_url: str):
        """
        This function is used to show an image.
        :param image_url: The image url to show.
        """
        st.image(image_url)
