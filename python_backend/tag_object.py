from database_connector import Connection
class Tag:

    def __init__(self, tag_name="", description="", tagged_recipes=[]):
        self.__tag_name = tag_name
        self.__description = description
        self.__tagged_recipes = tagged_recipes

    def set_name(self, tag_name):
        self.__tag_name = tag_name

    def set_description(self, description):
        self.__description = description

    def set_tagged_recipes(self, tagged_recipes):
        self.__tagged_recipes = tagged_recipes

    def add_tagged_recipe(self, recipe_to_tag):
        self.__tagged_recipes.append(recipe_to_tag)

    def get_name(self):
        return self.__tag_name

    def get_description(self):
        return self.__description
  
    def get_tagged_recipes(self):
        return self.__tagged_recipes

    def save(self, user, pwd):
        rowsAffected = 0
        saveConn = Connection( user = user, pwd = pwd, db = "recipe_me" )
        queryString = "SELECT tag_name FROM tag WHERE tag_name = %s;"
        queryValues = [self.get_name()]
        queryResult = saveConn.run_query(queryString, queryValues)
        if (queryResult == []):
            insertString = "INSERT INTO tag (tag_name, description) VALUES (%s, %s);"
            insertValues = [self.get_name(), self.get_description()]
            rowsAffected = saveConn.run_modify(insertString, insertValues)
            if (rowsAffected == 1):
                for recipeID in self.get_tagged_recipes():
                    insertString = "INSERT IGNORE INTO recipe_tags (tagged_recipe, attached_tag) VALUES (%s, %s);"
                    insertValues = [recipeID, self.get_name()]
                    rowsAffected = saveConn.run_modify(insertString, insertValues)

        return (rowsAffected == 1)
    
    def load(self, user, pwd, name):
        dbConn = Connection( user = user, pwd = pwd, db = "recipe_me" )
        queryString = "SELECT * FROM tag WHERE tag_name = %s;"
        queryValues = [name]
        queryResult = dbConn.run_query(queryString, queryValues)
        if (queryResult != None):
            for (name, description) in queryResult:
                self.set_name(name)
                self.set_description(description)

            queryString = "SELECT tagged_recipe FROM recipe_tags WHERE attached_tag = %s;"
            queryValues = [self.get_name()]
            recipeResult = dbConn.run_query(queryString, queryValues)
            recipeList = []
            if (recipeResult != None):
                for recipeID in recipeResult:
                    recipeList.append(recipeID)
                self.set_tagged_recipes(recipeList)
            return True

        return False