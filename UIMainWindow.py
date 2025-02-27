# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'r:\PyQt5OllamaChat\UIMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(591, 312)
        MainWindow.setMinimumSize(QtCore.QSize(410, 180))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/icon-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.txtMessages = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtMessages.setFont(font)
        self.txtMessages.setReadOnly(True)
        self.txtMessages.setObjectName("txtMessages")
        self.verticalLayout_2.addWidget(self.txtMessages)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txtPrompt = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPrompt.setMinimumSize(QtCore.QSize(0, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.txtPrompt.setFont(font)
        self.txtPrompt.setText("")
        self.txtPrompt.setReadOnly(False)
        self.txtPrompt.setObjectName("txtPrompt")
        self.horizontalLayout.addWidget(self.txtPrompt)
        self.cbModel = QtWidgets.QComboBox(self.centralwidget)
        self.cbModel.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cbModel.setFont(font)
        self.cbModel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cbModel.setObjectName("cbModel")
        self.horizontalLayout.addWidget(self.cbModel)
        self.btnModelList = QtWidgets.QPushButton(self.centralwidget)
        self.btnModelList.setMinimumSize(QtCore.QSize(30, 30))
        self.btnModelList.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnModelList.setFont(font)
        self.btnModelList.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnModelList.setObjectName("btnModelList")
        self.horizontalLayout.addWidget(self.btnModelList)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 591, 18))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuTools = QtWidgets.QMenu(self.menuBar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/icon-search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/icon-error.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon2)
        self.actionExit.setObjectName("actionExit")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icon/icon-bookmark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon3)
        self.actionHelp.setObjectName("actionHelp")
        self.aMenuClean = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/icon/icon-edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.aMenuClean.setIcon(icon4)
        self.aMenuClean.setObjectName("aMenuClean")
        self.aMenuExit = QtWidgets.QAction(MainWindow)
        self.aMenuExit.setIcon(icon2)
        self.aMenuExit.setObjectName("aMenuExit")
        self.aMenuSearch = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/icon/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.aMenuSearch.setIcon(icon5)
        self.aMenuSearch.setObjectName("aMenuSearch")
        self.aMenuStop = QtWidgets.QAction(MainWindow)
        self.aMenuStop.setEnabled(True)
        self.aMenuStop.setIcon(icon2)
        self.aMenuStop.setObjectName("aMenuStop")
        self.menuFile.addAction(self.aMenuExit)
        self.menuTools.addAction(self.aMenuStop)
        self.menuTools.addAction(self.aMenuClean)
        self.menuTools.addAction(self.aMenuSearch)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ollama Chat"))
        self.txtPrompt.setPlaceholderText(_translate("MainWindow", "請輸入提問，輸入完成按 Enter 。"))
        self.btnModelList.setToolTip(_translate("MainWindow", "Refresh Model"))
        self.btnModelList.setText(_translate("MainWindow", "⟳"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.aMenuClean.setText(_translate("MainWindow", "Clean Messages"))
        self.aMenuExit.setText(_translate("MainWindow", "Exit"))
        self.aMenuSearch.setText(_translate("MainWindow", "Search Models"))
        self.aMenuStop.setText(_translate("MainWindow", "Stop Messages"))
import resource_rc
