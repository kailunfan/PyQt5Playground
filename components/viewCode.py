# -*- encoding:utf-8 -*-
import sys
from PyQt5 import QtWebEngineWidgets, QtWidgets
from PyQt5.QtCore import QUrl, QSize
import os
import base64


class ViewCode(QtWebEngineWidgets.QWebEngineView):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setup_ui()

    def setup_ui(self):
        index = (os.path.split(os.path.realpath(__file__))[0]) + "/monaco_index.html"
        self.load(QUrl.fromLocalFile(index))

    def sizeHint(self):
        return QSize(700, 900)

    def get_value(self, callback):
        self.page().runJavaScript("monaco.editor.getModels()[0].getValue()", callback)

    def set_value(self, data):
        if data is None:
            return
        data = base64.b64encode(data.encode())
        data = data.decode()
        self.page().runJavaScript("monaco.editor.getModels()[0].setValue(Base.decode('{}'))".format(data))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = ViewCode()
    ui.show()
    sys.exit(app.exec_())
