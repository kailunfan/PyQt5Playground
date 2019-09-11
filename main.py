import sys
from PyQt5 import QtWidgets, QtCore

import demoWidgets
from components.viewCode import ViewCode
from components.menuTree import MenuTree
import importlib
import sip
import cgitb

cgitb.enable(format="text")


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.connect()
        self.active_name = None

    def active_file_name(self):
        return f"./demoWidgets/{self.active_name}.py"

    def setup_ui(self):
        # 尺寸
        self.showMaximized()
        # 菜单栏
        self.menu = self.menuBar().addMenu('&file')
        self.logout_action = QtWidgets.QAction("&reload", self)
        self.logout_action.triggered.connect(self.reload)
        self.menu.addAction(self.logout_action)
        # 树形菜单
        self.setup_tree_menu()
        # 代码编辑器
        self.setup_code_view()
        # 主控件,QMainWindow一般有一个主控件,用来布局.
        self.cw = QtWidgets.QWidget(self)
        self.setCentralWidget(self.cw)
        # 布局
        self.cw_layout = QtWidgets.QGridLayout(self.cw)
        self.cw_layout.setContentsMargins(0, 0, 0, 0)
        self.cw_layout.setSpacing(0)
        # 加载控件
        self.load_widgets()

    def setup_tree_menu(self):
        self.tree_menu = QtWidgets.QTreeWidget(self)
        self.tree_menu.headerItem().setText(0, "WidgetDemoName")
        dock = QtWidgets.QDockWidget(self)
        dock.setWidget(self.tree_menu)
        dock.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        dock.setFixedWidth(250)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), dock)

    def setup_code_view(self):
        widge = QtWidgets.QWidget(self)
        self.code_view = ViewCode(widge)
        code_widget = QtWidgets.QWidget(self)
        code_layout = QtWidgets.QVBoxLayout(code_widget)
        code_layout.setContentsMargins(0, 0, 0, 0)
        code_layout.setSpacing(2)
        btn = QtWidgets.QPushButton("修改", self)
        btn.clicked.connect(self.save_code)
        code_layout.addWidget(btn)
        code_layout.addWidget(self.code_view)
        dock = QtWidgets.QDockWidget(self)
        dock.setWidget(code_widget)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(2), dock)

    def load_widgets(self):
        self.tree_menu.clear()
        for i in self.cw.children():
            if isinstance(i, QtWidgets.QWidget) and not isinstance(i, QtWidgets.QGridLayout):
                sip.delete(i)
        for k, v in demoWidgets.__dict__.items():
            # if isinstance(v, type) and issubclass(v, QtWidgets.QWidget) and k.endswith("Demo"):
            if k.endswith("Demo"):
                widget_class = getattr(v, k)
                widget = widget_class(self.cw)
                widget.hide()
                self.cw_layout.addWidget(widget)
                tree_item = QtWidgets.QTreeWidgetItem(self.tree_menu, [k[:-4]])
                tree_item.widget_class = widget_class
                tree_item.name = k

    def connect(self):
        self.tree_menu.itemClicked.connect(self.select_widget)

    def select_widget(self, item):
        self.active_name = item.name
        self.show_widget()

    def show_widget(self):
        self.code_view.set_value(self.get_code())
        for i in self.cw.children():
            if self.active_name in str(i.__class__):
                i.show()
                continue
            if isinstance(i, QtWidgets.QWidget) and not isinstance(i, QtWidgets.QGridLayout):
                i.hide()

    def get_code(self):
        with open(self.active_file_name(), encoding='utf-8') as f:
            return f.read()

    def save_code(self):
        def func(code):
            with open(self.active_file_name(), "w", encoding='utf-8') as f:
                f.write(code)
            self.reload()
            self.show_widget()

        self.code_view.get_value(func)

    def reload(self):
        try:
            importlib.reload(demoWidgets)
            self.load_widgets()
        except Exception as e:
            QtWidgets.QMessageBox.information(self, "error", str(e))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())
