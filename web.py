from flask import Flask, request, redirect

app = Flask(__name__)

posts = []

# Home route (prevents "broken" root)
@app.route("/")
def home():
    return '<h2>Server running</h2><a href="/blog">Go to Blog</a>'

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

@app.route("/blog")
def blog():
    html = "<h1>Vintage Blog</h1><a href='/add'>+ Add New</a><hr>"

    for post in posts:
        html += f"""
        <div style='margin-bottom:30px'>
            <h2>{post['title']}</h2>
            <img src='{post['image']}' width='100%'>
            <p>{post['content']}</p>
            <hr>
        </div>
        """

    return html

import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))