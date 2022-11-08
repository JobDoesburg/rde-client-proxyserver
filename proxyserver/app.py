from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

connections = {}

@app.route('/')
def index():
    return render_template('index.html')

@sock.route('/socket/<token>')
def echo(s, token):
    if token not in connections:
        connections[token] = []
    connections[token].append(s)
    while True:
        data = s.receive()
        for socket in connections[token]:
            if socket != s:
                socket.send(data)


if __name__ == '__main__':
    app.run()
