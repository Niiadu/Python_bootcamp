from flask import Flask, render_template
import random
import datetime
import requests

# year = datetime.date.today().year

app = Flask(__name__)

@app.route("/")
def home():
    rand_number = random.randint(0,12)
    year = datetime.date.today().year
    return render_template("index.html", num=rand_number, this_year = year)


@app.route("/guess/<name>")
def guess_age(name):
    parameter = {
        "name": name
    }
    response = requests.get("https://api.genderize.io", params=parameter)
    response.raise_for_status()
    gender = response.json()["gender"]

    age_response = requests.get("https://api.agify.io", params=parameter)
    age_response.raise_for_status()
    age = age_response.json()["age"]
    return render_template("gender.html", guess_gender=gender, guess_age=age, guess_name=name.title())

@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    blog_data = response.json()
    return render_template("blog.html", data=blog_data)


if __name__ == "__main__":
    app.run(debug=True)



# blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
# response = requests.get(blog_url)
# for title in response.json():
#     print(title["title"])
#     print(title["subtitle"])