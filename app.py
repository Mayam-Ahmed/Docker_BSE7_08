from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>BSE7-08 Docker Application</h1><p>My Docker container is running successfully!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)