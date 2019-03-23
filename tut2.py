from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/jawad")
def hellojawad():
    return "Hello jawad!"

@app.route("/boot")
def boot():
    return render_template('boot.html')

app.run(debug=True)
