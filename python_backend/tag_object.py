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
        rows_affected = 0
        save_conn = Connection( user = user, pwd = pwd, db = "recipe_me" )
        query_string = "SELECT tag_name FROM tag WHERE tag_name = %s;"
        query_values = [self.get_name()]
        query_result = save_conn.run_query(query_string, query_values)
        if (query_result == []):
            insert_string = "INSERT INTO tag (tag_name, description) VALUES (%s, %s);"
            insert_values = [self.get_name(), self.get_description()]
            rows_affected = save_conn.run_modify(insert_string, insert_values)
            if (rows_affected == 1):
                for recipe_id in self.get_tagged_recipes():
                    insert_string = "INSERT IGNORE INTO recipe_tags (tagged_recipe, attached_tag) VALUES (%s, %s);"
                    insert_values = [recipe_id, self.get_name()]
                    rows_affected = save_conn.run_modify(insert_string, insert_values)

        return (rows_affected == 1)
    
    def load(self, user, pwd, name):
        db_conn = Connection( user = user, pwd = pwd, db = "recipe_me" )
        query_string = "SELECT * FROM tag WHERE tag_name = %s;"
        query_values = [name]
        query_result = db_conn.run_query(query_string, query_values)
        if (query_result != None):
            for (name, description) in query_result:
                self.set_name(name)
                self.set_description(description)

            query_string = "SELECT tagged_recipe FROM recipe_tags WHERE attached_tag = %s;"
            query_values = [self.get_name()]
            recipe_result = db_conn.run_query(query_string, query_values)
            recipe_list = []
            if (recipe_result != None):
                for recipe_id in recipe_result:
                    recipe_list.append(recipe_id)
                self.set_tagged_recipes(recipe_list)
            return True

        return False