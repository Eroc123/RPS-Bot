from random import randint
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
    def translate(self, move):
        if type(move) == type('R'):
            return self.str2int[move]
        elif type(move) == type(0):
            return self.int2str[move]
    def log(self, aimove, pmove, result):
        self.logging['ai'].append(aimove)
        self.logging['player'].append(pmove)
        self.logging['result'].append(result)
        self.updateModel()
    def updateModel(self):
        if len(self.logging['player']) <= 2:
            return
        self.whenResult[self.logging['result'][-2]].append(self.logging['player'][-1])
        self.whenAiMove[self.logging['ai'][-2]].append(self.logging['player'][-1])
        if self.logging['player'][-1] == self.logging['player'][-2]:
            self.repetition += 1
        try:
            self.chanceOfRepete = len(self.logging['player'])/self.repetition
        except:
            self.chanceOfRepete = 0
        self.mostCommonMove = max(self.logging['player'])
        l1 = self.translate(self.logging['player'][-1])
        l2 = self.translate(self.logging['player'][-2])
        self.changeGesture[l1+l2] + 1
    def predict(self):
        if len(self.logging['player']) <= 3:
            return randint(-1,1)
        lose = {
        0 : 1,
        1 : -1,
        -1 : 0
        }
        prediction = {
        0:0,
        1:0,
        -1:0
        }

        #most common gesture after the last gesture
        largesti = 0
        for keys in self.changeGesture:
            if self.changeGesture[keys] == largesti:
                predict1tmp = largesti
                predict1keytmp = keys
            elif self.changeGesture[keys] > largesti:
                predict1 = keys
        if predict1tmp == largesti:
            prediction[self.translate(list(predict1keytmp)[1])] += 0.5
            prediction[self.translate(list(keys)[1])] += 0.5
        else:
            prediction[self.translate(list(keys)[1])] += 1
        print(prediction)
        #most common gesture
        prediction[max(self.logging['player'])] += 0.5

        if self.chanceOfRepete >= 0.75:
            prediction[self.logging['player'][-1]] += 1.5
        elif self.chanceOfRepete >= 0.5:
            prediction[self.logging['player'][-1]] += 0.5
        result = 0
        for i in prediction:
            imax = prediction[i]
            if imax > result:
                result = imax
                resultkeys = i
            else:
                resultkeys = i
        print(prediction, resultkeys)
        return lose[resultkeys]
