import unittest
import json
import handler as JenkinsJobsHandler

class TestJenkinsJobsHandler(unittest.TestCase):

    def setUp(self):
        self.app = JenkinsJobsHandler.app.test_client()

    # Deve testar a listagem de jobs
    def test_job_list(self):
        response = self.app.get('/jobs')
        self.__test_job_list_status(response)
        json_data = response.get_json()
        self.__test_jobs_list_data(json_data)

    # Deve testar se o status do retorno esta correto.
    def __test_job_list_status(self, response):
        self.assertEqual(200, response.status_code)

    # Deve testar se o retorno esta dentro do esperado.
    def __test_jobs_list_data(self, json_data):
        print(json_data)

    def test_execute_job(self):
        d = dict(data={'job_name': 'Airports'})
        response = self.app.post('/jobs',
            data= json.dumps(d),
            content_type='application/json',)
        self.assertEqual(200, response.status_code)

if __name__ == '__main__':
    unittest.main()