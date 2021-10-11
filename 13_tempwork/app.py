#Team Cheese: Jesse Xie (with Polly), Wen Hao Dong (with Jal Hordan), Justin Zou (with Piggy)
#SoftDev
#K13 -- Template for Success
#2021-10-08

from flask import Flask, render_template
import occupations

app = Flask(__name__)

@app.route("/occupyflaskst")
def main():
    return render_template("tablified.html", occ=occupations.random_occupation(), data=occupations.data)

if __name__ == "__main__":
    app.debug = True
    app.run()
