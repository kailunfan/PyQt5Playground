from PyQt5 import QtWidgets, QtCore
import sys


class QLayoutDemo(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setup_ui()

    def setup_ui(self):
        self.layout = QtWidgets.QGridLayout(self)
        w_1 = QtWidgets.QTextBrowser(self)

        # splitter: 可退拽调整大小
        splitter = QtWidgets.QSplitter(self)
        splitter.setHandleWidth(5)
        splitter.setLineWidth(2)
        splitter.setOrientation(QtCore.Qt.Horizontal)
        QtWidgets.QTextBrowser(splitter)
        QtWidgets.QTextBrowser(splitter)

        # QHBoxLayout: 横向布局
        w_31 = QtWidgets.QTextBrowser(self)
        w_32 = QtWidgets.QTextBrowser(self)
        w_33 = QtWidgets.QTextBrowser(self)
        w_3 = QtWidgets.QHBoxLayout(self)
        w_3.addWidget(w_31)
        w_3.addWidget(w_32)
        w_3.addWidget(w_33)

        # QVBoxLayout: 纵向布局
        w_v1 = QtWidgets.QTextBrowser(self)
        w_v2 = QtWidgets.QTextBrowser(self)
        w_v = QtWidgets.QVBoxLayout(self)
        w_v.addWidget(w_v1)
        w_v.addWidget(w_v2)

        self.layout.addWidget(w_1, 0, 0, 1, 3)
        self.layout.addWidget(splitter, 1, 0, 1, 3)
        self.layout.addItem(w_3, 2, 0, 1, 3)
        self.layout.addItem(w_v, 0, 3, 3, 1)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = QLayoutDemo()
    ui.show()
    sys.exit(app.exec_())
