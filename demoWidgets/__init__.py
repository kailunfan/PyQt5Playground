from importlib import reload

from . import QTreeWidgetDemo
from . import QtWebEngineViewDemo
from . import QDialogDemo
from . import QTableWidgetDemo
from . import QTabWidgetDemo
from . import QLayoutDemo


reload(QtWebEngineViewDemo)
reload(QTreeWidgetDemo)
reload(QTabWidgetDemo)
reload(QTableWidgetDemo)
reload(QDialogDemo)
reload(QLayoutDemo)
