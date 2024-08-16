import sys
import re
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow
from pytube import YouTube

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Set up the UI

        # Connect button click to search function
        self.search_button.clicked.connect(self.search_youtube)

    def search_youtube(self):
        url = self.search_input.text()
        if not url:
            self.results_text.setText('Please enter a YouTube URL or search term.')
            return

        video_info = self.fetch_video_details(url)
        self.results_text.setText(video_info)

    def fetch_video_details(self, url):
        try:
            video_id = self.extract_video_id(url)
            if not video_id:
                return 'Invalid YouTube URL.'

            # Create a YouTube object
            yt = YouTube(f'https://www.youtube.com/watch?v={video_id}')

            # Fetch video title and URL
            video_title = yt.title
            video_url = yt.watch_url
            return f'Video Title: {video_title}\nVideo URL: {video_url}'

        except Exception as e:
            return f'Error: {str(e)}'

    def extract_video_id(self, url):
        video_id_regex = re.compile(r'(?:v=|\/)([0-9A-Za-z_-]{11})')
        match = video_id_regex.search(url)
        if match:
            return match.group(1)
        return None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
