class Ai():
    def __init__(self):
        self.logging = {
        'ai':[],
        'player':[],
        'result':[]
        }
        self.whenResult = {
        0:[],
        1:[],
        -1:[]
        }
        self.whenAiMove = {
        0:[],
        1:[],
        -1:[]
        }
        self.chanceOfRepete = 0.5
        self.repetition = 0
        self.mostCommonMove = 0
        self.changeGesture = {
        'RR':0,
        'RP':0,
        'RS':0,
        'PR':0,
        'PP':0,
        'PS':0,
        'SR':0,
        'SP':0,
        'SS':0
        }
        self.int2str = {
        0:'R',
        1:'P',
        -1:'S'
        }
        self.str2int = {
        'R':0,
        'P':1,
        'S':-1
        }
    def translate(move):
        if type(move) == type(0):
            return self.str2int[move]
        elif type(move) == type('R'):
            return self.int2str[move]
    def log(self, aimove, pmove, result):
        self.logging['ai'].append(aimove)
        self.logging['player'].append(pmove)
        self.logging['result'].append(result)
        self.updateModel()
    def updateModel(self):
        self.whenResult[self.logging['result'][-2]].append(self.logging['player'][-1])
        self.whenAiMove[self.logging['ai'][-2]].append(self.logging['player'][-1])
        if self.logging['player'][-1] == self.logging['player'][-2]:
            self.repetition += 1
        self.chanceOfRepete = len(self.logging['player'])/self.repetition
        self.mostCommonMove = max(self.logging['player'])
        l1 = self.translate(self.logging['player'][-1])
        l2 = self.translate(self.logging['player'][-2])
        self.changeGesture[l1+l2] + 1
    def predict(self):
        prediction = {
        0:0
        1:0
        -1:0
        }
        largesti = 0
        for keys in self.changeGesture:
            if self.changeGesture[keys] == largesti:
                predict1tmp = largesti
                predict1keytmp = keys
            elif self.changeGesture[keys] > largesti:
                predict1 = keys
        if predict1tmp == largesti:
            prediction[predict1keytmp] = 0.5
            prediction[keys] = 0.5
