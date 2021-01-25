from flask import Flask, request, render_template
server = Flask(__name__)

@server.route("/")
def send():
    return render_template("index.html")

if __name__ == "__main__":
   server.run(host='0.0.0.0', port=80) 
