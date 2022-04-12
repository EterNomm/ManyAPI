# importing required libraries

from PyQt5.QtCore import * 

from PyQt5.QtWidgets import * 

from PyQt5.QtGui import * 

from PyQt5.QtWebEngineWidgets import * 

from PyQt5.QtPrintSupport import * 

import os 

import sys 

 

# main window

class MainWindow(QMainWindow): 

 

    # constructor 

    def __init__(self, *args, **kwargs): 

        super(MainWindow, self).__init__(*args, **kwargs) 

 

        # creating a tab widget 

        self.tabs = QTabWidget() 

 

        # making document mode true 

        self.tabs.setDocumentMode(True) 

 

        # adding action when double clicked 

        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick) 

 

        # adding action when tab is changed 

        self.tabs.currentChanged.connect(self.current_tab_changed) 

 

        # making tabs closeable 

        self.tabs.setTabsClosable(True) 

 

        # adding action when tab close is requested 

        self.tabs.tabCloseRequested.connect(self.close_current_tab) 

 

        # making tabs as central widget 

        self.setCentralWidget(self.tabs) 

 

        # creating a status bar 

        self.status = QStatusBar() 

 

        # setting status bar to the main window 

        self.setStatusBar(self.status) 

 

        # creating a tool bar for navigation 

        navtb = QToolBar("Navigation") 

 

        # adding tool bar tot he main window 

        self.addToolBar(navtb) 

 

        # creating back action 

        back_btn = QAction("Back", self) 

 

        # setting status tip 

        back_btn.setStatusTip("Back to previous page") 

 

        # adding action to back button 

        # making current tab to go back 

        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back()) 

 

        # adding this to the navigation tool bar 

        navtb.addAction(back_btn) 

 

        # similarly adding next button 

        next_btn = QAction("Forward", self) 

        next_btn.setStatusTip("Forward to next page") 

        next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward()) 

        navtb.addAction(next_btn) 
