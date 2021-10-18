# Team threeCoffeePeanuts: Jesse Xie, Yaying Liang Li, Ryan Wang
#SoftDev
#K15 -- Sessions Greetings
#2021-10-18


from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
Some will work as written; other sections will not. Can you predict which?
Devise some simple tests you can run to "take apart this engine," as it were.
Execute your tests. Process results.
PROTIP: Insert your own in-line comments wherever they will help your future self and/or current teammates understand what is going on.
'''

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    '''
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app) #<Flask 'app'>
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    #empty dict cuz user hasn't submitted anything yet

    #request.args['username'] doesn't exist yet, cuz user didn't submit username yet
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    '''
    '''
        form prompts user to enter username in webpage;
        <name="username"> saves the user's inputted name under the key "username" in the ImmutableMultiDict
        <form action="/auth"> after user submits, takes the user to <host>/auth?username=...
    '''
    return render_template( 'login.html' )


@app.route("/auth") # , methods=['GET', 'POST'])
def authenticate():
    actualUsername = "threeCoffeePeanuts"
    actualpassword = "oneWalnutLatte"
    username = request.args['username'] #access value of key 'username' in Dict
    password = request.args['password'] #access value of key 'username' in Dict
    '''
        use response.html as template
        method (called in response.html) is actually the request.method (which is get)
        username (called in response.html) is actually username (from this python file)
    '''
    if (username == actualUsername) and (password == actualpassword):
        return render_template('response.html', method=request.method, username=username, password = password)  #response to a form submission
    else:
        return render_template( 'login.html' )

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
