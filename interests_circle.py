from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.patches import Wedge


def create_interests_circle():
    # Create a new Matplotlib figure
    fig = Figure()

    # Create an Axes object in the figure
    ax = fig.add_subplot(111)

    # Create wedges to divide the circle into sections
    wedge1 = Wedge((0.5, 0.5), 0.4, 0, 90, facecolor='red')
    wedge2 = Wedge((0.5, 0.5), 0.4, 90, 180, facecolor='green')
    wedge3 = Wedge((0.5, 0.5), 0.4, 180, 270, facecolor='blue')
    wedge4 = Wedge((0.5, 0.5), 0.4, 270, 360, facecolor='yellow')

    # Add the wedges to the Axes
    ax.add_patch(wedge1)
    ax.add_patch(wedge2)
    ax.add_patch(wedge3)
    ax.add_patch(wedge4)

    # Set the aspect ratio of the Axes
    ax.set_aspect('equal')

    # Turn off the display of the axes and numbers
    ax.axis('off')

    # Add labels to each section
    ax.text(0.25, 0.65, 'Section 1')
    ax.text(0.6, 0.65, 'Section 2')
    ax.text(0.25, 0.3, 'Section 3')
    ax.text(0.6, 0.3, 'Section 4')

    # Set the title of the plot
    ax.set_title('Artistic & Philosophical Interests')

    # Create a PyQt5 widget to hold the Matplotlib figure
    canvas = FigureCanvas(fig)
    return canvas
