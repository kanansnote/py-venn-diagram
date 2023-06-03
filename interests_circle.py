from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.patches import Wedge


def create_interests_circle():
    # Create a new Matplotlib figure
    fig = Figure()

    # Create an Axes object in the figure
    ax = fig.add_subplot(111)

    # Create wedges to divide the circle into sections
    wedge1 = Wedge((0.5, 0.5), 0.4, -60, 110, facecolor='red')
    wedge2 = Wedge((0.5, 0.5), 0.4, 110, -60, facecolor='green')

    # Add the wedges to the Axes
    ax.add_patch(wedge1)
    ax.add_patch(wedge2)

    # Set the aspect ratio of the Axes
    ax.set_aspect('equal')

    # Turn off the display of the axes and numbers
    ax.axis('off')

    # Add labels to each section
    ax.text(0.22, 0.42, 'Philosophical')
    ax.text(0.63, 0.55, 'Artistic')

    # Set the title of the plot
    ax.set_title('Artistic & Philosophical Interests')

    # Create a PyQt5 widget to hold the Matplotlib figure
    canvas = FigureCanvas(fig)
    return canvas
