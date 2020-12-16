import unittest
from main import create_app, db
from models.Profile import Profile


class TestProfiles(unittest.TestCase):
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

    def test_profile_index(self):
        response = self.client.get("/profile/")
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_profile_create(self):
        response = self.client.post("/auth/register",
                                    json={
                                        "email": "test6@test.com",
                                        "password": "123456"
                                    })
        response = self.client.post("/auth/login",
                                    json={
                                        "email": "test6@test.com",
                                        "password": "123456"
                                    })
        data = response.get_json()
        headers_data = {
            "Authorization": f"Bearer {data['token']}"
        }
        data = {
            "username": "lucy",
            "firstname": "test",
            "lastname": "test"
        }
        response = self.client.post("/profile/",
                                    json=data,
                                    headers=headers_data)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        profile = Profile.query.get(data["id"])
        self.assertIsNotNone(profile)
        self.assertEqual(profile.username, "lucy")

    def test_profile_update(self):
        response = self.client.post("/auth/login",
                                    json={
                                        "email": "test5@test.com",
                                        "password": "123456"
                                    })
        data = response.get_json()
        headers_data = {
            "Authorization": f"Bearer {data['token']}"
        }
        profile_data = {
            "username": "updated username",
            "firstname": "test",
            "lastname": "test"
        }
        response = self.client.patch("/profile/5",
                                     json=profile_data,
                                     headers=headers_data)
        data = response.get_json()
        profile = Profile.query.get(data["id"])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(profile.username, "updated username")
        self.assertEqual(response.status_code, 200)

    def test_profile_show(self):
        response = self.client.get("profile/1")
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["id"], 1)
