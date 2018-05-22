
# Classe que encapsula todas as operações DAO de um usuário.
class UserDAO(object):

    def __init__(self, conn):
        self.conn = conn

    def save(self, user):
        pass
    
    def getByEmail(self, email):
        pass
    
    def update(self, user):
        pass
