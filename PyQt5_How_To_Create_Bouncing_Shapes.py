import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen
from PyQt5.QtCore import Qt, QTimer, QPointF
import numpy as np
import abc  # for creating abstract base classes


# Abstract base class for all shapes
class Shape(metaclass=abc.ABCMeta):
    def __init__(self, x_range, y_range, size, dx, dy, color):
        self.x = np.random.uniform(size, x_range - size)
        self.y = np.random.uniform(size, y_range - size)
        self.size = size
        self.dx = dx
        self.dy = dy
        self.color = color

    @abc.abstractmethod
    def draw(self, painter):
        pass


# Subclass for Balloons (circles)
class Balloon(Shape):
    def draw(self, painter):
        painter.drawEllipse(QPointF(self.x, self.y), self.size, self.size)


# Subclass for Squares
class Square(Shape):
    def draw(self, painter):
        painter.drawRect(self.x - self.size/2, self.y - self.size/2, self.size, self.size)


class ShapeDrawerWidget(QWidget):
    def __init__(self, num_shapes=50):
        super().__init__()

        # Set the window's attributes
        self.setWindowTitle('Bouncing Shapes Screensaver')
        self.setGeometry(50, 50, 800, 600)

        # Create a list of Shapes (Balloons and Squares) with random properties
        self.shapes = [
            np.random.choice([Balloon, Square])(
                x_range=self.width(),
                y_range=self.height(),
                size=np.random.uniform(10, 25),
                dx=np.random.uniform(-2, 2),
                dy=np.random.uniform(-2, 2),
                color=QColor(np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))
            )
            for _ in range(num_shapes)
        ]

        # Setup the timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)  # Trigger update function every time the timer times out
        self.timer.start(10)  # Timeout every 100 ms

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setPen(Qt.NoPen)  # Set transparent pen

        for shape in self.shapes:
            # Create a new brush with the shape's color
            brush = QBrush()
            brush.setColor(shape.color)
            brush.setStyle(Qt.SolidPattern)
            painter.setBrush(brush)

            # Draw the shape using its draw method
            shape.draw(painter)

            # Update the shape's position
            shape.x += shape.dx
            shape.y += shape.dy

            # Check for collision with borders
            if shape.x - shape.size < 0 or shape.x + shape.size > self.width():
                shape.dx *= -1  # Reverse horizontal direction
            if shape.y - shape.size < 0 or shape.y + shape.size > self.height():
                shape.dy *= -1  # Reverse vertical direction


def main():
    app = QApplication(sys.argv)

    shape_drawer = ShapeDrawerWidget()
    shape_drawer.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

