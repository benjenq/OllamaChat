# pyinstaller -F --clean --windowed --icon=icon.ico OllamaChat.py
from PyQt5 import QtWidgets,QtGui # ,QtCore PyQt5 : pip3 install pyqt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * #QKeySequence
import UIMainWindow
import qdarktheme,webbrowser

#from ollamaHelper import llmChat, modelList #, ollamaChat, modelList
from ChatQThread import ChatQThread,modelList

class mainWin(QtWidgets.QMainWindow,UIMainWindow.Ui_MainWindow):
    def __init__(self,parent=None):
        super(mainWin,self).__init__()
        self.setupUi(self)
        #self.btnSent.clicked.connect(lambda: self.doChat(self.txtask))
        self.aMenuStop.setEnabled(False)
        self.aMenuStop.triggered.connect(lambda: self.actionStopMessages())
        self.aMenuStop.setShortcut(QKeySequence("Ctrl+Shift+S"))
        self.aMenuClean.triggered.connect(lambda: self.actionCleanMessages(self.txtMessages)) 
        self.aMenuClean.setShortcut(QKeySequence("Ctrl+Shift+C"))
        self.aMenuSearch.triggered.connect(lambda: self.actionOpenURL('https://ollama.com/search'))
        self.aMenuSearch.setShortcut(QKeySequence("Ctrl+Shift+W"))
        self.aMenuExit.triggered.connect(self.exitApp)
        self.aMenuExit.setShortcut(QKeySequence("Ctrl+Q"))
        self.btnModelList.setShortcut(QKeySequence("Ctrl+Shift+R"))
        self.cbModel.currentTextChanged.connect(lambda: self.txtPrompt.setFocus())

        self.btnModelList.clicked.connect(lambda:self.genCBItems(self.cbModel))
        self.txtPrompt.returnPressed.connect(lambda: self.doChat(self.txtPrompt)) #按下 Enter 觸發

        self.chat_thread = ChatQThread() #建立 Ollama 對話 Thread  # 儲存 QThread 物件，避免重複建立
        #self.chat_thread.breakShortcut = "⇧+⌘+S" if sys.platform == 'darwin' else "Ctrl+Shift+S"
        self.chat_thread.messages_signal.connect(self.chatMessages)
        self.chat_thread.status_signal.connect(self.chatStatus)
        self.chat_thread.finished_signal.connect(self.chatFinished)

        self.genCBItems(self.cbModel)
        self.txtPrompt.setFocus()


        '''尋找元件範例
        txt = self.centralwidget.findChild(QPlainTextEdit, "txt1")
        txt.setPlainText("DDDD")
        self.chk_1.setChecked(True)
        '''
    def chatMessages(self,res:str):
        self.txtMessages.setPlainText(self.txtMessages.toPlainText()+res)
        self.txtMessages.verticalScrollBar().setValue(self.txtMessages.verticalScrollBar().maximum())
        QtWidgets.QApplication.processEvents()

    def chatStatus(self,code:int, status:str):
        # https://stackoverflow.com/questions/5795214/qt-statusbar-color
        if code < 0:
            self.statusBar.setStyleSheet("QStatusBar{background:rgba(160,0,0,255);color:white;font-weight:bold;}")
        elif code == 0:
            self.statusBar.setStyleSheet("")
        else:
            self.statusBar.setStyleSheet("QStatusBar{background:rgba(160,160,0,255);color:black;font-weight:bold;}")
        self.statusBar.showMessage(status)
        QtWidgets.QApplication.processEvents()

    def chatFinished(self,finished:bool):
        self.txtPrompt.setEnabled(finished)
        self.cbModel.setEnabled(finished)
        self.btnModelList.setEnabled(finished)
        self.aMenuStop.setEnabled(not finished)
        if(finished):
            self.txtPrompt.setText('')
            self.txtPrompt.setFocus()
        QtWidgets.QApplication.processEvents()

    def genCBItems(self, obj): #產生下拉項目
        obj.clear()
        found, items = modelList()
        if found:
            s = 's' if len(items) >= 2 else ''
            for item in items:
                obj.addItem(item)
            self.chatStatus(0, f'Found {len(items)} model{s}.')
        else:
            self.chatStatus(-1, items[0])
        self.txtPrompt.setFocus()

    def doChat(self,request:QTextEdit):
        if self.chat_thread and self.chat_thread.isRunning():  # 避免重複啟動線程
            print("⏳ 任務執行中，請稍候...")
            return
        #llmChat(request.text(), self.cbModel.currentText(),self.callBack)
        self.chat_thread.startChat(request.text(),self.cbModel.currentText())
    
    def actionStopMessages(self):
        self.chat_thread.messageBreak()

    def actionCleanMessages(self,obj:QTextEdit):
        self.chat_thread.messageClear()
        obj.setPlainText('')
        self.chatStatus(0,'')
        self.txtPrompt.setFocus()
    
    def actionOpenURL(self,strUrl:str):
        webbrowser.open(strUrl)

    def exitApp(self):
        self.close()
    
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        choose = QtWidgets.QMessageBox.question(self,"Question","This App will close & exit.\nAre you sure?",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No )
        if choose == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            self.txtPrompt.setFocus()
        #return super().closeEvent(event)

# https://stackoverflow.com/questions/41331201/pyqt-5-and-4k-screen/51914685#51914685
# PyQt 5 and 4k screen
if __name__ == "__main__":
    import sys,os
    os.environ["QT_ENABLE_HIGHDPI_SCALING"]   = "1"
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    os.environ["QT_SCALE_FACTOR"]             = "1"
    app = QtWidgets.QApplication(sys.argv)
    qdarktheme.setup_theme("auto")
    win = mainWin()
    win.show()
    sys.exit(app.exec_())
    