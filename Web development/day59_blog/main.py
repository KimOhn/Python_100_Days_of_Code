from flask import Flask, render_template, request
import requests
#from blog import Blog

blog_data = requests.get(url = "https://api.npoint.io/2259d7f2dacf28c2ca3c")
blog_data.raise_for_status()
json_data = blog_data.json()

# blog_object = []
# for b in json_data:
#     id = b["id"]
#     title = b["title"]
#     subtitle = b["subtitle"]
#     body = b["body"]
#     b_object = Blog(id, title, subtitle, body)
#     blog_object.append(b_object)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts = json_data)

@app.route('/about')
def call_about():
    return render_template("about.html")


@app.route('/<int:index>')
def get_post(index):
    requested_post = None
    for blog_post in json_data:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", ind_posts = requested_post)
@app.route('/contact', methods = ["GET","POST"])
def contact():
    contact_submit = False
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        contact_submit = True
    return render_template("contact.html", submit_status = contact_submit)
if __name__ == "__main__":
    app.run(debug=True)

