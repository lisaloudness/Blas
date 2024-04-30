import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


def create_app():

    app = CustomFlask(__name__)


app = Flask(__name__)
app.jinja_env.lstrip_blocks = True
app.jinja_env.trim_blocks = True

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# HOME PAGE
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


# SIGN UP--

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if name already exists in a database --
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username").lower()
        password = request.form.get("password")

        # Check if username exists in the database
        existing_user = mongo.db.users.find_one({"username": username})

        if existing_user:
            # Verify submitted password against the hashed password in database
            if check_password_hash(existing_user["password"], password):
                # Store username in session to indicate user is logged in
                session["user"] = username

                # Check if the logged-in user is an admin
                if session["user"].lower() == "admin":
                    # Redirect to admin dashboard
                    return redirect(url_for("admin"))
                else:
                    # Redirect to user profile
                    return redirect(url_for("profile", username=username))
            else:
                # Incorrect password
                flash("Incorrect password. Please try again.", "error")
                return redirect(url_for("login"))
        else:
            # Username doesn't exist
            flash("Username not found. Please check your username.", "error")
            return redirect(url_for("login"))

    # Render the login page for GET requests
    return render_template("login.html")


# Profile
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Ensure the user is logged in
    if 'user' not in session:
        flash("You need to log in first")
        return redirect(url_for("login"))

    # Get the username from the session
    logged_in_user = session["user"]

    # Fetch the user's recipes from the database
    user_recipes = mongo.db.recipes.find({"created_by": logged_in_user})
    # If user has no recipes to display
    if not user_recipes:
        flash("All recipes you add to Blas will display here")

    return render_template(
        "profile.html", username=username, recipes=user_recipes)


# logout
@app.route("/logout")
def logout():
    # remove user from session cookies
    session.pop("user")
    return redirect(url_for("login"))


# Search Recipes
@app.route("/get_recipes", methods=["GET"])
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


# Search Function
@app.route("/search", methods=["GET`", "POST"])
def search():
    if request.method == "POST":
        query = request.form.get("query")
        # Store the query in the session
        session['last_query'] = query
        # Perform the search and get the results
        results = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    else:    # if search is empty retrieve all recipes
        results = list(mongo.db.recipes.find())

    # If no results are found, display a flash message
    if not results and query:
        flash(
            "No results found for '{}' Please try another search".format(
                query))

    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes, query=query)


# show all recipes in databsase
@app.route("/recipes", methods=["GET"])
def show_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


# add recipes
@app.route("/add_recipes", methods=["GET", "POST"])
def add_recipes():
    if request.method == "POST":
        recipes = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "serves": request.form.get("serves"),
            "difficulty_level": request.form.get("difficulty_level"),
            "ingredient_1": request.form.get("ingredient_1"),
            "ingredient_2": request.form.get("ingredient_2"),
            "ingredient_3": request.form.get("ingredient_3"),
            "ingredient_4": request.form.get("ingredient_4"),
            "ingredient_5": request.form.get("ingredient_5"),
            "ingredient_6": request.form.get("ingredient_6"),
            "ingredient_7": request.form.get("ingredient_7"),
            "ingredient_8": request.form.get("ingredient_8"),
            "ingredient_9": request.form.get("ingredient_9"),
            "ingredient_10": request.form.get("ingredient_10"),
            "method_1": request.form.get("method_1"),
            "method_2": request.form.get("method_2"),
            "method_3": request.form.get("method_3"),
            "method_4": request.form.get("method_4"),
            "method_5": request.form.get("method_5"),
            "method_6": request.form.get("method_6"),
            "method_7": request.form.get("method_7"),
            "method_8": request.form.get("method_8"),
            "method_9": request.form.get("method_9"),
            "method_10": request.form.get("method_10"),
            "image": request.form.get("image"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipes)
        flash("Recipe Successfully Added")
        return redirect(url_for("profile", username=session["user"]))

    categories = mongo.db.categories.find().sort("category_name", 1)
    difficulty = mongo.db.difficulty.find().sort("difficulty_level", 1)
    return render_template(
        "add_recipes.html", categories=categories, difficulty=difficulty)

# edit recipes
@app.route("/edit_recipes/<recipe_id>", methods=["GET", "POST"])
def edit_recipes(recipe_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "serves": request.form.get("serves"),
            "difficulty_level": request.form.get("difficulty_level"),
            "ingredient_1": request.form.get("ingredient_1"),
            "ingredient_2": request.form.get("ingredient_2"),
            "ingredient_3": request.form.get("ingredient_3"),
            "ingredient_4": request.form.get("ingredient_4"),
            "ingredient_5": request.form.get("ingredient_5"),
            "ingredient_6": request.form.get("ingredient_6"),
            "ingredient_7": request.form.get("ingredient_7"),
            "ingredient_8": request.form.get("ingredient_8"),
            "ingredient_9": request.form.get("ingredient_9"),
            "ingredient_10": request.form.get("ingredient_10"),
            "method_1": request.form.get("method_1"),
            "method_2": request.form.get("method_2"),
            "method_3": request.form.get("method_3"),
            "method_4": request.form.get("method_4"),
            "method_5": request.form.get("method_5"),
            "method_6": request.form.get("method_6"),
            "method_7": request.form.get("method_7"),
            "method_8": request.form.get("method_8"),
            "method_9": request.form.get("method_9"),
            "method_10": request.form.get("method_10"),
            "image": request.form.get("image"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update_one(
            {"_id": ObjectId(recipe_id)}, {"$set": submit})
        flash("{{ recipe.recipe_name }} Successfully Updated")
        return redirect(url_for("profile", username=session["user"]))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    difficulty = mongo.db.difficulty.find().sort("difficulty_level", 1)
    return render_template(
        "edit_recipes.html", recipe=recipe, categories=categories, difficulty=difficulty)

# view recipes
@app.route("/view_recipes/<recipe_id>", methods=["GET"])
def view_recipes(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("view_recipes.html", recipe=recipe)

# delete recipe
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    # Retrieve the recipe from the database
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    # Check if the recipe exists
    if recipe:
        # Check if the logged-in user is authorized to delete the recipe
        logged_in_user = session["user"]
    if logged_in_user == "admin" or logged_in_user == recipe.get("created_by"):
        # Delete the recipe
        mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
        flash("Recipe Successfully Deleted")

    # Determine redirect URL based on current location
    if request.referrer and "/admin.html" in request.referrer:

        # Redirect to admin interface
        return redirect(url_for("admin"))
    else:
        # Redirect to profile page
        return redirect(url_for("profile", username=session["user"]))


# Only accessible if logged in user is "Admin"
@app.route("/admin.html")
def admin():
    recipes = mongo.db.recipes.find()
    return render_template("admin.html", recipes=recipes)


# Manage categories
@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


# Add new category 
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        return redirect(url_for("get_categories"))

    return render_template("categories.html")


# Delete Category Function
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.delete_one({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


# Manage users when logged in as "admin"
@app.route("/get_users")
def get_users():
    users = list(mongo.db.users.find().sort("username", 1))
    return render_template("users.html", users=users)


# Delete User Function
@app.route("/delete_users/<users_id>")
def delete_users(users_id):
    mongo.db.users.delete_one({"_id": ObjectId(users_id)})
    flash("User Successfully Deleted")
    return redirect(url_for("get_users"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)
