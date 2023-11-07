from flask import Flask  # From module import Class

app = Flask(__name__)

@app.get("/hello")
def hello():
        return "Hello from my first web app!"




if __name__  == "__main__":
        app.run() #Starts a local webserver, and waits.... forever.
