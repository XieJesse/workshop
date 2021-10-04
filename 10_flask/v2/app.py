# Team Polar: Yuqing Wu, Jesse Xie, Rachel Xiao
# SoftDev
# K10 -- Putting Little Pieces Together
# 2021-10-04

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.run()

# predictions:
# Print two lines in terminal, first line "about to print __name__", second line prints "__main__".
# Returns No hablo queso! to the home directory of website.

#result:
# After loading the website, behave same as prediction.
