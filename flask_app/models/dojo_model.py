from ..config.mysqlconnection import connectToMySQL
from flask_app.models.new_ninja_model import Ninja



class Dojo:
    def __init__(self, data):
        self.id  = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
        
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojo_ninja_v3').query_db(query)
        print(results)
        dojos = []

        for row in results:
            dojos.append(cls(row))
        return dojos

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojos_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojo_ninja_v3').query_db(query,data)
        dojo = Dojo(results[0])
        for row in results:
            row_data = {
                "id": row['ninjas.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "age": row['age'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at'],
            
            }
            dojo.ninjas.append(Ninja(row_data))
        return dojo

    @classmethod
    def create(cls,data):
        query = "INSERT INTO dojos (name, created_at, updated_at ) VALUES (%(name)s, NOW(), NOW());"

        results = connectToMySQL('dojo_ninja_v3').query_db(query,data)
        return results

   