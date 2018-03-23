
from flask import Flask,request,render_template,send_from_directory
from flask_socketio import SocketIO, emit
from flask_jsonpify import jsonpify
import threading,webbrowser
import json
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
            time.sleep(3)
            self.agent.move()
            socketio.emit('message',json.dumps(agent.getPos()),namespace='/test')
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
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template('WABM02.html')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/getupdate', methods=['GET'])
def getUpdate():
    print("GET")
    return  jsonpify(agent.getPos())


@socketio.on('connect', namespace='/test')
def test_connect():
    print("here")
    emit('message', {'data': 'Connected'})


        
if __name__ == "__main__":
    agent = Agent(0,0)
    thread1 = AgentThread(agent)
    thread1.start()
    #webbrowser.open("http://192.168.0.17:5000")
    #app.run( port=5000,debug=True)
    socketio.run(app,host='0.0.0.0',port=5000,debug=True)
    
