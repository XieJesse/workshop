from flask import Flask
import json
import urllib3
app = Flask(__name__)

@app.route("/")
def test():
    data = urllib2.urlopen('https://api.nasa.gov/planetary/apod?api_key=W4wJIqBrRcjVnc4PPIP6FJ8l64Jc1ecLi4Ye7dU4')
    print(data.read())
    response_info = json.loads(data)
    print(response_info)
    print("response_info")
    return "No hablo queso!"

app.run()
