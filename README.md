# Venn Diagram

The concept for this project was developed since *January 2023*, and the programming part started in *May 2023*. It has been discontinued for several months, and there are no plans to resume work yet.

## Coding Solution

I'm considering using `Python`, due to its versatility and popularity in data visualization field. The project consists of multiple code files, each serving a specific purpose:

- `main_window.py` is the main window implementation for the visualization project. It utilizes the `PyQt5` library for GUI development.
- `all_three_circles.py` creates a visualization with three circles; `interests_circle.py` represents artistic and philosophical interests, `skills_circle.py` technical and nutritional skills, and `needs_circle.py` financial, health and communication needs.

Each code file includes functions that generate the respective visualizations using the `Matplotlib` library, which are then rendered using `PyQt5` to display them as interactive widgets.

Additionally, `pygame` library is implemented in order to prevent any potential problems related with audio playback upon clicking the "**speaker**" icon.

## Requirements

- Python 3.x
- PyQt5
- Pygame
- Matplotlib
- Matplotlib_venn

## Usage

1. Clone the project repository to your IDE:

   `git clone https://github.com/kanansnote/My-Venn-Diagram.git`

2. Install the required dependencies. Ensure you have installed the libraries below:

   `pip install pyqt5 pygame matplotlib matplotlib_venn`

3. Run the project:

   `python main_window.py`

4. The **Introduction Window** will appear with showing a welcome message, an animated GIF, and a description of the project:

Introduction Window
![Introduction Window](./media/windows_introduction_window.gif)

Click the `Start` button to proceed to the **Visualizations Window**. To exit the application, click the `Cancel` button.

5. In the **Visualizations Window**, you can explore the visualizations by the name of the current one on the left side corner:

Visualizations Window
![Visualizations Window](./media/windows_visualizations_window.gif)

Click the `Next` and `Back` buttons in the status bar to implement the navigation process with all the visualizations.
Click the `Finish` button to end the visualization any time by closing the application.

## License

The project is licensed under the **GNU General Public License (GPL) version 3.0**.

**The GPL** is a popular open-source license that grants users the freedom to use, modify, and distribute the software. It ensures that any derivative works or modifications made to the software are also subject to the GPL, promoting the principles of openness and collaboration.

For more details, please refer to the [full text of the GPL](https://github.com/kanansnote/My-Venn-Diagram/blob/main/LICENSE).

## Additional Info

<div class="additionalInfo">
   <table>
      <tr>
         <th colspan="2">Resources</th>
         <th colspan="6">Icons</th>
      </tr>
      <tr>
         <td>
            <a href="https://academo.org/demos/venn-diagram-generator/">Venn Diagram Generator</a>
         </td>
         <td>
            <a href="https://tenor.com/view/full-circle-olanrogers-youtube-gif-4749604">Full Circle GIF</a>
         </td>
         <td>
            <img src="media/buttons/speaker.png" height="10"/>
            <a href="https://icon-icons.com/icon/speaker-sound-volume/54138">Speaker</a>
         </td>
         <td>
            <img src="media/buttons/start.png" height="10"/>
            <a href="https://icon-icons.com/icon/presentation-board-graph-chart/108631">Start</a>
         </td>
         <td>
            <img src="media/buttons/cancel.png" height="10"/>
            <a href="https://icon-icons.com/icon/cancel/73703">Cancel</a>
         </td>
         <td>
            <img src="media/buttons/back.png" height="10"/>
            <a href="https://icon-icons.com/icon/above-the-arrow/1049">Back</a>
         </td>
         <td>
            <img src="media/buttons/next.png" height="10"/>
            <a href="https://icon-icons.com/icon/Next-arrow/1058">Next</a>
         </td>
         <td>
            <img src="media/buttons/finish.png" height="10"/>
            <a href="https://www.iconarchive.com/show/farm-fresh-icons-by-fatcow/flag-finish-icon.html">Finish</a>
         </td>
      </tr>
   </table>
</div>


