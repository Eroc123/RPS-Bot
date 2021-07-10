from random import randint
from time import sleep
from cogs import Ai
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QLabel
from PyQt5.QtCore import pyqtSlot
import sys
# 0 rock
# 1 paper
# 2 scissors
w = ['rock','paper', 'scissor']
aiwin = 0
playerwin = 0
p = {
0 : 'rock',
1 : 'paper',
-1 : 'scissor'
}
log = {
'in' : [0],
'result' : [1],
'ch' : [1]
}
win = [[1,0],[0,-1],[-1,1]]
lose = [[0,1],[-1,0],[1,-1]]
tie = [[1,1],[-1,-1],[0,0]]
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.title = 'RPS AI bot - https://github.com/Eroc123'
        self.initVar()
        self.initUI()
    def initVar(self):
        self.c = Ai()
        self.aiwin = 0
        self.playerwin = 0
        self.w = ['rock','paper', 'scissor']
        self.aiwin = 0
        self.playerwin = 0
        self.p = {
        0 : 'rock',
        1 : 'paper',
        -1 : 'scissor'
        }
        self.log = {
        'in' : [0],
        'result' : [1],
        'ch' : [1]
        }
        self.win = [[1,0],[0,-1],[-1,1]]
        self.lose = [[0,1],[-1,0],[1,-1]]
        self.tie = [[1,1],[-1,-1],[0,0]]
        self.scores = 'YOU : {} AI : {}'.format(self.playerwin, self.aiwin)
    def initUI(self):
        self.setWindowTitle(self.title)
        button1 = QPushButton('Rock', self)
        button1.setToolTip('Throw Rock against the AI')
        button1.clicked.connect(self.rock)
        button1.move(50,100)
        button2 = QPushButton('Paper', self)
        button2.setToolTip('Throw Paper against the AI')
        button2.clicked.connect(self.paper)
        button2.move(150,100)
        button3 = QPushButton('Scissor', self)
        button3.setToolTip('Throw Scissor against the AI')
        button3.clicked.connect(self.rock)
        button3.move(250,100)
        self.scoreLabel = QLabel(self.scores, self)
        self.scoreLabel.move(150, 50)
        self.show()
    @pyqtSlot()
    def rock(self):
        self.pchoice = 0
        self.get_result()
    @pyqtSlot()
    def paper(self):
        self.pchoice = 1
        self.get_result()
    @pyqtSlot()
    def scissor(self):
        self.pchoice = -1
        self.get_result()
    def get_result(self):
        self.aichoice = self.c.predict()
        self.result = check([self.pchoice, self.aichoice])
        self.c.log(self.aichoice, self.pchoice, self.result)
        if self.result == -1:
            self.aiwin += 1
        if self.result == 1:
            self.playerwin += 1
        self.update_result()
    def update_result(self):
        self.scores = 'YOU : {} AI : {}'.format(self.playerwin, self.aiwin)
        self.scoreLabel.setText(self.scores)
def check(rt):
    if rt in win:
        return 1
    elif rt in lose:
        return -1
    elif rt in tie:
        return 0
def rps(input):
    if input == 'rock':
        return 0
    elif input == 'paper':
        return 1
    elif input == 'scissor':
        return -1
def getinput():
    inpt = input('rock, paper or scissor\n')
    if inpt in w:
        return inpt
    else:
        print('Unknown input, exiting..')
        exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
