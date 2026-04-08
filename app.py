from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage (replace later with database)
users = []
posts = []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Get user data
        username = request.form.get("username")
        email = request.form.get("email")
        neighborhood = request.form.get("neighborhood")

        # Get dog data
        dog_name = request.form.get("dog_name")
        dog_breed = request.form.get("dog_breed")

        # Store it (temporary)
        user = {
            "username": username,
            "email": email,
            "neighborhood": neighborhood,
            "dog": {
                "name": dog_name,
                "breed": dog_breed
            }
        }

        users.append(user)

        return redirect(url_for("success"))

    return render_template("register.html")

@app.route("/success")
def success():
    return "<h2>Registration successful!</h2>"

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/board", methods=["GET", "POST"])
def board():
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        neighborhood = request.form.get("neighborhood")
        time = request.form.get("time")
        post_type = request.form.get("type")

        post = {
            "title": title,
            "description": description,
            "neighborhood": neighborhood,
            "time": time,
            "type": post_type
        }

        posts.append(post)

    return render_template("board.html", posts=posts)

@app.route("/community")
def community():
    return "<h2>Community (coming soon)</h2>"

@app.route("/search")
def search():
    return "<h2>Search (coming soon)</h2>"

@app.route("/profile")
def profile():
    return "<h2>My Profile (coming soon)</h2>"

@app.route("/tokens")
def tokens():
    return "<h2>Tokens system (coming soon)</h2>"

if __name__ == "__main__":
    app.run(debug=True)
