import os
import webbrowser
import swim_utils
import hfpy_utils

from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True


@app.get("/", methods=["GET"])
def dropdown():
    colours = ["Red", "Blue", "Black", "Orange"]
    return render_template("test.html", colours=colours)


if __name__ == "__main__":
    app.run()
