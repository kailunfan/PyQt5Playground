from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets


class QTabWidgetDemo(QtWidgets.QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setup_ui()
        self.fill_data()
        self.connect()

    def setup_ui(self):
        self.setElideMode(Qt.ElideLeft)
        self.setUsesScrollButtons(True)

    def fill_data(self):
        for i in range(10):
            tab = QtWidgets.QWidget(self)
            QtWidgets.QLabel(f"contents of tab_{i}", tab)
            self.addTab(tab, f'tab_{i}')

    def connect(self):
        pass
