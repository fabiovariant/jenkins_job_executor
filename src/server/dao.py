
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

class JobDAO(object):

    def __init__(self, conn):
        self.cur = conn.cursor(buffered=True)

    def save(self, job, user):
        try:
            sql = '''INSERT INTO job_exec_history(id_user, job_name, dt_exec) 
                     VALUES (%s, %s, %s, NOW()) RETURNING id_exec'''
            self.cur.execute(sql, (user['id_user'], job['job_name']))
            if (id_exec) in self.cur:
                return id_exec
        except:
            raise

    def get_job_exec_history(self, user):
        try:
            sql = '''SELECT id_exec, id_user, job_name, dt_exec, exec_return, sucess,
                     finished FROM job_exec_history WHERE id_user = %s LIMIT 100'''
            self.cur.execute(sql, (user['id_user']))
            jobs_hist = []
            for (id_exec, id_user, job_name, dt_exec, exec_return, sucess, finished) in self.cur:
                job = {
                    'id_exec': id_exec,
                    'id_user': id_user,
                    'job_name': job_name,
                    'dt_exec': dt_exec,
                    'exec_return': exec_return,
                    'sucess': sucess,
                    'finished': finished
                }
                jobs_hist.append(job)
            return jobs_hist
        except:
            raise

    def get_user_jobs(self, user):
        sql = '''
                SELECT 
                    job.id_job, 
                    job.nm_Job 
                FROM job_user_permission
                    INNER JOIN job
                            ON job.id_job = job_user_permission.id_job
                WHERE job_user_permission.cd_user_Type = %s'''
        self.cur.execute(sql, (user['id_user']))
        jobs = []
        for (id_job, nm_Job) in self.cur:
            job = {
                'id_job': id_job, 
                'nm_Job': nm_Job
            }
            jobs.append(job)
        return jobs

    def update_exec(self, id_exec, job, user, exec_return, success):
        sql = '''
            UPDATE job_exec_history
               SET 
                exec_return = %s,
                sucess = %s,
                finished = true
            WHERE id_exec = %s
              AND id_user = %s
              AND job_name = %s
              AND finished IS NULL '''
        self.cur.execute(sql, (exec_return, success, id_exec, user['id_user'], job['job_name']))