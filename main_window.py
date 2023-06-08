import sys
from PyQt5 import QtWidgets, QtCore
from all_three_circles import create_all_three_circles
from interests_circle import create_interests_circle
from skills_circle import create_skills_circle
from needs_circle import create_needs_circle


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
    window = VisualizationWindow()
    screen_geometry = QtWidgets.QApplication.desktop().availableGeometry()
    window.resize(screen_geometry.width(), screen_geometry.height())
    window.show()
    app.exec_()
