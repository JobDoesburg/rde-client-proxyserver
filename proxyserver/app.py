from secrets import token_urlsafe

from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__)
app.config['SOCK_SERVER_OPTIONS'] = {'ping_interval': 25}
sock = Sock(app, )

connections = {}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/open")
def open_new_socket():
    # TODO authenticate this route
    new_token = token_urlsafe(32)
    while new_token in connections:
        new_token = token_urlsafe(32)
    connections[new_token] = []
    return new_token


@sock.route("/socket/<token>")
def echo(s, token):
    if token not in connections.keys():
        return

    connections[token].append(s) # TODO only allow 2 connections per token

    while True:
        data = s.receive() # TODO handle disconnects, timeouts, etc.
        # TODO
        for socket in connections[token]:
            if socket != s:
                socket.send(data)


# TODO: close sockets and clear connections[token]

if __name__ == "__main__":
    app.run()
