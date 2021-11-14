# RPS-Bot
<p>Rock Paper Scissor AI written in python and PyQt5</p>
<p>This is a true AI in the sense that it does not read your input and use that against you, but it will use your past inputs to learn how to beat you :)</p>


# Requriements 
* PyQt5
* Python (3.x)

# How to use
<p>Download the files
<code>git clone https://github.com/Eroc123/RPS-Bot.git</code></p>

<p>Put them in the same folder</p>
<p>Run <code>python3 main.py</code> in terminal (linux) </p>
<p>Else run <code>py main.py</code> in the terimal (windows)</p>
<p>You need to install PyQt5 is not already installed

  
## You can import cogs.py into your own code

 Some important functions
* predict() get the AI choice
* log(the ai choice, the player choice, the result)

  make sure to use <code>from cog import Ai</code>  
  
  0 : 'rock'  
  1 : 'paper'  
  -1 : 'scissor'  
  for example  
  <code>
    from cogs import Ai
    #the cogs.py does not provide functions to find if its a win or a loss
    win = [[1,0],[0,-1],[-1,1]]
    lose = [[0,1],[-1,0],[1,-1]]
    tie = [[1,1],[-1,-1],[0,0]]
    
    score = 0
    
    def check(rt):
      if rt in win:
          return 1
      elif rt in lose:
          return -1
      elif rt in tie:
          return 0
    
    c = Ai()
    userchoice = input() #here the user input 1, 0, -1
    AIchoice = c.predict()
    score += check([userchoice, AIchoice]) #remember its user choice first, then ai choice
    print(score)
  </code>
    
    
  
