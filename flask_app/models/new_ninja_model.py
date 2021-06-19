from ..config.mysqlconnection import connectToMySQL



class Ninja:
    def __init__(self, data):
        self.id  = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojo_ninja_v3').query_db(query)
        print(results)
        ninjas = []
        
        for row in results:
            ninjas.append(Ninja(row))
        return ninjas
    
    
    @classmethod
    def create(cls,data):
        query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojos_id) VALUES (%(first_name)s,%(last_name)s, %(age)s, NOW(), NOW(), %(dojos_id)s);"
        
        results = connectToMySQL('dojo_ninja_v3').query_db(query,data)
        return results
    