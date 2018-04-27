import unittest
import handler as JenkinsJobsHandler

class TestJenkinsJobsHandler(unittest.TestCase):

    def setUp(self):
        self.app = JenkinsJobsHandler.app.test_client()

    # Deve testar a listagem de jobs
    def test_job_list(self):
        response = self.app.get('/jobs')
        self.__test_job_list_status(response)
        json_data = response.get_json()
        print json_data
    
    def __test_job_list_status(self, response):
        self.assertEqual(200, response.status_code)

if __name__ == '__main__':
    unittest.main()