from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget,  QLabel, QHBoxLayout, QVBoxLayout, QPushButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLabel Image Demo")

        image_label = QLabel()
        image_label.setPixmap(QPixmap("C:/Users/Tymek/VisualStudioCodeProjects/PySide Training/Qt-For-Python-PySide6-GUI-For-Beginners-The-Fundamentals--main/3.ATourOfQtWidgets/7.QLabel_Images/images/minions.png"))

        layout = QVBoxLayout()
        layout.addWidget(image_label)

        self.setLayout(layout)