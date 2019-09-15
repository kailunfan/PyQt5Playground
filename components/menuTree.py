from PyQt5 import QtCore
from PyQt5 import QtWidgets


class MenuTree(QtWidgets.QDockWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setUI()

    def setUI(self):
        self.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        self.tree = QtWidgets.QTreeWidget(self)
        self.tree.headerItem().setText(0, "WidgetDemoName")
        self.setWidget(self.tree)

    def sizeHint(self):
        return QtCore.QSize(200, 900)

    def clear(self):
        self.tree.clear()

    def add_menu(self, text):
        tree_item = QtWidgets.QTreeWidgetItem(self.tree, [text])
        return tree_item
