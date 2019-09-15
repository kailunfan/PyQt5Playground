from PyQt5 import QtWidgets, QtCore
import sys


class Dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setup_ui()
        self.hobby = ''
        self.name = ''

    def setup_ui(self):
        layout = QtWidgets.QHBoxLayout(self)
        self.input_name = QtWidgets.QLineEdit(self)
        self.input_hobby = QtWidgets.QLineEdit(self)
        btn = QtWidgets.QPushButton('确认', self)
        btn.clicked.connect(self.confirm)
        layout.addWidget(self.input_name)
        layout.addWidget(self.input_hobby)
        layout.addWidget(btn)

    def confirm(self):
        self.name = self.input_name.text()
        self.hobby = self.input_hobby.text()
        self.done(QtWidgets.QDialog.Accepted)


class QDialogDemo(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setup_ui()
        self.fill_data()
        self.connect()

    def setup_ui(self):
        btn = QtWidgets.QPushButton("showDialog", self)
        btn.clicked.connect(self.show_dialog)

    def show_dialog(self):
        dia = Dialog(self)
        if dia.exec_():
            print(dia.name, dia.hobby)

    def fill_data(self):
        pass

    def connect(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = QDialogDemo()
    ui.show()
    sys.exit(app.exec_())
