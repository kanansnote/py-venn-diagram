from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.patches import Wedge


def create_skills_circle():
    # Create a new Matplotlib figure
    fig = Figure()

    # Create an Axes object in the figure
    ax = fig.add_subplot(111)

    # Create wedges to divide the circle into sections
    wedge1 = Wedge((0.5, 0.5), 0.4, 60, -120, facecolor='purple')
    wedge2 = Wedge((0.5, 0.5), 0.4, -120, 60, facecolor='gray')

    # Add the wedges to the Axes
    ax.add_patch(wedge1)
    ax.add_patch(wedge2)

    # Set the aspect ratio of the Axes
    ax.set_aspect('equal')

    # Turn off the display of the axes and numbers
    ax.axis('off')

    # Add labels to each section
    ax.text(0.25, 0.57, 'Technical')
    ax.text(0.57, 0.38, 'Nutritional')

    # Set the title of the plot
    ax.set_title('Technical & Nutritional Skills')

    # Create a PyQt5 widget to hold the Matplotlib figure
    canvas = FigureCanvas(fig)
    return canvas
