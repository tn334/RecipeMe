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
        rows_affected = 0
        save_conn = Connection( user = user, pwd = pwd, db = "recipe_me" )
        query_string = "SELECT user_id FROM user WHERE email = %s;"
        query_values = [self.get_email()]
        query_result = save_conn.run_query(query_string, query_values)
        if (query_result == []):
            insert_string = "INSERT INTO user (email, password) VALUES (%s, %s);"
            insert_values = [self.get_email(), self.get_password()]
            rows_affected = save_conn.run_modify(insert_string, insert_values)
            if (rows_affected == 1):
                for recipe_id in self.get_favorites():
                    insert_string = "INSERT IGNORE INTO user_favorite_recipes (favoriting_user, favorited_recipe) VALUES (%s, %s);"
                    insert_values = [recipe_id, self.get_id()]
                    rows_affected = save_conn.run_modify(insert_string, insert_values)

        return (rows_affected == 1)
    
    def load(self, user, pwd, email):
        db_conn = Connection( user = user, pwd = pwd, db = "recipe_me" )
        query_string = "SELECT * FROM user WHERE email = %s;"
        query_values = [email]
        query_result = db_conn.run_query(query_string, query_values)
        if (query_result != None):
            for (user_id, email, password) in query_result:
                self.set_id(user_id)
                self.set_email(email)
                self.set_password(password)

            query_string = "SELECT favorited_recipe FROM user_favorite_recipes WHERE favoriting_user = %s;"
            query_values = [self.get_id()]
            favorite_result = db_conn.run_query(query_string, query_values)
            favorites_list = []
            if (favorite_result != None):
                for favorite_id in favorite_result:
                    favorites_list.append(favorite_id)
                self.set_favorites(favorites_list)
            return True

        return False
