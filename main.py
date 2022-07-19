from flask import *
import threading 
import time


def FlaskServer():
  
  app = Flask(__name__)
  
  @app.route('/')
  def index():
      return r'This is the broadcast station of PowerUI TV. This station currently doesn`t have a site.'
  @app.route("/broadcastData")
  def getBroadcastData():
    with open("broadcastData", "r") as f:
      return f.read()
    f.close()
  @app.route("/broadcastDescription")
  def getBroadcastDescription():
    with open("broadcastDescription", "r") as f:
      return f.read()
    f.close()
  @app.route("/broadcast")
  def sendBroadcast():
    return send_file("broadcast.mp4")
  
  app.run(host='0.0.0.0', port=81)

def UpdateBroadcastData():
  currentData = 0
  while True:
    currentData += 1
    with open("broadcastData", "w") as f:
      f.write(str(currentData))
    f.close()
    print(str(currentData))
    time.sleep(1)

server = threading.Thread(target=FlaskServer, daemon=True)
server.start()
client = threading.Thread(target=UpdateBroadcastData)
client.start()
client.join()
