from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextEdit

class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle('YouTube Viewer')
        MainWindow.setGeometry(100, 100, 600, 400)

        # Create a central widget and set layout
        self.central_widget = QWidget()
        self.layout = QVBoxLayout()

        # Create widgets
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText('Enter YouTube URL or Search Term')
        self.search_button = QPushButton('Search')
        self.results_text = QTextEdit()
        self.results_text.setReadOnly(True)

        # Add widgets to layout
        self.layout.addWidget(self.search_input)
        self.layout.addWidget(self.search_button)
        self.layout.addWidget(self.results_text)

        # Set layout to central widget
        self.central_widget.setLayout(self.layout)
        MainWindow.setCentralWidget(self.central_widget)
