# Team Vengeful Mice: Raymond Yeung and Jesse Xie
# SoftDev pd2
# K19 -- A RESTful Journey Skyward
# 2021-11-23

from flask import Flask, render_template
import json
import urllib

app = Flask(__name__)

@app.route("/")
def main():
    f = open("key_nasa.txt")
    key = f.read()
    # read key from file
    data = urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=' + (key))
    response = data.read()
    response_info = json.loads(response)
    # load into dictionary
    picture = response_info['url']
    explanation = response_info['explanation']
    return render_template('main.html', picture = picture, explanation = explanation)

if __name__ == "__main__":
    app.debug = True
    app.run()
