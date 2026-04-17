from flask import Flask, request, redirect
import os
import json

app = Flask(__name__)

try:
    with open("posts.json", "r") as f:
        posts = json.load(f)
except:
    posts = []

# HOME
@app.route("/")
def home():
    return redirect("/user/zara_world_hara")
# PROFILE PAGE
@app.route("/user/<username>")
def profile(username):
    return f"""
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                margin: 0;
                font-family: Georgia, serif;
                background: linear-gradient(rgba(120,0,0,0.6), rgba(60,0,0,0.9)),
                            url('https://images.unsplash.com/photo-1520975922284-9c6a4c0c4b6c');
                background-size: cover;
                color: #f5e6e6;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
            }}

            .card {{
                background: rgba(255,240,240,0.9);
                color: #3b1f1f;
                padding: 25px;
                border-radius: 20px;
                width: 90%;
                max-width: 350px;
                text-align: center;
            }}

            img {{
                width: 100px;
                border-radius: 50%;
                margin-bottom: 10px;
            }}

            .btn {{
                display: block;
                background: #8b0000;
                color: white;
                padding: 10px;
                border-radius: 10px;
                margin-top: 10px;
                text-decoration: none;
            }}
        </style>
    </head>

    <body>
        <div class="card">
            <img src="https://via.placeholder.com/150">
            <h2>@{username}</h2>
            <p>Vintage cinema | timeless frames | old stories</p>

            <a class="btn" href="https://instagram.com/{username}" target="_blank">
                Visit Instagram
            </a>

            <a class="btn" href="/blog">
                Read Blog
            </a>
        </div>
    </body>
    </html>
    """

# ADD BLOG
@app.route("/add", methods=["GET", "POST"])
def add_post():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        image = request.form.get("image")

        if title and content and image:
            posts.append({
                "title": title,
                "content": content,
                "image": image
            })
            if title and content and image:
    posts.append({
        "title": title,
        "content": content,
        "image": image
    })

    with open("posts.json", "w") as f:
        json.dump(posts, f)

        return redirect("/blog")

    return """
    <h2>Add Blog</h2>
    <form method="POST">
        <input name="title" placeholder="Title" required><br><br>
        <input name="image" placeholder="Image URL" required><br><br>
        <textarea name="content" placeholder="Content" required></textarea><br><br>
        <button type="submit">Post</button>
    </form>
    <br>
    <a href="/blog">View Blog</a>
    """

# BLOG PAGE
@app.route("/blog")
def blog():
    html = "<h1>Vintage Blog</h1><a href='/add'>+ Add New</a><hr>"

    for post in posts:
        html += f"""
        <div style='background:white;padding:15px;border-radius:10px;margin:20px'>
            <img src='{post['image']}' style='width:100%;border-radius:10px'>
            <h2>{post['title']}</h2>
            <p>{post['content']}</p>
        </div>
        """

    return html

# RUN
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
