import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QMovie
from all_three_circles import create_all_three_circles
from interests_circle import create_interests_circle
from skills_circle import create_skills_circle
from needs_circle import create_needs_circle


def cancel():
    QtWidgets.QApplication.quit()


class IntroductionWindow(QtWidgets.QWidget):
    def __init__(self, visualization_widget):
        super().__init__()

        self.visualization_widget = visualization_widget

        # Set up the layout for the introduction page
        layout = QtWidgets.QVBoxLayout(self)

        # Add the heading label
        heading_label = QtWidgets.QLabel("Welcome to My Venn Diagram!")
        heading_label.setAlignment(QtCore.Qt.AlignCenter)
        heading_font = heading_label.font()
        heading_font.setPointSize(20)
        heading_font.setBold(True)
        heading_label.setFont(heading_font)
        layout.addWidget(heading_label)

        # Add the image label
        image_label = QtWidgets.QLabel()
        image_label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(image_label)

        # Load the GIF image using QMovie
        gif_path = "full-circle.gif"  # Replace with the actual path to your GIF file
        movie = QMovie(gif_path)

        # Set the movie as the content of the label
        image_label.setMovie(movie)

        # Start playing the GIF
        movie.start()

        # Add the description label
        description_label = QtWidgets.QLabel("Here I'm trying to visualize my career options "
                                             "with three circles that represent different sets "
                                             "and their intersections.")
        description_label.setAlignment(QtCore.Qt.AlignCenter)
        description_font = description_label.font()
        description_font.setPointSize(14)
        description_label.setFont(description_font)
        layout.addWidget(description_label)

        # Add the buttons
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

    def start_visualization(self):
        self.hide()
        self.visualization_widget.show()


def create_visualization_1():
    # Create the first visualization using the imported function
    visualization_widget = create_all_three_circles()
    return visualization_widget


def create_visualization_2():
    # Create the second visualization using the imported function
    visualization_widget = create_interests_circle()
    return visualization_widget


def create_visualization_3():
    # Create the third visualization using the imported function
    visualization_widget = create_skills_circle()
    return visualization_widget


def create_visualization_4():
    # Create the fourth visualization using the imported function
    visualization_widget = create_needs_circle()
    return visualization_widget


class VisualizationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a stacked widget to hold the different visualizations
        self.stacked_widget = QtWidgets.QStackedWidget()

        # Create a widget for the buttons
        buttons_widget = QtWidgets.QWidget()
        buttons_layout = QtWidgets.QVBoxLayout(buttons_widget)
        buttons_layout.setAlignment(QtCore.Qt.AlignCenter)
        buttons_layout.addStretch(1)

        # Create the buttons
        all_three_circles_button = QtWidgets.QPushButton("All Three Circles")
        all_three_circles_button.setFixedSize(200, 40)  # Set custom button size
        all_three_circles_button.clicked.connect(lambda: self.show_page(0))
        buttons_layout.addWidget(all_three_circles_button)

        interests_circle_button = QtWidgets.QPushButton("Interests Circle")
        interests_circle_button.setFixedSize(200, 40)  # Set custom button size
        interests_circle_button.clicked.connect(lambda: self.show_page(1))
        buttons_layout.addWidget(interests_circle_button)

        skills_circle_button = QtWidgets.QPushButton("Skills Circle")
        skills_circle_button.setFixedSize(200, 40)  # Set custom button size
        skills_circle_button.clicked.connect(lambda: self.show_page(2))
        buttons_layout.addWidget(skills_circle_button)

        needs_circle_button = QtWidgets.QPushButton("Needs Circle")
        needs_circle_button.setFixedSize(200, 40)  # Set custom button size
        needs_circle_button.clicked.connect(lambda: self.show_page(3))
        buttons_layout.addWidget(needs_circle_button)

        buttons_layout.addStretch(1)

        # Set the buttons widget as the central widget of the window
        self.setCentralWidget(buttons_widget)

        # Create back and next buttons
        self.back_button = QtWidgets.QPushButton("Back")
        self.back_button.clicked.connect(self.show_previous_page)
        self.back_button.setVisible(False)  # Hide the button initially

        self.next_button = QtWidgets.QPushButton("Next")
        self.next_button.clicked.connect(self.show_next_page)
        self.next_button.setVisible(False)  # Hide the button initially

        # Add the buttons to the status bar
        self.statusBar().addWidget(self.back_button)
        self.statusBar().addWidget(self.next_button)

    def show_page(self, index):
        # Switch to the selected page in the stacked widget
        if self.stacked_widget.count() == 0:
            self.stacked_widget.addWidget(create_visualization_1())
            self.stacked_widget.addWidget(create_visualization_2())
            self.stacked_widget.addWidget(create_visualization_3())
            self.stacked_widget.addWidget(create_visualization_4())

        self.setCentralWidget(self.stacked_widget)
        self.stacked_widget.setCurrentIndex(index)

        # Show/hide back and next buttons based on the current page
        self.update_navigation_buttons(index)

    def show_previous_page(self):
        current_index = self.stacked_widget.currentIndex()
        if current_index > 0:
            self.stacked_widget.setCurrentIndex(current_index - 1)
            self.update_navigation_buttons(current_index - 1)

    def show_next_page(self):
        current_index = self.stacked_widget.currentIndex()
        if current_index < self.stacked_widget.count() - 1:
            self.stacked_widget.setCurrentIndex(current_index + 1)
            self.update_navigation_buttons(current_index + 1)

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

    visualization_window.resize(window_width, window_height)
    visualization_window.setWindowTitle("My Venn Diagram")

    introduction_window.resize(window_width, window_height)
    introduction_window.setWindowTitle("Intro")

    introduction_window.show()
    app.exec_()
