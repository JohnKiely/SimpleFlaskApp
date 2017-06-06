from flask import Flask, render_template

app=Flask(__name__)
app.config["SECRET_KEY"] = "F34TF$($e34D";

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/index/")
def index():
    return render_template("index.html", index=index)

if __name__== "__main__":
    app.run(host="0.0.0.0", port=2000)
