from flask import Flask, render_template
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/home")
def home():
    return "homepage"
if __name__=="main_":
    app.run(host='0.0.0.0',port=10000)