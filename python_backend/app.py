from flask import Flask, render_template, request
from urllib.parse import urlparse  # Import urlparse function

from scraper.scrape_recipe import RecipeScraper

app = Flask(__name__)

scraper = RecipeScraper()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_query = request.form.get('search_query')
        if urlparse(search_query).scheme == '':
            search_query = f'https://www.google.com/search?q={search_query}'
        scraper.scrape(search_query)
        recipe_info = scraper.recipe_info
        return render_template('search.html', recipe_info=recipe_info)
    else:
        return render_template('search.html')

if __name__ == "__main__":
    app.run(debug=True)
