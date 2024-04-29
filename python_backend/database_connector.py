import mysql.connector

class Connection:

    def __init__(self, host = "localhost", user = "root", pwd = "Cs440", db = "recipe_me"):
        self.__hostname = host
        self.__username = user
        self.__password = pwd
        self.__database = db
        self.__DBconnection = None



    def open_con(self):
        self.__DBconnection = mysql.connector.connect(host=self.__hostname,
                                              user=self.__username,
                                              password=self.__password,
                                              database=self.__database)


    def get_con(self):
        return self.__DBconnection


    def close_con(self):
        self.__DBconnection .close()
        self.__DBconnection  = None

    def run_query(self, sql, values):
        self.open_con()
        cursor = self.__DBconnection.cursor()
        cursor.execute(sql, values)
        results = cursor.fetchall()
        cursor.close()
        self.__DBconnection.close()
        return results

    def run_modify(self, sql, values):
        self.open_con()
        cursor = self.__DBconnection.cursor()
        cursor.execute(sql, values)
        self.__DBconnection.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        self.__DBconnection.close()
        return affected_rows