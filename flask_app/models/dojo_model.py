from ..config.mysqlconnection import connectToMySQL



class Dojo:
    def __init__(self, data):
        self.id  = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_ninjas').query_db(query)
    
        dojos = []
        
        for row in results:
            dojos.append(cls(row))
        return dojos
    
    
    @classmethod
    def create(cls,data):
        query = "INSERT INTO dojos (name, created_at, updated_at ) VALUES (%(name)s, NOW(), NOW());"
        
        results = connectToMySQL('dojos_ninjas').query_db(query,data)
        return results
       