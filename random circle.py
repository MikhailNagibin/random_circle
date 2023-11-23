import sys
from PyQt5.QtWidgets import *
from random import randint
from PyQt5.QtGui import QPainter, QColor
from UI import Ui_MainWindow


class Main_Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def draw_flag(self, qp):
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        a = randint(50, 200)
        qp.drawEllipse(400 - a // 2, 300 - a // 2, a, a)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_Window()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec_())