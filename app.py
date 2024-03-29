import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

 
#--HOME PAGE--
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


#--SIGN UP--

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        #-- check if name already exists in a database --
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

        #put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Ensure the user is logged in
    if 'user' not in session:
        flash("You need to log in first")
        return redirect(url_for("login"))

    # Get the username from the session
    logged_in_user = session["user"]

    # Check if the username in the URL matches the logged-in user
    if username != logged_in_user:
        flash("You can only view your own profile")
        return redirect(url_for("home"))  # Or any other appropriate redirect

    # Fetch the user's recipes from the database
    user_recipes = mongo.db.recipes.find({"created_by": logged_in_user})

    return render_template("profile.html", username=username, recipes=user_recipes)


@app.route("/logout")
def logout():
    #remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/recipes", methods=["GET"])
def show_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


@app.route("/add_recipes", methods=["GET","POST"])
def add_recipes():
    if request.method == "POST":
        recipes = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "serves": request.form.get("serves"),
            "rating": request.form.get("rating"),
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
        return redirect(url_for("add_recipes"))
        
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipes.html", categories=categories)

@app.route("/edit_recipes/<recipe_id>", methods=["GET", "POST"])
def edit_recipes(recipe_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "serves": request.form.get("serves"),
            "rating": request.form.get("rating"),
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
        mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)}, {"$set": submit})
        flash("Recipe Successfully Updated")
        
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_recipes.html", recipe=recipe, categories=categories)

@app.route("/view_recipes/<recipe_id>", methods=["GET"])
def view_recipes(recipe_id):
    recipe=mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("view_recipes.html", recipe=recipe)



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)