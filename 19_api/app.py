# Team Vengeful Mice: Raymond Yeung and Jesse Xie
# SoftDev pd2
# K19 -- A RESTful Journey Skyward
# 2021-11-23

from flask import Flask, render_template
import json
import urllib

app = Flask(__name__)

@app.route("/")
def test():
    data = urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=W4wJIqBrRcjVnc4PPIP6FJ8l64Jc1ecLi4Ye7dU4')
    response = data.read()
    response_info = json.loads(response)
    picture = response_info['url']
    return render_template('main.html', picture = picture)

if __name__ == "__main__":
    app.debug = True
    app.run()
