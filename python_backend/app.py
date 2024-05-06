from flask import Flask, render_template, request, redirect, url_for
from urllib.parse import urlparse  # Import urlparse function
import os
from database_connector import Connection
from recipe_object import Recipe
from run_scraper import run_scraper
from user_object import User
from apscheduler.schedulers.background import BackgroundScheduler

sched = BackgroundScheduler(daemon=True)
sched.add_job(run_scraper,'interval',minutes=60*6)
sched.start()

template_dir = os.path.abspath('../Website')

app = Flask(__name__, template_folder=template_dir, static_folder=template_dir+'/static')

#define route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Instantiate connection
        db_conn = Connection()

        # Create a User object
        user = User()

        # Attempt to authenticate the user
        if user.load(user='root', pwd='Cs440', email=email):
            if user.get_password() == password:
                # If authentication successful, redirect to home page
                return redirect(url_for('home'))
        
        # If authentication fails, render login page with an error message
        error_message = "Invalid email or password. Please try again."
        return render_template('login.html', error_message=error_message)

    # If request method is GET, render the login page
    return render_template('login.html')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/recipe')
@app.route('/recipe/<recipe_id>')
def recipe(recipe_id=None):
    recipe_object = Recipe()
    recipe_object.load('root', 'Cs440', recipe_id)
    #recipe_object.print_out()
    return render_template('recipe.html', recipe=recipe_object)

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/sign_up')
def signup():
    return render_template('sign_up.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        # Handle the POST request
        search_query = request.form.get('search_query')
        selected_tags = request.form.getlist('tags[]')

        db_conn = Connection(user='root', pwd='IhAtEtHiS!22', db='recipe_me')
        query_string = "SELECT recipe_id, name FROM recipe WHERE name LIKE %s"
        query_values = ['%' + search_query + '%']
        if selected_tags:
          query_string += " AND recipe_id IN (SELECT DISTINCT r.recipe_id FROM recipe r INNER JOIN recipe_tags rt ON r.recipe_id = rt.recipe_id INNER JOIN tag t ON rt.tag_id = t.tag_id WHERE t.tag_name IN (%s))"
          query_values.extend(selected_tags)
        search_results = db_conn.run_query(query_string, query_values)

        recipes = []
        for recipe_id, recipe_name in search_results:
            recipe = Recipe()
            recipe.load('root', 'IhAtEtHiS!22', recipe_id)
            recipes.append(recipe)
        # Perform any necessary logic with the search query
        # For example, you can redirect to the recipe page based on the search query
        return redirect(url_for('recipe', recipes=recipes))
    else:
        # Handle the GET request
        # Fetch tag data from the database and render the search page
        db_conn = Connection(user='root', pwd='IhAtEtHiS!22', db='recipe_me')
        query_string = "SELECT tag_name, description FROM tag;"
        tag_data = db_conn.run_query(query_string, [])
        tag_objects = [Tag(tag_name=name, description=description) for name, description in tag_data]
        return render_template('search.html', tag_options=tag_objects)

if __name__ == "__main__":
    app.run(debug=True)
