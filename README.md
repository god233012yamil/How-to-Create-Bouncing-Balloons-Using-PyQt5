# How-to-Create-Bouncing-Balloons-Using-PyQt5
This application can serve as a starting point for programmers  looking to understand how animation and object movement can be  handled in PyQt5. The key concepts demonstrated here include  basic PyQt5 widget creation, handling the paint event, using  QTimer for animation, and simple object physics for movement.

# Code Video
https://github.com/god233012yamil/How-to-Create-Bouncing-Balloons-Using-PyQt5/assets/5813359/f7f46f7b-5200-40e6-93ce-a192246a610a

# Code Description
1. Initialization: The application window is set up, and a list of balloons is generated. Each balloon is assigned random attributes including position, size, color, and movement direction. The position is constrained to ensure that the entire balloon is visible within the application window, and is never initially positioned partly outside the window.

2. Animation: A QTimer is set up to call the update method periodically (every 100ms in this case), triggering a repaint of the widget. This technique is fundamental to creating animations in PyQt5.

3. Painting: In the paintEvent method, each balloon in the list is drawn onto the widget using its current properties. The balloon is drawn as a filled ellipse with a color defined by a QBrush. A transparent QPen is used to avoid drawing an outline around the ellipse.

4. Movement and Collision: After each balloon is painted, its position is updated based on its movement direction. If the balloon's new position would place it outside the boundaries of the window, the direction of movement is reversed, creating a bouncing effect.

This application serves as a foundation upon which more complex behaviors and features can be built. For instance, you might add interactivity (allowing the user to click on balloons to "pop" them), different shapes, or varied movement patterns. The possibilities are limited only by your imagination!

