from os import system
from os import environ
from bin import app

if __name__ == "__main__":
    HOST = environ.get("SERVER_HOST","localhost")
    try:
        PORT = int(environ.get("SERVER_HOST","localhost"))
    except ValueError:
        PORT = 5000
    system("start chrome.exe http://127.0.0.1:5000")
    app.run(HOST,PORT)