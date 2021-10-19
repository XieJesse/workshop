# Team threeCoffeePeanuts: Jesse Xie, Yaying Liang Li, Ryan Wang
#SoftDev
#K15 -- Sessions Greetings
#2021-10-18


from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import sessions

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():

    return render_template( 'login.html' )


@app.route("/auth") # , methods=['GET', 'POST'])
def authenticate():
    #hard coding single username and password
    logins = {
        "coffee":"peanut"
    }
    username = request.args['username']
    password = request.args['password']

    if (username in logins and logins[username] == password):
        return render_template('response.html', method=request.method, username=username, password = password)
    elif (username in logins and logins[username] != password):
        error = "user exists but wrong password"
        return render_template( 'login.html', error=error)
    else:
        error = "Error: that username does not exist"
        return render_template( 'login.html', error=error)

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
