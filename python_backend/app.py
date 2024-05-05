from flask import Flask, render_template, request
from urllib.parse import urlparse  # Import urlparse function
import os
from recipe_object import Recipe

template_dir = os.path.abspath('../Website')

app = Flask(__name__, template_folder=template_dir, static_folder=template_dir+'/static')

#scraper = RecipeScraper()

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
    recipeObject = Recipe()
    recipeObject.load('root', 'Cs440', recipe_id)
    #recipeObject.print_out()
    return render_template('recipe.html', recipe=recipeObject)

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
