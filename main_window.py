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
        self.stacked_widget.addWidget(create_visualization_1())
        self.stacked_widget.addWidget(create_visualization_2())
        self.stacked_widget.addWidget(create_visualization_3())
        self.stacked_widget.addWidget(create_visualization_4())

        # Set the stacked widget as the central widget of the window
        self.setCentralWidget(self.stacked_widget)

        # Create a menu bar with separate menus for each visualization
        menu_bar = self.menuBar()

        # Create a custom widget with a layout to center the menus
        menu_widget = QtWidgets.QWidget()
        menu_layout = QtWidgets.QHBoxLayout(menu_widget)
        menu_layout.setContentsMargins(0, 0, 0, 0)
        menu_layout.addStretch(1)

        all_three_circles_action = QtWidgets.QAction("All Three Circles", self)
        all_three_circles_action.triggered.connect(lambda: self.handle_menu_trigger(all_three_circles_action))
        all_three_circles_button = QtWidgets.QToolButton()
        all_three_circles_button.setDefaultAction(all_three_circles_action)
        menu_layout.addWidget(all_three_circles_button)

        interests_circle_action = QtWidgets.QAction("Interests Circle", self)
        interests_circle_action.triggered.connect(lambda: self.handle_menu_trigger(interests_circle_action))
        interests_circle_button = QtWidgets.QToolButton()
        interests_circle_button.setDefaultAction(interests_circle_action)
        menu_layout.addWidget(interests_circle_button)

        skills_circle_action = QtWidgets.QAction("Skills Circle", self)
        skills_circle_action.triggered.connect(lambda: self.handle_menu_trigger(skills_circle_action))
        skills_circle_button = QtWidgets.QToolButton()
        skills_circle_button.setDefaultAction(skills_circle_action)
        menu_layout.addWidget(skills_circle_button)

        needs_circle_action = QtWidgets.QAction("Needs Circle", self)
        needs_circle_action.triggered.connect(lambda: self.handle_menu_trigger(needs_circle_action))
        needs_circle_button = QtWidgets.QToolButton()
        needs_circle_button.setDefaultAction(needs_circle_action)
        menu_layout.addWidget(needs_circle_button)

        menu_layout.addStretch(1)

        # Add the custom widget to the menu bar as a corner widget
        menu_bar.setCornerWidget(menu_widget, QtCore.Qt.TopLeftCorner)

    def handle_menu_trigger(self, action):
        menu_text = action.text()
        if menu_text == "All Three Circles":
            self.stacked_widget.setCurrentIndex(0)
        elif menu_text == "Interests Circle":
            self.stacked_widget.setCurrentIndex(1)
        elif menu_text == "Skills Circle":
            self.stacked_widget.setCurrentIndex(2)
        elif menu_text == "Needs Circle":
            self.stacked_widget.setCurrentIndex(3)


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
