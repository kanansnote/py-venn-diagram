# Venn Diagram - May 17, 2023
# I want to write a venn diagram in python that indicates my interests,
# skills and needs which eventually can help me to choose a career.

import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Set the labels for each circle
labels = ['Artistic & Philosophical', 'Technical', 'Financial & Healthy']

# Create the Venn diagram with three circles
venn_diagram = venn3(subsets=(1, 1, 1, 1, 1, 1, 1), set_labels=labels)

# Add labels to the intersections of the circles
venn_diagram.get_label_by_id('100').set_text('Fi')
venn_diagram.get_label_by_id('010').set_text('Se')
venn_diagram.get_label_by_id('001').set_text('Te')
venn_diagram.get_label_by_id('110').set_text('Fe')
venn_diagram.get_label_by_id('011').set_text('Ni')
venn_diagram.get_label_by_id('101').set_text('Ti')
venn_diagram.get_label_by_id('111').set_text('Ne')

# Display the Venn diagram
plt.title('MBTI Cognitive Functions Venn Diagram')
plt.show()
