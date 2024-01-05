# import unittest
# from main import app

# class Testapp(unittest.TestCase):
#     def setUp(self):
#         app.testing = True
#         self.app = app.test_client()
#     def test_hello(self):
#         res = self.app.get('/')
#         self.assertEqual(res.status, "200 OK")
#         self.assertEqual(res.data, b"Hello World!\n")

# if __name__ == "__main__":
#     unittest.main()


import pytest
from main import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()
def test_hello(client):
    res = client.get('/')
    assert res.status == '200 OK'
    assert res.data == b'Hello World!\n'

