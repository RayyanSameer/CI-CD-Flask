from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    print("This is a modded peice")
    print("Here is another statement ")
    print("I am doing this to test if my changes are being reflected live")
    print("it works !")

    return "Changes are live , check logs "


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
