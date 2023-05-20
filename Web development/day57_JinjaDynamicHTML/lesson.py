from flask import Flask, render_template
import requests
app = Flask(__name__)


@app.route('/guess/<string:name>')
def home(name):
    param = {"name":name}
    response =  requests.get("https://api.genderize.io", params = param)
    response.raise_for_status()
    data = response.json()
    gender = data["gender"]
    response_age = requests.get("https://api.agify.io", params = param)
    response_age.raise_for_status()
    age = response_age.json()["age"]
    return render_template("lesson.html", your_name = name, guessed_gender = gender, guessed_age = age)


@app.route('/blog/animals/')
def plush_toys():
    response = requests.get("https://api.npoint.io/39b372afb2c0c75fdf6c")
    data = response.json()
    return render_template("blog.html", blog_posts = data)

if __name__ == "__main__":
    app.run(debug = True)