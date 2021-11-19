from pathlib import Path
from flask import Flask, render_template, request, render_template_string
import os
app = Flask(__name__)


@app.route('/')
def Home():
    FILENAME = os.listdir()
    return render_template("index.html", FILENAME=FILENAME, request=request, os=os)


@app.route('/view')
def view():
    filename = request.args.get('file')
    if os.path.isfile(filename):
        try:
            with open(filename) as f:
                in_text = f.read()
                No_of_lines = len(in_text.split("\n"))
                return render_template("display.html", in_text=in_text, os=os, No_of_lines=No_of_lines)
        except:
            return render_template("display.html", in_text=None, request=request, os=os)
    elif os.path.isdir(filename):
        FILENAME = os.listdir(filename)
        return render_template("folder.html", FILENAME=FILENAME, request=request, os=os)


app.run(port=5000,host='0.0.0.0',
        debug=True)
