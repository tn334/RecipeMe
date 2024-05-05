from recipe_factory import RecipeFactory
from recipe_object import Recipe
from scrape_recipe import RecipeScraper, AllRecipesStrategy


def runScraper():
    # List of recipe URLs to scrape
    urls = [
        'https://www.allrecipes.com/recipe/218054/spicy-sausage-broccoli-rabe-parmesan/',
        'https://www.allrecipes.com/recipe/188824/cheesy-sausage-pasta/',
        'https://www.allrecipes.com/recipe/238691/simple-macaroni-and-cheese/',
        'https://www.allrecipes.com/recipe/8527854/coconut-chickpea-curry/',
        'https://www.allrecipes.com/black-pepper-chicken-recipe-8382732'
        'https://www.allrecipes.com/chicken-scampi-pasta-recipe-8636935',
        'https://www.allrecipes.com/recipe/236992/santa-maria-grilled-tri-tip-beef/',
        'https://www.allrecipes.com/mediterranean-baked-cod-with-lemon-recipe-8576313',
        'https://www.allrecipes.com/parmesan-crusted-baked-fish-recipe-8584575',
        'https://www.allrecipes.com/watermelon-tuna-poke-bowl-recipe-7568001',
        'https://www.allrecipes.com/lemon-ricotta-and-spinach-pasta-recipe-7975824',
        'https://www.allrecipes.com/recipe/15022/veggie-pizza/',
        'https://www.allrecipes.com/recipe/265979/air-fryer-baked-potatoes/',
        'https://www.allrecipes.com/recipe/85452/homemade-black-bean-veggie-burgers/',
        'https://www.allrecipes.com/recipe/24712/ginger-veggie-stir-fry/'
    ]

    # Loop over each URL, create a scraper instance, then print the scraped data
    allRecipesStrategy = AllRecipesStrategy()
    scraper = RecipeScraper(strategy=allRecipesStrategy)
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