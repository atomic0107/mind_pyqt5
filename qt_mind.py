import json
import pprint
import sys
import collections as cl
from PyQt5.QtWidgets import *
#from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QToolTip, QPushButton, QApplication)
from PyQt5.QtCore import *
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import *
#from PyQt5.QtGui import QFont

#dic = cl.OrderedDict()
dic = {}

class QExtPushButton(QPushButton):#QPushButton
    doubleClicked = pyqtSignal()
    clicked = pyqtSignal()
#    def __init__(self, title, parent):
#        super().__init__(title, parent)
    def __init__(self, *args, **kwargs):
        QPushButton.__init__(self, *args, **kwargs)
        self.initUI()
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.clicked.emit)
        super().clicked.connect(self.checkDoubleClick)

    def initUI(self):
        self.clicked.connect(self.click)# Quitボタンをクリックしたら画面を閉じる
        self.doubleClicked.connect(self.dclick)

    def click(self):
        print("click!!")
        QCoreApplication.instance().quit
    
    def dclick(self):
        print("double click!!")
        #QCoreApplication.instance().quit
     
    @pyqtSlot()
    def checkDoubleClick(self):
        if self.timer.isActive():
            self.doubleClicked.emit()
            self.timer.stop()
        else:
            self.timer.start(250)

class EditWidget(QWidget):
    

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #self.resize(250, 150)
        #self.move(300, 300)
        #self.setWindowTitle('mindmap') 
        
        QToolTip.setFont(QFont('SansSerif', 10))# 10pxのサンセリフフォントを吹き出しに使う
        self.setToolTip('This is a <b>QWidget</b> widget')# 画面の吹き出し設定
        self.setGeometry(300, 100, 300, 700)#setGeometry(ウインド位置x,ウインド位置y,横幅,高さ)
        self.setWindowTitle('mindmap')
        self.set_qbtn()
        self.set_qbtn_noline("key")
        #self.write_text()
        self.show()

    def set_qbtn(self):
        global dic
        keys = {}
        qbtn = QExtPushButton( 'Quit', self )# ボタン作成
        qbtn.setToolTip( 'This is a <b>QPushButton</b> widget' )# ボタンの吹き出し設定
        qbtn.clicked.connect( QCoreApplication.instance().quit )# Quitボタンをクリックしたら画面を閉じる
        qbtn.resize( qbtn.sizeHint() )# ボタンのサイズをいい感じに自動設定
        qbtn.move( 50, 50 )# ボタンの位置設定
        pprint.pprint(dic)
        print("dic print!!")
        keys = dic["0"].keys()
        keys_len = len(keys)
        print("key len = " + str(keys_len))
        i = 0
        for dic_key in dic["0"]["child"].keys():
            i += 1
            #print(dic["root"][dic_key]["parent"])
            text = dic["0"]["child"][dic_key]["parent"]
            qbtn = QExtPushButton( text, self )# ボタン作成
            qbtn.move( 50, 50 + i*20 )# ボタンの位置設定


    def set_qbtn_noline(self,text):
        qbtn = QPushButton( text, self )# ボタン作り
        qbtn.setFlat(True)# 枠線
        qbtn.setToolTip( 'This is a <b>QPushButton</b> widget' )# ボタンの吹き出し設定
        qbtn.clicked.connect( QCoreApplication.instance().quit )# Quitボタンをクリックしたら画面を閉じる
        qbtn.resize( qbtn.sizeHint() )# ボタンのサイズをいい感じに自動設定
        qbtn.move( 50, 150 )# ボタンの位置設定

    def write_text(self):
        qle = QLineEdit(self)# QLineEditオブジェクト作成(テキストボックス)
        self.lbl = QLabel(self)# ラベルオブジェクト作成
        qle.move(60, 100)
        self.lbl.move(60, 40)
        qle.textChanged[str].connect(self.onChanged)
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)# ラベルに入力されたテキストを挿入
        self.lbl.adjustSize() # 入力されたテキストによって、ラベルの長さを調整       

class Mind():
    
    #mind_dic = dic
    def __init__(self):
        global dic
        f = open("mind.json", 'r')
        dic = json.load(f) #JSON形式で読み込む
        f.close()
        print("print read json!")
        pprint.pprint(dic)
        self.mind_dic = dic

        """
        for i in range(3):
            self.mind_dic.setdefault("root",{})
            key = input()
            self.mind_dic["root"].setdefault(key,{})
            self.mind_dic["root"][key].setdefault("parent",key)
            self.mind_dic["root"][key].setdefault("child",{})
        #ファイル書き込み
        f = open('mind.json','w')
        json.dump(self.mind_dic,f,indent=4)
        f.close
        """

    def mind_print(self):
        print("hello my mind world!!")
        pprint.pprint(self.mind_dic)
        print(len(self.mind_dic))

if __name__ == "__main__":

    mind = Mind()
    mind.mind_print()

    app = QApplication(sys.argv)
    ex = EditWidget()
    sys.exit(app.exec_())


