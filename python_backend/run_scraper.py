from recipe_factory import RecipeFactory
from recipe_object import Recipe
from scrape_recipe import RecipeScraper



# List of recipe URLs to scrape
urls = [
    'https://www.allrecipes.com/recipe/218054/spicy-sausage-broccoli-rabe-parmesan/',
    'https://www.allrecipes.com/recipe/188824/cheesy-sausage-pasta/',
    'https://www.allrecipes.com/recipe/238691/simple-macaroni-and-cheese/',
    'https://www.allrecipes.com/recipe/8527854/coconut-chickpea-curry/',
    'https://www.allrecipes.com/black-pepper-chicken-recipe-8382732'
]

# Loop over each URL, create a scraper instance, then print the scraped data
scraper = RecipeScraper()
factory = RecipeFactory()
ids = []
for url in urls:
    scraper.scrape(url)
    newRecipe = factory.makeRecipe(scraper.recipe_info)
    newRecipe.save('root', 'Cs440')
    ids.append(newRecipe.get_id())

for id in ids:
    newRecipe = Recipe()
    newRecipe.load(id, 'root', 'Cs440')
    newRecipe.print_out()