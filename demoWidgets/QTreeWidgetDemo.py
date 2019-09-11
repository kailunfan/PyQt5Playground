from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem


class QTreeWidgetDemo(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setUI()
        self.fill_data()
        self.connect()

    def setUI(self):
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.headerItem().setText(0, "id")
        self.headerItem().setText(1, "name")

    def fill_data(self):
        for i in range(10):
            QTreeWidgetItem(self, [str(i), f"NUM_{i}"])

    def connect(self):
        self.customContextMenuRequested.connect(self.show_menu)

    def show_menu(self, pos):
        print(pos)
        print(self.itemAt(pos))
