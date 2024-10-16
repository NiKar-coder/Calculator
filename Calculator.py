from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
import qdarktheme
import math


class Calculator():
    def __init__(self):
        self.globs = {
            "__builtins__": {},
            "sqrt": lambda x: math.sqrt(x),
            "abs": lambda x: abs(x),
            "tg": lambda x: math.tan(math.radians(x)),
            "sin": lambda x: math.sin(math.radians(x)),
            "ctg": lambda x: math.cos(math.radians(x)) / math.sin(math.radians(x)),
            "cos": lambda x: math.cos(math.radians(x)),
            "rad": lambda x: math.radians(x),
            "deg": lambda x: math.degrees(x)
        }

    def calculate(self, num):
        for x, y in ("^", "**"), (",", "."), (" ", ""):
            num = num.replace(x, y)
        try:
            return str(round(eval(num, self.globs, {}), 3))
        except Exception:
            return "Error!"


FONT = QtGui.QFont()
FONT.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1322, 174)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 1281, 111))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rm = QtWidgets.QPushButton(parent=self.layoutWidget)

        self.rm.setFont(FONT)
        self.rm.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.rm.setObjectName("rm")
        self.verticalLayout_2.addWidget(self.rm)
        self.cm = QtWidgets.QPushButton(parent=self.layoutWidget)

        self.cm.setFont(FONT)
        self.cm.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.cm.setObjectName("cm")
        self.verticalLayout_2.addWidget(self.cm)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.input_ = QtWidgets.QLineEdit(parent=self.layoutWidget)

        self.input_.setFont(FONT)
        self.input_.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.input_.setPlaceholderText("Введите выражение")
        self.input_.setClearButtonEnabled(True)
        self.input_.setObjectName("input_")
        self.horizontalLayout.addWidget(self.input_)
        self.btn = QtWidgets.QPushButton(parent=self.layoutWidget)

        self.btn.setFont(FONT)
        self.btn.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn.setDefault(False)
        self.btn.setObjectName("btn")
        self.horizontalLayout.addWidget(self.btn)
        self.result = QtWidgets.QLineEdit(parent=self.layoutWidget)

        self.result.setFont(FONT)
        self.result.setReadOnly(True)
        self.result.setObjectName("result")
        self.horizontalLayout.addWidget(self.result)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.m_plus = QtWidgets.QPushButton(parent=self.layoutWidget)

        self.m_plus.setFont(FONT)
        self.m_plus.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.m_plus.setObjectName("m_plus")
        self.verticalLayout.addWidget(self.m_plus)
        self.m_minus = QtWidgets.QPushButton(parent=self.layoutWidget)

        self.m_minus.setFont(FONT)
        self.m_minus.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.m_minus.setObjectName("m_minus")
        self.verticalLayout.addWidget(self.m_minus)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1322, 23))

        self.menubar.setFont(FONT)
        self.menubar.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.rm.setText(_translate("MainWindow", "RM"))
        self.cm.setText(_translate("MainWindow", "CM"))
        self.btn.setText(_translate("MainWindow", "="))
        self.m_plus.setText(_translate("MainWindow", "M+"))
        self.m_minus.setText(_translate("MainWindow", "M-"))


CALCULATOR = Calculator()


class Calc_Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.initUI()
        self.mem = ""

    def initUI(self):
        self.setFocus()
        self.btn.clicked.connect(self.calculate)
        self.m_plus.clicked.connect(self.m_p)
        self.m_minus.clicked.connect(self.m_m)
        self.rm.clicked.connect(self.rm_)
        self.cm.clicked.connect(self.cm_)
        self.menubar.addAction('Help (F1)', self.help)
        self.menubar.addAction('Calculate (F5)', self.calculate)

    def cm_(self):
        self.mem = ""
        self.input_.setFocus()

    def setFocus(self):
        self.result.setText("")
        self.input_.setFocus()

    def calculate(self):

        self.result.setText(
            CALCULATOR.calculate(self.input_.text()))
        self.input_.setText("")
        self.input_.setFocus()

    def rm_(self):

        self.input_.setText(self.input_.text() + self.mem)
        self.setFocus()

    def set_m(self):
        return float(self.result.text())

    def m_p_m(self, a):
        try:
            self.mem = a + str(self.set_m())
            self.setFocus()
        except Exception:
            pass

    def m_p(self):
        self.m_p_m('')

    def m_m(self):
        self.m_p_m('-')

    def init_help(self):
        self.dlg = QMessageBox(self)
        self.dlg.setWindowTitle("Help")
        self.dlg.setFont(FONT)
        self.dlg.setText("Functions:\nabs(x) - Find the module of the number x\ncos(x) - Find the cosine of the number x\nctg(x) - Find the cotangent of the number x\ndeg(x) - Convert x radians to degrees\nsin(x) - Find the sine of the number x\nrad(x) - Convert x degrees to radians\nsqrt(x) - Find the square root of the number x\ntg(x) - find the tangent of the number x")
        self.dlg.setCursor(QtGui.QCursor(
            QtCore.Qt.CursorShape.PointingHandCursor))
        self.dlg.exec()

    def help(self):
        self.init_help()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key.Key_F5.value:
            self.calculate()
        elif e.key() == Qt.Key.Key_F1.value:
            self.help()


def main():
    qdarktheme.enable_hi_dpi()
    app = QApplication(sys.argv)
    qdarktheme.setup_theme(
        custom_colors={"primary": "fff"}, corner_shape="sharp")
    ex = Calc_Window()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
