
from flask import Flask,request,render_template,send_from_directory
from flask_jsonpify import jsonpify
import threading
import time
from random import randint


class AgentThread (threading.Thread):
    def __init__(self, agent):
        threading.Thread.__init__(self)
        self.agent = agent
        self.counter = 0
    
    def run(self):
        self.iterate()
        print("done #2")
            
            
    def iterate(self):
        while self.agent.run:
            time.sleep(0.5)
            self.agent.move()
            self.counter+=1


class Agent:
    agentCount = 0
    run = True

    def __init__(self, xPos,yPos):
        self.xPos =xPos 
        self.yPos =yPos 
        Agent.agentCount+=1
        
   
    def move(self):
        self.xPos+=randint(-1, 1)
        self.yPos+=randint(-1, 1)
     
    def getPos(self):
        return(self.xPos,self.yPos)
        


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('WABM.html')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/getupdate', methods=['GET'])
def getUpdate():
    return  jsonpify(agent.getPos())

        
if __name__ == "__main__":
    agent = Agent(0,0)
    thread1 = AgentThread(agent)
    thread1.start()

    app.run(host='0.0.0.0', port=5000,debug=True)
