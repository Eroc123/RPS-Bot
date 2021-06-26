from random import randint
from os import system
from time import sleep

# 0 rock
# 1 paper
# 2 scissors
w = ['rock','paper', 'scissor']
system('clear')
aiwin = 0
playerwin = 0
p = {
0 : 'rock',
1 : 'paper',
2 : 'scissor'
}
log = {
'in' : [0],
'result' : [1],
'ch' : [1]
}
win = [[1,0],[0,2],[2,1]]
lose = [[0,1],[2,0],[1,2]]
tie = [[1,1],[2,2],[0,0]]
def main(rt):
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
        return 2
def getinput():
    inpt = input('rock, paper or scissor\n')
    if inpt in w:
        return inpt
    else:
        print('Unknown input, exiting..')
        exit()
d
while True:
    choice = rps(getinput())

    aichoicec = randint(0,5)
    if len(log['in']) > 5:
        if log['in'][-1] == log['in'][-2]:
            if log['in'][-1] == log['in'][-4] and log['in'][-2] == log['in'][-5]:
                if log['in'][-3] == 0:
                    aichoice = 1
                elif log['in'][-3] == 1:
                    aichoice = 2
                elif log['in'][-3] == 2:
                    aichoice = 0
            elif log['in'][-2] == log['in'][-3] == log['in'][-4]:
                if log['in'][-1] == 0:
                    aichoice = 1
                elif log['in'][-1] == 1:
                    aichoice = 2
                elif log['in'][-1] == 2:
                    aichoice = 0
            elif log['in'][-3] == log['in'][-4]:
                if log['in'][-4] == 0:
                    aichoice = 1
                elif log['in'][-4] == 1:
                    aichoice = 2
                elif log['in'][-4] == 2:
                    aichoice = 0
            elif randint(0,8) == 8:
                if log['in'][-1] == 0:
                    aichoice = 1
                elif log['in'][-1] == 1:
                    aichoice = 2
                elif log['in'][-1] == 2:
                    aichoice = 0
            elif aichoicec >= 4 and aichoicec <= 5:
                a = log['in'][-1]
                j = 0
                h = 0
                ilist = []
                while j < len(log['in'])-1:
                    if log['in'][j] == a:
                        ilist.append([log['in'][j],log['in'][j+1]])
                    j += 1
                try:
                    aichoice = max(ilist)[1]
                except:
                    aichoice = ilist[0]

            elif aichoicec == 3:
                if log['in'][-1] == 0:
                    aichoice = 1
                elif log['in'][-1] == 1:
                    aichoice = 2
                elif log['in'][-1] == 2:
                    aichoice = 0
            elif log['in'][-1] == log['in'][-3] and log['in'][-2] == log['in'][-4]:
                if log['in'][-2] == 0:
                    aichoice = 1
                elif log['in'][-2] == 1:
                    aichoice = 2
                elif log['in'][-2] == 2:
                    aichoice = 0
            elif log['in'][-1] == log['in'][-4] and log['in'][-2] == log['in'][-5]:
                if log['in'][-3] == 0:
                    aichoice = 1
                elif log['in'][-3] == 1:
                    aichoice = 2
                elif log['in'][-3] == 2:
                    aichoice = 0
            elif log['in'][-1] == log['in'][-3] and randint(0,6) == 1:
                if log['in'][-2] == 0:
                    aichoice = 1
                elif log['in'][-2] == 1:
                    aichoice = 2
                elif log['in'][-2] == 2:
                    aichoice = 0

            elif aichoicec >= 0 and aichoicec <= 2:
                i = randint(0,3)
                if i == 3:
                    if log['result'][-1] == 0:
                        if log['in'][-1] == 0:
                            aichoice = 2
                        elif log['in'][-1] == 1:
                            aichoice = 0
                        elif log['in'][-1] == 2:
                            aichoice = 1
                    elif log['result'][-1] == 1:
                        if log['in'][-1] == 0:
                            aichoice = 1
                        elif log['in'][-1] == 1:
                            aichoice = 2
                        elif log['in'][-1] == 2:
                            aichoice = 0
                    elif log['result'][-1] == -1:
                        if log['in'][-1] == 0:
                            aichoice = 0
                        elif log['in'][-1] == 1:
                            aichoice = 1
                        elif log['in'][-1] == 2:
                            aichoice = 2
                elif i == 2:
                    if log['in'][-1] == log['in'][-2]:
                        if log['in'][-1] == 0:
                            aichoice = 1
                        elif log['in'][-1] == 1:
                            aichoice = 2
                        elif log['in'][-1] == 2:
                            aichoice = 0
                else:
                    aichoice = max(log['in'])
    else:
        i = randint(0,1)
        if i == 1:
            if log['result'][-1] == 0:
                if log['in'][-1] == 0:
                    aichoice = 2
                elif log['in'][-1] == 1:
                    aichoice = 0
                elif log['in'][-1] == 2:
                    aichoice = 1
            elif log['result'][-1] == 1:
                if log['in'][-1] == 0:
                    aichoice = 1
                elif log['in'][-1] == 1:
                    aichoice = 2
                elif log['in'][-1] == 2:
                    aichoice = 0
            elif log['result'][-1] == -1:
                if log['in'][-1] == 0:
                    aichoice = 0
                elif log['in'][-1] == 1:
                    aichoice = 1
                elif log['in'][-1] == 2:
                    aichoice = 2
        aichoice = randint(0,2)

    result = main([choice, aichoice])
    log['ch'].append(aichoice)
    log['result'].append(result)
    log['in'].append(choice)
    if result == -1:
        aiwin += 1
    if result == 1:
        playerwin += 1
    print(str(playerwin)+ " - " + str(aiwin))
    print('Player Choice : {}\nAI Choice : {}'.format(p[choice], p[aichoice]))
    sleep(1)
    system('clear')
    print(str(playerwin)+ " - " + str(aiwin))
    print('Player Choice : {}\nAI Choice : {}'.format(p[choice], p[aichoice]))
