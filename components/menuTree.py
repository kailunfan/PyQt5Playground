
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QDockWidget


class MenuTree(QTreeWidget.QDockWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setUI()
        self.fill_data()
        self.connect()

    def setUI(self):
        self.tree = QtWidgets.QTreeWidget(self)
        self.tree.headerItem().setText(0, "WidgetDemoName")

    def clear(self):
        self.tree.clear()

    def add_menu(self, text):
        tree_item = QtWidgets.QTreeWidgetItem(self.tree, text)
        return tree_item
