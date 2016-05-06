from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/Biography")
def biography():
    return render_template("bio.html")
    
@app.route("/contact")
def contact():
    return render_template("contact.html")
    
@app.route("/charity")
def charity():
    return render_template("charity.html")
    
if __name__ == '__main__':
    app.debug = True
    port = int(os.getenv('PORT', 8080))
    host = os.getenv('IP', '0.0.0.0')
    app.run(port=port, host=host)