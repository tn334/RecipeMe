def suggest_recipes(user_favorites, user_tags, recipe_database):
    suggested_recipes = []

    for recipe_id in user_favorites:
        # Fetch details of user's favorite recipes from the database
        favorite_recipe = recipe_database.get_recipe_by_id(recipe_id)
        # Find similar recipes based on shared ingredients or tags
        similar_recipes = find_similar_recipes(favorite_recipe, recipe_database)
        suggested_recipes.extend(similar_recipes)

    # Remove duplicates from the list of suggested recipes
    suggested_recipes = list(set(suggested_recipes))

    # Rank suggested recipes based on relevance
    ranked_recipes = rank_recipes(suggested_recipes, user_favorites)

    # Return top suggestions
    return ranked_recipes[:10]

def find_similar_recipes(favorite_recipe, recipe_database):
    similar_recipes = []
    # Find similar recipes based on shared ingredients or tags
    for ingredient_id in favorite_recipe.ingredients:
        # Fetch recipes containing the same ingredient
        similar_recipes.extend(recipe_database.get_recipes_by_ingredient(ingredient_id))
    for tag in favorite_recipe.tags:
        # Fetch recipes with similar tags
        similar_recipes.extend(recipe_database.get_recipes_by_tag(tag))

    return similar_recipes

def rank_recipes(suggested_recipes, user_tags):
    # Implement ranking algorithm based on user preferences
    # Assign weights to different factors such as ingredient match, cooking time
    ranked_recipes = []

    # Example ranking logic:
    for recipe in suggested_recipes:
        relevance_score = calculate_relevance_score(recipe, user_tags)
        # Calc relevance score based on user preferences and recipe attributes
        # Higher scores indicate higher relevance
        ranked_recipes.append((recipe, relevance_score))

    # Sort recipes based on relevance score
    ranked_recipes.sort(key=lambda x: x[1], reverse=True)

    return ranked_recipes

def calculate_relevance_score(recipe, user_tags):
    # Calculate relevance scores based on shared tags between the recipe and user's preferences
    shared_tags = recipe.tags.intersection(user_tags)
    relevance_score = len(shared_tags) / len(user_tags) if user_tags else 0
    return relevance_score