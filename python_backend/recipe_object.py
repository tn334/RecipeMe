from database_connector import Connection

class Recipe:

    def __init__(self, name="", description="", url="", author="", ingredients=[], steps=[]):
        self.__name = name
        self.__description = description
        self.__url = url
        self.__author = author
        self.__ingredients = ingredients
        allSteps = ""
        for step in steps:
            allSteps += step + "\n"
        self.__steps = allSteps


    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_description(self, description):
        self.__description = description

    def set_url(self, url):
        self.__url = url

    def set_author(self, author):
        self.__author = author

    def set_ingredients(self, ingredients):
        self.__ingredients = ingredients

    def set_steps(self, steps):
        self.__steps = steps

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_url(self):
        return self.__url

    def get_author(self):
        return self.__author

    def get_ingredients(self):
        return self.__ingredients

    def get_steps(self):
        return self.__steps
    
    def print_out(self):
        print("title: ", self.get_name())
        print("description: ", self.get_description())
        print("author: ", self.get_author())
        print("ingredients: ", self.get_ingredients())
        print("steps: ", self.get_steps())

    def save(self, user, pwd):
        rowsAffected = 0
        saveConn = Connection( user = user, pwd = pwd, db = "recipe_me" )
        queryString = "SELECT recipe_id FROM recipe WHERE origin_url = %s;"
        queryValues = [self.get_url()]
        queryResult = saveConn.run_query(queryString, queryValues)
        if (queryResult == []):
            insertString = "INSERT INTO recipe (name, description, origin_url, author, steps) VALUES (%s, %s, %s, %s, %s);"
            insertValues = [self.get_name(), self.get_description(), self.get_url(), self.get_author(), self.get_steps()]
            rowsAffected = saveConn.run_modify(insertString, insertValues)
            if (rowsAffected == 1):
                queryString = "SELECT recipe_id FROM recipe WHERE origin_url = %s;"
                queryValues = [self.get_url()]
                recipeID = saveConn.run_query(queryString, queryValues)[0][0]
                self.set_id(recipeID)
                for ingredient in self.get_ingredients():
                    if ',' in ingredient[1]:
                        ingredientName, ingredientDescription = ingredient[1].split(',')
                    else:
                        ingredientName = ingredient[1]
                        ingredientDescription = ''
                    
                    queryString = "SELECT ingredient_id FROM ingredient WHERE ingredient_name = %s;"
                    queryValues = [ingredientName]
                    queryResult = saveConn.run_query(queryString, queryValues)
                    if (queryResult == []):
                        insertString = "INSERT INTO ingredient (ingredient_name) VALUES (%s);"
                        insertValues = [ingredientName]
                        saveConn.run_modify(insertString, insertValues)
                        queryString = "SELECT ingredient_id FROM ingredient WHERE ingredient_name = %s;"
                        queryValues = [ingredientName]
                        queryResult = saveConn.run_query(queryString, queryValues)
                    ingredientID = queryResult[0][0]
                    insertString = "INSERT INTO recipe_ingredients (quantity, description, calling_recipe, called_ingredient) VALUES (%s, %s, %s, %s)"
                    insertValues = [ingredient[0], ingredientDescription, recipeID, ingredientID]
                    rowsAffected = saveConn.run_modify(insertString, insertValues)
        else:
            self.set_id(queryResult[0][0])

        return (rowsAffected == 1)


    def remove(self, user, pwd):
        saveConn = Connection( user = user, pwd = pwd, db = "recipe_me" )
        queryString = "DELETE FROM recipe WHERE recipe_id = %s;"
        queryValues = [self.get_id()]
        rowsAffected = saveConn.run_modify(queryString, queryValues)
        return (rowsAffected == 1)


    def load(self, id, user, pwd):
        dbConn = Connection( user = user, pwd = pwd, db = "recipe_me" )
        queryString = "SELECT * FROM recipe WHERE recipe_id = %s;"
        queryValues = [id]
        queryResult = dbConn.run_query(queryString, queryValues)
        if (queryResult != None):
            for (recipe_id, name, description, url, author, steps) in queryResult:
                self.set_id(recipe_id)
                self.set_name(name)
                self.set_description(description)
                self.set_url(url)
                self.set_author(author)
                self.set_steps(steps)
            queryString = "SELECT ri.quantity, ri.description, i.ingredient_name FROM recipe_ingredients ri INNER JOIN ingredient i ON ri.called_ingredient = i.ingredient_id WHERE calling_recipe = %s;"
            queryValues = [id]
            ingredientResult = dbConn.run_query(queryString, queryValues)
            ingredientList = []
            if (ingredientResult != None):
                for (quantity, description, ingredient_name) in ingredientResult:
                    if description != '':
                        ingredient_name += ","+description
                    ingredientList.append([quantity, ingredient_name])
                self.set_ingredients(ingredientList)
            return True

        return False