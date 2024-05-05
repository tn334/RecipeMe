from recipe_object import Recipe

class RecipeFactory:

    def make_recipe(self, recipe_dict):
        new_recipe_name = recipe_dict['title']
        new_recipe_description = recipe_dict['description'] + '\n Prep time: ' + recipe_dict['prep time'] + '\n Active time: ' + recipe_dict['active time'] + \
                                '\n Cook time: ' + recipe_dict['cook time'] + '\n Yield: ' + recipe_dict['yield']
        new_recipe_url = recipe_dict['url']
        new_recipe_author = recipe_dict['author']
        new_recipe_ingredients = recipe_dict['ingredients']
        new_recipe_steps = recipe_dict['directions']


        new_recipe = Recipe(new_recipe_name, new_recipe_description, new_recipe_url, new_recipe_author, new_recipe_ingredients, new_recipe_steps)

        return new_recipe
