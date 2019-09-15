from PyQt5 import QtWidgets, QtGui
import sys
import random


class QTableWidgetDemo(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setup_ui()
        self.fill_data()
        self.connect()

    def setup_ui(self):
        self.setSortingEnabled(True)
        self.setColumnCount(4)
        self.horizontalHeader().setStretchLastSection(True)
        self.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem('姓名'))
        self.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem('姓别'))
        self.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem('爱好'))
        self.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem('操作'))

    def fill_data(self):
        for i in range(100):
            self.setRowCount(self.rowCount() + 1)
            id_item = QtWidgets.QTableWidgetItem('用户{:0>2d}'.format(i))
            id_item.id = i
            self.setItem(i, 0, id_item)
            self.setItem(i, 1, QtWidgets.QTableWidgetItem("男" if i % 2 == 0 else "女"))
            self.setItem(i, 2, QtWidgets.QTableWidgetItem(['吃饭', '睡觉', '打豆豆'][random.randint(0, 2)]))
            btn_group = QtWidgets.QWidget(self)
            btn_group.id = i
            btn_group_layout = QtWidgets.QHBoxLayout(btn_group)
            del_btn = QtWidgets.QPushButton('删除', btn_group)
            confirm_btn = QtWidgets.QPushButton('修改', btn_group)
            confirm_btn.clicked.connect(lambda: print(self.sender().parent().id))
            del_btn.clicked.connect(self.remove)
            btn_group_layout.addWidget(del_btn)
            btn_group_layout.addWidget(confirm_btn)
            self.setCellWidget(i, 3, btn_group)

    def remove(self):
        for i in range(self.rowCount()):
            if self.sender().parent().id == self.item(i, 0).id:
                self.removeRow(i)
                break

    def connect(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = QTableWidgetDemo()
    ui.show()
    sys.exit(app.exec_())
