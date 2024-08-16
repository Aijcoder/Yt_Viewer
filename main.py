import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextEdit
from PyQt6.QtCore import Qt
from pytube import YouTube

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('YouTube Viewer')
        self.setGeometry(100, 100, 600, 400)

        # Set up the central widget and layout
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Create widgets
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText('Enter YouTube URL or Search Term')
        self.search_button = QPushButton('Search')
        self.results_text = QTextEdit()
        self.results_text.setReadOnly(True)

        # Add widgets to layout
        layout.addWidget(self.search_input)
        layout.addWidget(self.search_button)
        layout.addWidget(self.results_text)

        # Set layout to central widget
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Connect button click to search function
        self.search_button.clicked.connect(self.search_youtube)

    def search_youtube(self):
        search_term = self.search_input.text()
        if not search_term:
            self.results_text.setText('Please enter a search term or URL.')
            return

        try:
            # Create a YouTube object
            yt = YouTube(search_term)

            # Fetch video title
            video_title = yt.title
            video_url = yt.watch_url

            # Update results text area
            self.results_text.setText(f'Video Title: {video_title}\nVideo URL: {video_url}')
        except Exception as e:
            self.results_text.setText(f'Error: {str(e)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
