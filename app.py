from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
    return "Welcome to MRECW"
@app.route("/home")
def home():
    return "homepage"
if __name__=="main_":
    app.run(host='0.0.0.0',port=10000)