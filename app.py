from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/pies")
def pies():
    return render_template("pies.html")   

@app.route("/order")
def order():
    return render_template("order.html")   

@app.route("/applepie")
def applepies():
    return render_template("applepie.html")  

@app.route("/seasonalpies")
def seasonalpies():
    return render_template("seasonalpies.html")  

if __name__== "__main__":
    app.run(debug=True) 