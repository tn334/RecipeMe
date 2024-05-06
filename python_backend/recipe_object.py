from database_connector import Connection

class Recipe:

    def __init__(self, name="", description="", url="", author="", ingredients=[], steps=[]):
        self.__name = name
        self.__description = description
        self.__url = url
        self.__author = author
        self.__ingredients = ingredients
        all_steps = ""
        for step in steps:
            all_steps += step + "\n"
        self.__steps = all_steps


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
        rows_affected = 0
        save_conn = Connection( user = user, pwd = pwd, db = "recipe_me" )
        query_string = "SELECT recipe_id FROM recipe WHERE origin_url = %s;"
        query_values = [self.get_url()]
        query_result = save_conn.run_query(query_string, query_values)
        if (query_result == []):
            insert_string = "INSERT INTO recipe (name, description, origin_url, author, steps) VALUES (%s, %s, %s, %s, %s);"
            insert_values = [self.get_name(), self.get_description(), self.get_url(), self.get_author(), self.get_steps()]
            rows_affected = save_conn.run_modify(insert_string, insert_values)
            if (rows_affected == 1):
                query_string = "SELECT recipe_id FROM recipe WHERE origin_url = %s;"
                query_values = [self.get_url()]
                recipe_id = save_conn.run_query(query_string, query_values)[0][0]
                self.set_id(recipe_id)
                for ingredient in self.get_ingredients():
                    if ',' in ingredient[1]:
                        ingredient_name, ingredient_description = ingredient[1].split(',')
                    else:
                        ingredient_name = ingredient[1]
                        ingredient_description = ''
                    
                    query_string = "SELECT ingredient_id FROM ingredient WHERE ingredient_name = %s;"
                    query_values = [ingredient_name]
                    query_result = save_conn.run_query(query_string, query_values)
                    if (query_result == []):
                        insert_string = "INSERT INTO ingredient (ingredient_name) VALUES (%s);"
                        insert_values = [ingredient_name]
                        save_conn.run_modify(insert_string, insert_values)
                        query_string = "SELECT ingredient_id FROM ingredient WHERE ingredient_name = %s;"
                        query_values = [ingredient_name]
                        query_result = save_conn.run_query(query_string, query_values)
                    ingredient_id = query_result[0][0]
                    insert_string = "INSERT INTO recipe_ingredients (quantity, description, calling_recipe, called_ingredient) VALUES (%s, %s, %s, %s)"
                    insert_values = [ingredient[0], ingredient_description, recipe_id, ingredient_id]
                    rows_affected = save_conn.run_modify(insert_string, insert_values)
        else:
            self.set_id(query_result[0][0])

        return (rows_affected == 1)


    def remove(self, user, pwd):
        save_conn = Connection( user = user, pwd = pwd, db = "recipe_me" )
        query_string = "DELETE FROM recipe WHERE recipe_id = %s;"
        query_values = [self.get_id()]
        rows_affected = save_conn.run_modify(query_string, query_values)
        return (rows_affected == 1)


    def load(self, user, pwd, id):
        db_conn = Connection( user = user, pwd = pwd, db = "recipe_me" )
        query_string = "SELECT * FROM recipe WHERE recipe_id = %s;"
        query_values = [id]
        query_result = db_conn.run_query(query_string, query_values)
        if (query_result != None):
            for (recipe_id, name, description, url, author, steps) in query_result:
                self.set_id(recipe_id)
                self.set_name(name)
                self.set_description(description)
                self.set_url(url)
                self.set_author(author)
                self.set_steps(steps)
            query_string = "SELECT ri.quantity, ri.description, i.ingredient_name FROM recipe_ingredients ri INNER JOIN ingredient i ON ri.called_ingredient = i.ingredient_id WHERE calling_recipe = %s;"
            query_values = [id]
            ingredient_result = db_conn.run_query(query_string, query_values)
            ingredient_list = []
            if (ingredient_result != None):
                for (quantity, description, ingredient_name) in ingredient_result:
                    if description != '':
                        ingredient_name += ","+description
                    ingredient_list.append([quantity, ingredient_name])
                self.set_ingredients(ingredient_list)
            return True

        return False