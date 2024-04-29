import requests
from bs4 import BeautifulSoup

class RecipeScraper:
    def __init__(self, url):
        """
        Initialize the scraper with the URL of the recipe
        """
        self.url = url
        self.soup = self.get_soup()
        self.recipe_info = {
            'title': '',
            'description': '',
            'author': '',
            'prep time': '',
            'active time': '',
            'cook time': '',
            'total time': '',
            'servings': '',
            'yield': '',
            'ingredients': [],
            'directions': [],
            'url': self.url
        }

    def get_soup(self):
        """
        Fetches the webpage and returns a BeautifulSoup object for parsing HTML
        """
        page = requests.get(self.url)
        return BeautifulSoup(page.text, 'html.parser')

    def scrape(self):
        """
        Runs the scraping functions to populate the recipe_info dictionary
        """
        self.recipe_info['title'] = self.get_title()
        self.recipe_info['description'] = self.get_description()
        self.recipe_info['author'] = self.get_author()
        self.scrape_details()
        self.recipe_info['ingredients'] = self.get_ingredients()
        self.recipe_info['directions'] = self.get_directions()
        print(self.format_recipe_info())

    def get_title(self):
        """
        Extracts the title of the recipe
        """
        return self.soup.find('h1', class_='article-heading type--lion').text

    def get_description(self):
        """
        Extracts the short description of the recipe
        """
        description = self.soup.find('p', class_='article-subheading type--dog')
        return description.text.strip() if description else 'No description available'

    def get_author(self):
        """
        Attempts to extract the author name using multiple potential locations
        """
        author_span = self.soup.find('span', class_='comp mntl-bylines__item mntl-attribution__item mntl-attribution__item-name')
        if author_span:
            return author_span.text.strip()
        author_a = self.soup.find('a', class_='mntl-attribution__item-name')
        return author_a.text.strip() if author_a else 'Author not found'

    def scrape_details(self):
        """
        Extracts recipe details like cook time, total time, servings, etc.
        """
        details_div = self.soup.find('div', class_='mntl-recipe-details__content')
        if details_div:
            details_items = details_div.find_all('div', class_='mntl-recipe-details__item')
            for item in details_items:
                label = item.find('div', class_='mntl-recipe-details__label').get_text(strip=True).replace(':', '').lower()
                value = item.find('div', class_='mntl-recipe-details__value').get_text(strip=True)
                self.recipe_info[label] = value

    def get_ingredients(self):
        """
        Extracts all ingredients listed in the recipe
        """
        ingredients = []
        ingredients_ul = self.soup.find('ul', class_='mntl-structured-ingredients__list')
        if ingredients_ul:
            ingredients_lis = ingredients_ul.find_all('li', class_='mntl-structured-ingredients__list-item')
            for li in ingredients_lis:
                ingredients.append(self.parse_ingredient(li))
        return ingredients

    def parse_ingredient(self, ingredient_li):
        """
        Parses each ingredient item to separate the quantity and name
        """
        quantity = ingredient_li.find('span', attrs={'data-ingredient-quantity': 'true'}).text.strip()
        unit = ingredient_li.find('span', attrs={'data-ingredient-unit': 'true'}).text.strip()
        name = ingredient_li.find('span', attrs={'data-ingredient-name': 'true'}).text.strip()
        if not quantity and not unit:
            return [name]
        return [f"{quantity} {unit}".strip(), name]

    def get_directions(self):
        """
        Extracts the step-by-step directions from the recipe
        """
        directions = []
        directions_ol = self.soup.find('ol', class_='comp mntl-sc-block mntl-sc-block-startgroup mntl-sc-block-group--OL')
        if directions_ol:
            directions_lis = directions_ol.find_all('li', class_='comp mntl-sc-block mntl-sc-block-startgroup mntl-sc-block-group--LI')
            for index, li in enumerate(directions_lis, start=1):
                direction_text = ' '.join(p.get_text(strip=True) for p in li.find_all('p', recursive=False))
                directions.append([f"Step {index}", direction_text])
        return directions

    def format_recipe_info(self):
        """
        Formats the recipe information into a more readable string output
        """
        return '\n'.join(f"{key}: {value}" for key, value in self.recipe_info.items())


# List of recipe URLs to scrape
urls = [
    'https://www.allrecipes.com/recipe/218054/spicy-sausage-broccoli-rabe-parmesan/',
    'https://www.allrecipes.com/recipe/188824/cheesy-sausage-pasta/',
    'https://www.allrecipes.com/recipe/238691/simple-macaroni-and-cheese/',
    'https://www.allrecipes.com/recipe/8527854/coconut-chickpea-curry/',
    'https://www.allrecipes.com/black-pepper-chicken-recipe-8382732'
]

# Loop over each URL, create a scraper instance, then print the scraped data
for url in urls:
    scraper = RecipeScraper(url)
    scraper.scrape()
    print("\n" + "="*80 + "\n")