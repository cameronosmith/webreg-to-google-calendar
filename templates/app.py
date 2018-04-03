#!flask/bin/python

from flask import Flask, render_template, request
import json
import pythonScripts.main 


application = app = Flask(__name__)

@app.route("/")
def output():
    return render_template("index.html", name="Joe")

@app.route('/receiver',methods=['POST'])
def worker():
    credentials = json.loads(request.form.keys()[0])#parse the stringified json
    username = credentials['username']
    password = credentials['password']
    print 'about to get the user schedule ipnut'
    eventsDataAsString = json.dumps(pythonScripts.main.run(username,password))
    print 'we got the credentials'
    return eventsDataAsString

if __name__ == "__main__":
    app.run()
