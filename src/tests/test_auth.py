import unittest
from main import create_app, db


class TestAuth(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.app = create_app()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()
        db.create_all()

        runner = cls.app.test_cli_runner()
        runner.invoke(args=["db", "seed"])

    @classmethod
    def tearDown(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    def test_auth_register(self):
        response = self.client.post("/auth/register", json={
            "email": "admin2@test.com",
            "password": "123456",
            "admin": "True"
        })

        data = response.get_json()
        self.assertTrue(bool(response.status_code >= 200 and response.status_code < 300))
        self.assertIsInstance(data, dict)
        self.assertTrue(bool("id" in data.keys()))

        response = self.client.post("/auth/register", json={
            "email": "admin1",
            "password": "1234567",
            "admin": "True"
        })

        data = response.get_json()
        self.assertTrue(response.status_code == 400)

    def test_auth_login(self):
        response = self.client.post("/auth/login", json={
            "email": "admin@test.com",
            "password": "123456",
        })

        data = response.get_json()
        self.assertTrue(bool(response.status_code >= 200 and response.status_code < 300))
        self.assertIsInstance(data, dict)
        self.assertTrue(bool("token" in data.keys()))

        response = self.client.post("/auth/login", json={
            "email": "admin@test.com",
            "password": "duck",
        })

        data = response.get_json()
        self.assertTrue(bool(response.status_code >= 400 and response.status_code < 500))
