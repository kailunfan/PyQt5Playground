from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import QUrl


class QtWebEngineViewDemo(QtWebEngineWidgets.QWebEngineView):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi()
        self.connect()

    def setupUi(self):
        self.load(QUrl('https://www.baidu.com'))

    def connect(self):
        self.loadFinished.connect(self.load_cookies)

    def load_cookies(self):
        def func(data):
            pass

        self.page().runJavaScript('document.cookie', func)

    def logout(self):
        self.page().profile().cookieStore().deleteAllCookies()
        self.reload()
