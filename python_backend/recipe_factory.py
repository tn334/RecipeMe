from recipe_object import Recipe

class RecipeFactory:

    def makeRecipe(self, recipeDict):
        newRecipeName = recipeDict['title']
        newRecipeDescription = recipeDict['description'] + '\n Prep time: ' + recipeDict['prep time'] + '\n Active time: ' + recipeDict['active time'] + \
                                '\n Cook time: ' + recipeDict['cook time'] + '\n Yield: ' + recipeDict['yield']
        newRecipeUrl = recipeDict['url']
        newRecipeAuthor = recipeDict['author']
        newRecipeIngredients = recipeDict['ingredients']
        newRecipeSteps = recipeDict['directions']


        newRecipe = Recipe(newRecipeName, newRecipeDescription, newRecipeUrl, newRecipeAuthor, newRecipeIngredients, newRecipeSteps)

        return newRecipe
