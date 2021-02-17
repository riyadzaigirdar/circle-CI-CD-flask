from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Riyad did CI/CD Alhamdulillah Alhamdulillah"

if __name__ == "__main__":
    app.run()