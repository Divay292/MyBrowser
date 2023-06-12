import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        nav = QToolBar()
        self.addToolBar(nav)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        nav.addAction(back_btn)

        forward = QAction('Forward', self)
        forward.triggered.connect(self.browser.forward)
        nav.addAction(forward)

        reload = QAction('Reload', self)
        reload.triggered.connect(self.browser.reload)
        nav.addAction(reload)

        home = QAction('Home', self)
        home.triggered.connect(self.navigate_home)
        nav.addAction(home)\
        
        self.search_bar = QLineEdit()
        self.search_bar.returnPressed.connect(self.navigate_to_url)
        nav.addWidget(self.search_bar)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://google.com'))

    def navigate_to_url(self):
        url = self.search_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.search_bar.setText(q.toString())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QApplication.setApplicationName('Divays Browser')
    window = MainWindow()
    app.exec_()

