from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit


app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')
socketio = SocketIO(app, cors_allowed_origins
                    ='*')

    
@socketio.on("connect")
def connected():
    print(request.sid)
    print("client has connected")
    emit('connect', {"data":f"id:{request.sid} is connected"})


@socketio.on('message')
def handle_message(message):
    print("Receive Message: "+ message)
    if message != "User connected!":
        print(message)
        emit('message',{"data":message})

@socketio.on("disconnect")
def disconnected():
    """event listener when client disconnects to the server"""
    print("user disconnected")
    emit("disconnect",f"user {request.sid} disconnected",broadcast=True)
if __name__ == '__main__':

    socketio.run(app, debug=True, )