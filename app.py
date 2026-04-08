from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage (replace later with database)
users = []

@app.route("/")
def home():
    return redirect(url_for("register"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Get user data
        username = request.form.get("username")
        email = request.form.get("email")

        # Get dog data
        dog_name = request.form.get("dog_name")
        dog_breed = request.form.get("dog_breed")

        # Store it (temporary)
        user = {
            "username": username,
            "email": email,
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

if __name__ == "__main__":
    app.run(debug=True)