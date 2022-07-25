import json

from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication
from PyQt5 import uic

app = QApplication([])


class ConfigTools(object):
    def __init__(self, configPath):
        self.path = configPath
        self.config = {}
        self.keys = []

    def add_config(self, key, value):
        self.config[key] = value

    def del_config(self, key):
        del self.config[key]

    def edit_config(self, key, value):
        self.config[key] = value

    def get_config(self, key):
        return self.config[key]

    def get_configs(self):
        return self.config

    def get_length(self):
        return len(self.config)

    def key_is_exist(self, key):
        return key in self.config

    def value_is_exist(self, value):
        for key in self.config:
            if self.config[key] == value:
                return True
        return False

    def sort_config(self):
        return sorted(self.config.items(), key=lambda x: x[0])

    def get_keys(self):
        for key in self.config:
            self.keys.append(key)
        return self.keys

    def save_config(self):
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(self.config, f)

    def load_config(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            self.config = json.load(f)


path = ConfigTools('./config.json')
path.load_config()
path = path.get_config('appPathConfig') + 'appPathConfig.json'


class AppManager(ConfigTools):
    def __init__(self, configPath):
        super(AppManager, self).__init__(configPath)
        self.load_config()

    def appIsExist(self, appName):
        return self.key_is_exist(appName)

    def getAppPath(self, appName):
        return self.get_config(appName)

    def delAppPath(self, appName):
        self.del_config(appName)

    def addAppPath(self, appName, configPath):
        self.add_config(appName, configPath)

    def getAppList(self):
        return self.get_keys()


class AppWindow(QMainWindow):
    def __init__(self, appName, appPath):
        super(AppWindow, self).__init__()
        self.setWindowTitle(appName)
        self.browser = QWebEngineView()
        self.browser.load(QUrl(appPath))
        self.setCentralWidget(self.browser)

    def showThis(self):
        self.show()
        app._exec()


class AppLoader(AppManager):
    def __init__(self, configPath):
        super(AppLoader, self).__init__(configPath)
        self.appWindow = None

    def loadApp(self, appName):
        QMessageBox.warning(None, '警告', '你正在运行第三方小程序，我们无法保证你在小程序内的安全（包括但不限于：网络安全、计算机安全和财务安全），且不负任何责任！')
        if self.appIsExist(appName):
            QMessageBox.about(None, '提示', '启动成功！')
            self.appWindow = AppWindow(appName, self.getAppPath(appName))
        else:
            QMessageBox.critical(None, '错误', '小程序不存在！')


class AppChoseWindow(QMainWindow, AppManager, AppLoader):
    def __init__(self):
        super(AppChoseWindow, self).__init__()
        super(AppManager).__init__(path)
        super(AppLoader).__init__(path)
        uic('./ui/smallProgramRunner.ui', self)
        self.appList.addItems(self.getAppList())
        self.smallProgramButton.clicked.connect(self.run)

    def run(self):
        self.loadApp(self.appList.currentItem().text())
