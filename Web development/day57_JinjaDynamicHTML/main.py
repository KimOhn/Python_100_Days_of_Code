from flask import Flask, render_template
import requests
from post import Post

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
response.raise_for_status()
blog_data = response.json()
blog_objects = []
for post in blog_data:
    post = Post(post["id"], post["title"], post["subtitle"], post["body"])
    blog_objects.append(post)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", blog_posts = blog_data)

@app.route('/<int:num>')
def get_blog(num):
    displayed = None
    for post in blog_objects:
        if post.id == num:
            displayed = post.body
    return render_template("post.html", blog_posts=post.body)


if __name__ == "__main__":
    app.run(debug=True)
