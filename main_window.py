import sys

import pygame
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtMultimedia import QMediaPlayer

from all_three_circles import create_all_three_circles
from interests_circle import create_interests_circle
from needs_circle import create_needs_circle
from skills_circle import create_skills_circle


def cancel():
    QtWidgets.QApplication.quit()


def finish():
    QtWidgets.QApplication.quit()


def play_audio():
    # Replace 'speaker1.mp3' with the path to your audio file
    audio_file_path = "media/speaker.mp3"

    # Load and play the audio file using pygame
    pygame.mixer.music.load(audio_file_path)
    pygame.mixer.music.play()


class IntroductionWindow(QtWidgets.QWidget):
    def __init__(self, visualization_widget):
        super().__init__()

        self.visualization_widget = visualization_widget

        # Set up the layout for the introduction page
        layout = QtWidgets.QVBoxLayout(self)

        # Add the audio button
        audio_button = QtWidgets.QPushButton()
        audio_button.setIcon(QtGui.QIcon("media/speaker.png"))  # Replace with the actual path to your speaker icon
        audio_button.setIconSize(QtCore.QSize(40, 40))
        audio_button.setFixedSize(40, 40)
        audio_button.clicked.connect(play_audio)
        layout.addWidget(audio_button)

        # Add the image label
        image_layout = QtWidgets.QVBoxLayout()
        layout.addLayout(image_layout)

        image_label = QtWidgets.QLabel()
        image_label.setAlignment(QtCore.Qt.AlignCenter)
        image_layout.addWidget(image_label)

        # Load the GIF image using QMovie
        gif_path = "media/full-circle.gif"  # Replace with the actual path to your GIF file
        movie = QtGui.QMovie(gif_path)

        # Set the movie as the content of the label
        image_label.setMovie(movie)

        # Start playing the GIF
        movie.start()

        # Create a wrapper widget for the heading and description labels
        heading_description_wrapper = QtWidgets.QWidget()
        heading_description_layout = QtWidgets.QVBoxLayout(heading_description_wrapper)

        # Add the wrapper for the heading and description labels to the main layout
        layout.addWidget(heading_description_wrapper, alignment=QtCore.Qt.AlignCenter)

        # Add the heading label
        heading_label = QtWidgets.QLabel("Welcome to My Venn Diagram!")
        heading_label.setAlignment(QtCore.Qt.AlignCenter)
        heading_font = heading_label.font()
        heading_font.setPointSize(20)
        heading_font.setBold(True)
        heading_label.setFont(heading_font)
        heading_description_layout.addWidget(heading_label, alignment=QtCore.Qt.AlignCenter)

        # Add the description label
        description_label = QtWidgets.QLabel("Here I'm trying to visualize my career options "
                                             "with three circles that represent different sets "
                                             "and their intersections.")
        description_label.setAlignment(QtCore.Qt.AlignCenter)
        description_font = description_label.font()
        description_font.setPointSize(14)
        description_label.setFont(description_font)
        heading_description_layout.addWidget(description_label)

        heading_description_layout.setSpacing(25)

        # Add the start and cancel buttons
        button_layout = QtWidgets.QHBoxLayout()
        layout.addLayout(button_layout)

        start_button = QtWidgets.QPushButton("Start")
        start_button.setFixedSize(500, 40)  # Set the custom size (width, height)
        start_button.clicked.connect(self.start_visualization)
        button_layout.addWidget(start_button)

        cancel_button = QtWidgets.QPushButton("Cancel")
        cancel_button.setFixedSize(500, 40)  # Set the custom size (width, height)
        cancel_button.clicked.connect(cancel)
        button_layout.addWidget(cancel_button)

        # Set up the media player for audio playback
        self.media_player = QMediaPlayer()

        # Initialize pygame for audio playback
        pygame.mixer.init(buffer=1024)

    def start_visualization(self):
        self.hide()
        self.visualization_widget.show()


def create_visualization_1():
    # Create the first visualization using the imported function
    visualization_widget = create_all_three_circles()
    visualization_widget.setObjectName("All Three Circles")  # Set a unique object name
    return visualization_widget


def create_visualization_2():
    # Create the second visualization using the imported function
    visualization_widget = create_interests_circle()
    visualization_widget.setObjectName("Interests Circle")  # Set a unique object name
    return visualization_widget


def create_visualization_3():
    # Create the third visualization using the imported function
    visualization_widget = create_skills_circle()
    visualization_widget.setObjectName("Skills Circle")  # Set a unique object name
    return visualization_widget


def create_visualization_4():
    # Create the fourth visualization using the imported function
    visualization_widget = create_needs_circle()
    visualization_widget.setObjectName("Needs Circle")  # Set a unique object name
    return visualization_widget


class VisualizationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a stacked widget to hold the different visualizations
        self.stacked_widget = QtWidgets.QStackedWidget()

        # Create finish, back and next buttons
        self.finish_button = QtWidgets.QPushButton("Finish")
        self.finish_button.setFixedSize(100, 40)  # Set the custom size (width, height)
        self.finish_button.clicked.connect(finish)

        self.back_button = QtWidgets.QPushButton("Back")
        self.back_button.setFixedSize(100, 40)  # Set the custom size (width, height)
        self.back_button.clicked.connect(self.show_previous_page)
        self.back_button.setVisible(False)  # Hide the button initially

        self.next_button = QtWidgets.QPushButton("Next")
        self.next_button.setFixedSize(100, 40)  # Set the custom size (width, height)
        self.next_button.clicked.connect(self.show_next_page)

        # Create a status bar
        self.setStatusBar(QtWidgets.QStatusBar())

        # Add the back button on the left corner and next button on the right corner of the status bar
        self.statusBar().addPermanentWidget(self.back_button)
        self.statusBar().addPermanentWidget(self.next_button)
        self.statusBar().addPermanentWidget(self.finish_button)

        # Add the visualization pages to the stacked widget
        self.stacked_widget.addWidget(create_visualization_1())
        self.stacked_widget.addWidget(create_visualization_2())
        self.stacked_widget.addWidget(create_visualization_3())
        self.stacked_widget.addWidget(create_visualization_4())

        # Set the first page as the current page
        self.show_page(0)

    def show_page(self, index):
        # Switch to the selected page in the stacked widget
        self.setCentralWidget(self.stacked_widget)
        self.stacked_widget.setCurrentIndex(index)

        # Show/hide back and next buttons based on the current page
        self.update_navigation_buttons(index)

        # Show the name of the current visualization in the status bar
        visualization_widget = self.stacked_widget.widget(index)
        visualization_name = visualization_widget.objectName()
        self.statusBar().showMessage(visualization_name)

    def show_previous_page(self):
        current_index = self.stacked_widget.currentIndex()
        if current_index > 0:
            self.stacked_widget.setCurrentIndex(current_index - 1)
            self.update_navigation_buttons(current_index - 1)

            # Show the name change for the current visualization in the status bar
            visualization_widget = self.stacked_widget.widget(current_index - 1)
            visualization_name = visualization_widget.objectName()
            self.statusBar().showMessage(visualization_name)

    def show_next_page(self):
        current_index = self.stacked_widget.currentIndex()
        if current_index < self.stacked_widget.count() - 1:
            self.stacked_widget.setCurrentIndex(current_index + 1)
            self.update_navigation_buttons(current_index + 1)

            # Show the name change for the current visualization in the status bar
            visualization_widget = self.stacked_widget.widget(current_index + 1)
            visualization_name = visualization_widget.objectName()
            self.statusBar().showMessage(visualization_name)

    def update_navigation_buttons(self, index):
        # Show/hide back and next buttons based on the current index
        self.back_button.setVisible(index > 0)
        self.next_button.setVisible(index < self.stacked_widget.count() - 1)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    visualization_window = VisualizationWindow()
    introduction_window = IntroductionWindow(visualization_window)

    window_width = 1022
    window_height = 523

    introduction_window.setWindowTitle("Intro")
    visualization_window.setWindowTitle("My Venn Diagram")

    # Set custom resolutions and center the windows on the screen
    window_rect = QtWidgets.QStyle.alignedRect(
        QtCore.Qt.LeftToRight,
        QtCore.Qt.AlignCenter,
        QtCore.QSize(window_width, window_height),
        QtWidgets.QApplication.desktop().availableGeometry()
    )
    introduction_window.setGeometry(window_rect)
    visualization_window.setGeometry(window_rect)

    introduction_window.show()
    app.exec_()
