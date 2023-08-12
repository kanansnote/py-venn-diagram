from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.patches import Wedge, Rectangle


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

    # Create a new Axes object for custom elements outside the main circle
    ax_custom = fig.add_axes([0, 0, 1, 1], zorder=-1)  # [left, bottom, width, height]
    ax_custom.axis('off')

    # Create checkbox-like elements in the new Axes
    checkbox1 = Rectangle((0.1, 0.7), 0.02, 0.03, facecolor='red')
    checkbox2 = Rectangle((0.1, 0.35), 0.02, 0.03, facecolor='green')

    ax_custom.add_patch(checkbox1)
    ax_custom.add_patch(checkbox2)

    # Add text next to checkboxes
    ax_custom.text(0.135, 0.712, 'Artistic', va='center')
    ax_custom.text(0.135, 0.362, 'Philosophical', va='center')

    # Create a PyQt5 widget to hold the Matplotlib figure
    canvas = FigureCanvas(fig)
    return canvas
