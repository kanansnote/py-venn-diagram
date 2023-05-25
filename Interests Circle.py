# Circle with Artistic & Philosophical Interests - May 25, 2023

import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

# Create wedges to divide the circle into sections
wedge1 = Wedge((0.5, 0.5), 0.4, 0, 90, facecolor='red')
wedge2 = Wedge((0.5, 0.5), 0.4, 90, 180, facecolor='green')
wedge3 = Wedge((0.5, 0.5), 0.4, 180, 270, facecolor='blue')
wedge4 = Wedge((0.5, 0.5), 0.4, 270, 360, facecolor='yellow')

# Add the wedges to the current axes
ax = plt.gca()
ax.add_patch(wedge1)
ax.add_patch(wedge2)
ax.add_patch(wedge3)
ax.add_patch(wedge4)

# Set the aspect ratio of the axes
ax.set_aspect('equal')

# Turn off the display of the axes and numbers
plt.axis('off')

# Add labels to each section
plt.text(0.25, 0.65, 'Section 1')
plt.text(0.6, 0.65, 'Section 2')
plt.text(0.25, 0.3, 'Section 3')
plt.text(0.6, 0.3, 'Section 4')

# Set the title of the plot
plt.title('Artistic & Philosophical Interests')

# Show the plot
plt.show()
