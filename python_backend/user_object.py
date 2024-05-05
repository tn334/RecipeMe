from database_connector import Connection

class User:

    def __init__(self, user_id="", email="", password="", favorites=[]):
        self.__user_id = user_id
        self.__email = email
        self.__password = password
        self.__favorites = favorites

    def set_id(self, user_id):
        self.__user_id = user_id

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password

    def set_favorites(self, favorites):
        self.__favorites = favorites

    def get_id(self):
        return self.__user_id

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password
    
    def get_favorites(self):
        return self.__favorites

    def save(self, user, pwd):
        rowsAffected = 0
        saveConn = Connection( user = user, pwd = pwd, db = "recipe_me" )
        queryString = "SELECT user_id FROM user WHERE email = %s;"
        queryValues = [self.get_email()]
        queryResult = saveConn.run_query(queryString, queryValues)
        if (queryResult == []):
            insertString = "INSERT INTO user (email, password) VALUES (%s, %s);"
            insertValues = [self.get_email(), self.get_password()]
            rowsAffected = saveConn.run_modify(insertString, insertValues)
            if (rowsAffected == 1):
                for recipeID in self.get_favorites():
                    insertString = "INSERT IGNORE INTO user_favorite_recipes (favoriting_user, favorited_recipe) VALUES (%s, %s);"
                    insertValues = [recipeID, self.get_id()]
                    rowsAffected = saveConn.run_modify(insertString, insertValues)

        return (rowsAffected == 1)
    
    def load(self, user, pwd, email):
        dbConn = Connection( user = user, pwd = pwd, db = "recipe_me" )
        queryString = "SELECT * FROM user WHERE email = %s;"
        queryValues = [email]
        queryResult = dbConn.run_query(queryString, queryValues)
        if (queryResult != None):
            for (user_id, email, password) in queryResult:
                self.set_id(user_id)
                self.set_email(email)
                self.set_password(password)

            queryString = "SELECT favorited_recipe FROM user_favorite_recipes WHERE favoriting_user = %s;"
            queryValues = [self.get_id()]
            favoriteResult = dbConn.run_query(queryString, queryValues)
            favoritesList = []
            if (favoriteResult != None):
                for favoriteID in favoriteResult:
                    favoritesList.append(favoriteID)
                self.set_favorites(favoritesList)
            return True

        return False
