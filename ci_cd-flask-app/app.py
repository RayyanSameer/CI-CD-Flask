from flask import Flask
app = Flask(__name__)

@app.route("/healthz")
def healthz():
    return "OK"

@app.route("/")
def home():
    return """This is a modded peice <br>


     "Here is another statement <br>


     "I am doing this to test if my 
     
     changes are being reflected live <br>


     "it works ! <br>



     Here is a second addition :) <br>



     "Changes are live , check logs """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
