from flask import Flask, render_template
import occupations

app = Flask(__name__)

@app.route("/occupyflaskst")
def main():
    return render_template("tablified.html", occ=occupations.random_occupation(),joblist = occupations.jobs)

if __name__ == "__main__":
    app.debug = True
    app.run()
