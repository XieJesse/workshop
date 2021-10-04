# Team Polar: Yuqing Wu, Jesse Xie, Rachel Xiao
# SoftDev
# K10 -- Putting Little Pieces Together
# 2021-10-04

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    pri(__name__)   #where will this go?
    return "No hablo queso!"


app.debug = False
app.run()

# Predictions:
# Turn debug mode to on in the terminal. Prints debug information in the terminal.
# Print two lines in terminal, first line "about to print __name__", second line
# prints "__main__".
# Returns No hablo queso! to the home directory of website.

#Results:
# * Debug mode: on
# * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
# * Restarting with stat
# * Debugger is active!
# * Debugger PIN: 429-585-123
# about to print __name__...
# __main__
# 127.0.0.1 - - [04/Oct/2021 09:13:02] "GET / HTTP/1.1" 200 -
# * Detected change in '/Users/yuqingwu/softdev/workshop/10_flask/v3/app.py', reloading
# * Restarting with stat
# * Debugger is active!
# * Debugger PIN: 429-585-123
# As we change the file, the debugger in the terminal detects a change and remind us after we save.


# When there's an error in the code that's run, with a debugger,
# it would specify the error on the website and gives more information
# about the error with the Werkzeug powered traceback interpreter.
# In the terminal, the error is also printed with the line of the error and the error.
# The traceback is also printed.
# pri(__name__)   #where will this go?
# NameError: name 'pri' is not defined

# Without a debugger, the website only shows internal server error.
