# Import flask and other modules
from flask import Flask, render_template, request, session, redirect, url_for
from datetime import timedelta

# Create an instance of the Flask class
app = Flask(__name__)

# Set a secret key for the session
app.secret_key = "secret"

# Set the session lifetime to 30 minutes
app.permanent_session_lifetime = timedelta(minutes=30)

# Define a route for the home page
@app.route("/")
def home():
    # Check if the user is logged in
    if "user" in session:
        # Get the username from the session
        user = session["user"]
        # Render the home.html template with the username
        return render_template("home.html", user=user)
    else:
        # Render the home.html template without the username
        return render_template("home.html")

# Define a route for the login page
@app.route("/login", methods=["GET", "POST"])
def login():
    # Check if the request method is POST
    if request.method == "POST":
        # Get the username from the form data
        user = request.form["user"]
        # Set the session to permanent
        session.permanent = True
        # Store the username in the session
        session["user"] = user
        # Redirect to the home page
        return redirect(url_for("home"))
    else:
        # Check if the user is already logged in
        if "user" in session:
            # Redirect to the home page
            return redirect(url_for("home"))
        else:
            # Render the login.html template
            return render_template("login.html")

# Define a route for the logout page
@app.route("/logout")
def logout():
    # Check if the user is logged in
    if "user" in session:
        # Pop the username from the session
        user = session.pop("user", None)
        # Render the logout.html template with the username
        return render_template("logout.html", user=user)
    else:
        # Redirect to the home page
        return redirect(url_for("home"))

# Run the app if this file is executed as the main program
if __name__ == "__main__":
    app.run(debug=True)