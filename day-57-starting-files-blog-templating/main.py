from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blog_post = response.json()
    return render_template("index.html", blog=blog_post)


@app.route("/post/<num>")
def get_blog(num):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blog_post = response.json()
    return render_template("post.html", blog=blog_post, page_number=int(num))


if __name__ == "__main__":
    app.run(debug=True)
