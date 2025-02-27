#pip3 install ollama
# https://github.com/ollama/ollama-python/blob/main/examples/list.py
from ollama import chat as oChat, list #,ListResponse
from PyQt5.QtCore import QThread, pyqtSignal
import sys
#response: ListResponse = list()
#from typing import Callable

class ChatQThread(QThread):
    messages_signal = pyqtSignal(str)  # 信息串流信號，回傳結果到主線程
    '''信息串流信號，回傳結果到主線程'''
    status_signal = pyqtSignal(int,str) # 狀態文字信號(int 狀態<0:一般,-1:錯誤,1:提醒>, str 狀態文字)，回傳結果到主線程
    '''狀態文字信號，回傳結果到主線程'''
    finished_signal = pyqtSignal(bool) # 完成輸出串流信號，回傳結果到主線程
    '''完成輸出串流信號，回傳結果到主線程'''

    def __init__(self, role_system:str = '用正體中文回答。', model:str=''):
        '''ChatQThread
        ---
        role_system: str, System Role 系統 Role \n
        model: str, model name 模型名稱
        '''
        super().__init__()
        self.breakMesage = False
        self.breakShortcut = "⇧+⌘+S" if sys.platform == 'darwin' else "Ctrl+Shift+S"
        self.model = model
        self.messages = [{'role': 'system', 'content': role_system}]
        self.lastPrompt = ''
        self.started = False #開始回應

    def messageClear(self,role_system:str = '用正體中文回答。'):
        '''清除所有對話紀錄'''
        self.messages.clear()
        self.messages.append({'role': 'system', 'content': role_system})

    def messageBreak(self):
        self.breakMesage = True

    def startChat(self,prompt:str = '', model:str=''):
        '''以 QThread 開始對話
        ---
        prompt: str, 提問內容\n
        model: str, model name 模型名稱
        '''
        if prompt == '':
            self.status_signal.emit(1, 'No prompt. Nothing to do.')
            self.finished_signal.emit(True)
            return
        if model == '':
            self.status_signal.emit(-1, 'No model selected.')
            self.finished_signal.emit(True)
            return        
        self.messages.append({'role': 'user', 'content':f'{prompt}'}) #加入 user 提問
        self.lastPrompt = prompt
        self.model = model
        self.started = False #開始回應

        self.finished_signal.emit(False)        
        self.start()

    def run(self):
        try:
            self.status_signal.emit(0, f'載入模型{self.model}')
            #self.finished_signal.emit(False)
            stream = oChat(
                model=self.model,
                messages=self.messages,
                stream=True,
                )
            self.status_signal.emit(0, f'分析提問...')
            self.messages_signal.emit(f'提問: {self.lastPrompt}\n\n')
            response = ''
            for chunk in stream:
                if not self.started:
                    self.started = True
                    self.status_signal.emit(0, f'分析完成，串流回應中...({self.breakShortcut} 中斷)')
                #print(chunk['message']['content'], end='', flush=True)
                self.messages_signal.emit(chunk['message']['content'])
                response = f"{response}{chunk['message']['content']}"
                if self.breakMesage:
                    self.breakMesage = False
                    self.messages_signal.emit('<break/>')
                    break
            self.messages.append({'role': 'assistant', 'content':f'{response}'}) # 加入 AI 回覆內容
            self.messages_signal.emit('\n\n')
            self.status_signal.emit(0, '')
            self.finished_signal.emit(True)
        except Exception as e:
            self.status_signal.emit(-1, str(e))
            self.finished_signal.emit(True)

def modelList():
        '''列出本地端 Ollama 模型名稱
        '''
        try:
            response = list()
            modelNames = []
            for model in response.models:
                modelNames.append(str(model.model))
            modelNames.sort()
            return True, modelNames
        except Exception as e:
            return False, [f'{str(e)}']