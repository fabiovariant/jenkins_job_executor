
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

class JobDAO(object):

    def __init__(self, conn):
        self.conn = conn

    def save(self, job, user):
        pass

    def get_job_exec_history(self, user):
        pass

    def get_user_jobs(self, user):
        pass

    def update_exec(self, job, user):
        pass