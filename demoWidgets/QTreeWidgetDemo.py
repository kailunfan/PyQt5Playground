from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtGui
import sys
from functools import partial


class QTreeWidgetDemo(QtWidgets.QTreeWidget):
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
            root = QtWidgets.QTreeWidgetItem(self, [str(i), f"Root_{i}"])
            root.setExpanded(True)
            for j in range(3):
                QtWidgets.QTreeWidgetItem(root, [str(j), f"Child_{j}"])

    def connect(self):
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.itemDoubleClicked.connect(lambda x: print(x))
        self.customContextMenuRequested.connect(self.show_menu)

    def show_menu(self, pos):
        item = self.itemAt(pos)
        context_menu = QtWidgets.QMenu(self)
        # 空白处点击,新建根节点
        if not item:
            context_menu.addAction(u'新建根节点').triggered.connect(
                partial(QtWidgets.QTreeWidgetItem, self, ['P', '新增的根节点']))
        else:
            context_menu.addAction(u'新建子节点').triggered.connect(
                partial(QtWidgets.QTreeWidgetItem, item, ['S', '新增的子节点']))
        context_menu.show()
        context_menu.move(QtGui.QCursor.pos())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = QTreeWidgetDemo()
    ui.show()
    sys.exit(app.exec_())
