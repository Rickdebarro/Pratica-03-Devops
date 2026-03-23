import unittest
from app.app import app

class AppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_print_health_check(self):
        response = self.app.get('/health-check')
        self.assertEqual(200, response.status_code, "Erro no test_http_code!")
        self.assertEqual("<h1>Hello, I'm Alive!</h1>", response.get_data(as_text=True)
                          , "Erro no test_print_health_check!")

    def test_hello_success(self):
        response = self.app.get('/hello?name=Python')
        self.assertEqual(200, response.status_code, "Deveria retornar status 200")
        self.assertEqual("Hello, Python!", response.get_data(as_text=True), "A saudação está incorreta!")
        
    def test_print_hello_error(self):
        response = self.app.get('/hello')
        
        self.assertEqual(response.status_code, 400)
        self.assertIn("Nome não informado", response.data.decode('utf-8'))