from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


def create_all_three_circles():
    # Create a new Matplotlib figure
    fig = Figure(frameon=False)

    # Create an Axes object in the figure
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')

    # Set the labels for each circle
    labels = ['Artistic & Philosophical Interests', 'Technical & Nutritional Skills', 'Financial & Healthy Needs']

    # Create the Venn diagram with three circles
    from matplotlib_venn import venn3
    venn_diagram = venn3(subsets=(1, 1, 1, 1, 1, 1, 1), set_labels=labels, ax=ax)

    # Add labels to the intersections of the circles
    venn_diagram.get_label_by_id('100').set_text('Fi')
    venn_diagram.get_label_by_id('010').set_text('Se & Ni')
    venn_diagram.get_label_by_id('001').set_text('Te')
    venn_diagram.get_label_by_id('110').set_text('Fe')
    venn_diagram.get_label_by_id('011').set_text('Si')
    venn_diagram.get_label_by_id('101').set_text('Ti')
    venn_diagram.get_label_by_id('111').set_text('Ne')

    # Create a PyQt5 widget to hold the Matplotlib figure
    canvas = FigureCanvas(fig)
    return canvas
