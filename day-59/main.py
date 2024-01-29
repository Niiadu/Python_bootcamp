from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    response = requests.get("https://api.npoint.io/25ed92c90bc8e724b31f")
    api_data = response.json()
    return render_template("index.html", data=api_data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<num>")
def post(num):
    response = requests.get("https://api.npoint.io/25ed92c90bc8e724b31f")
    api_data = response.json()
    print(api_data)
    return render_template("post.html", number=num, data=api_data)


if __name__ == "__main__":
    app.run(debug=True)

