from flask import Flask, render_template, request, redirect, url_for
from urllib.parse import urlparse  # Import urlparse function
import os
from database_connector import Connection
from recipe_object import Recipe
from run_scraper import runScraper
from user_object import User
from apscheduler.schedulers.background import BackgroundScheduler

sched = BackgroundScheduler(daemon=True)
sched.add_job(runScraper,'interval',minutes=60*6)
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

@app.route('/login')
def login():
    return render_template('login.html')

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

#@app.route('/search', methods=['GET', 'POST'])
#def search():
    #if request.method == 'POST':
        #search_query = request.form.get('search_query')
        #if urlparse(search_query).scheme == '':
            #search_query = f'https://www.google.com/search?q={search_query}'
        #return render_template('search.html', recipe_info=recipe_info)
    #else:
        #return render_template('search.html')

if __name__ == "__main__":
    app.run(debug=True)
