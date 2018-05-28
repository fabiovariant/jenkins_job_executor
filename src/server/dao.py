import sys
from mysql.connector.errors import DatabaseError
from _mysql_connector import MySQLInterfaceError

# Classe que encapsula todas as operações DAO de um usuário.
class UserDAO(object):

    def __init__(self, conn):
        self.cur = conn.cursor(buffered=True)

    def save(self, user):
        print('DAO')

    def getByEmail(self, email):
        print('DAO')

    def update(self, user):
        print('DAO')

    def getUserTypes(self):
        try:
            sql = 'SELECT cd_user_Type, ds_user_type FROM Dm_User_type'
            self.cur.execute(sql)
            user_types = []
            for (cd_user_Type, ds_user_type) in self.cur:
                user_type = {
                    'cd_user_type': cd_user_Type,
                    'ds_user_type': ds_user_type
                }
                user_types.append(user_type)
            return user_types
        except:
            raise

class JobDAO(object):

    def __init__(self, conn):
        self.cur = conn.cursor(buffered=True)

    def save(self, job, user):
        try:
            sql = '''INSERT INTO job_exec_history(id_user, job_name, dt_exec) 
                     VALUES (%s, %s, NOW())'''
            self.cur.execute(sql, (user, job, ))
            return self.cur.lastrowid
        except DatabaseError as e:
            print('DAO error:', e)
            raise

    def get_job_exec_history(self, user):
        try:
            sql = '''SELECT id_exec, id_user, job_name, dt_exec, exec_return, sucess,
                     finished FROM job_exec_history WHERE id_user = %s LIMIT 100'''
            self.cur.execute(sql, (user,))
            jobs_hist = []
            for (id_exec, id_user, job_name, dt_exec, exec_return, sucess, finished) in self.cur:
                job = {
                    'id_exec': id_exec,
                    'id_user': id_user,
                    'job_name': job_name,
                    'dt_exec': str(dt_exec),
                    'exec_return': exec_return,
                    'sucess': sucess,
                    'finished': finished
                }
                jobs_hist.append(job)
            return jobs_hist
        except:
            raise

    def get_user_jobs(self, user):
        try:
            sql = '''
                    SELECT 
                        job.id_job, 
                        job.nm_Job 
                    FROM job_user_permission
                        INNER JOIN job
                                ON job.id_job = job_user_permission.id_job
                    WHERE job_user_permission.cd_user_Type = %s'''
            self.cur.execute(sql, (user,))
            jobs = []
            for (id_job, nm_Job) in self.cur:
                job = {
                    'idJob': id_job, 
                    'jobName': nm_Job
                }
                jobs.append(job)
            return jobs
        except DatabaseError as e:
            print('DAO error:', e)
            raise

    def update_exec(self, id_exec, job_name, user, exec_return, success):
        try:
            sql = '''
                UPDATE job_exec_history
                   SET 
                    exec_return = %s,
                    sucess = %s,
                    finished = true
                WHERE id_exec = %s
                  AND id_user = %s
                  AND job_name = %s'''
            print((exec_return, success, id_exec, user, job_name,))
            self.cur.execute(sql, (exec_return, success, id_exec, user, job_name,))
        except DatabaseError as e:
            print('DAO error:', e)
            raise
        except MySQLInterfaceError as e:
            print('_mysql_connector.MySQLInterfaceError', e)
            raise
        except:
            print('Unexpected error:', sys.exc_info()[0])
            raise

    def insert_new_job(self, job):
        try:
            sql = '''INSERT INTO job(nm_Job) VALUES (%s)'''
            self.cur.execute(sql, (job,))
            print('ow')
            return self.cur.lastrowid
        except DatabaseError as e:
            print('DAO error:', e)
            raise

    def get_registred_jobs(self):
        sql = '''SELECT id_job, nm_Job FROM job'''
        self.cur.execute(sql)
        jobs = []
        for (id_job, nm_Job) in self.cur:
            job = {
                'id_job': id_job,
                'nm_Job': nm_Job
            }
            jobs.append(job)
        return jobs

    
    def insert_job_user_permission(self, job_id, tp_user):
        sql = '''INSERT INTO job_user_permission(id_job, cd_user_Type) VALUES (%s, %s)'''
        self.cur.execute(sql, (job_id, tp_user))