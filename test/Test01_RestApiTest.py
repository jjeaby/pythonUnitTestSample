import unittest
import json

from app import run


class RestApiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        run.app.testing = True
        cls.app = run.app.test_client()
        with run.app.app_context():
            run.app

        cls.app.preserve_context = run.app.test_client().preserve_context
        # execute before class

    def setUp(self):
        # execute before every test case
        pass

    def tearDown(self):
        # execute after every test case
        pass

    def test01_Index_RestAPI_Test(self):
        response = self.app.get('/')
        self.assertEqual(b'Hello World!', response.data, "Index RestApi Test 실패")

    def test02_getInfo_RestAPI_Test(self):
        response = self.app.get('/getInfo', query_string=dict(query='getInfoRestApi'))

        expectResponse = {}
        expectResponse["query"] = "getInfoRestApi"
        expectResponse["status"] = 200

        expectResponseJson = json.dumps(expectResponse, ensure_ascii=False).encode(encoding="utf-8")

        self.assertEqual(expectResponseJson, response.data, "getInfo RestApi Test 실패")

    def test03_postInfo_RestAPI_Test(self):
        postText = {
            "query": "Post Info Rest Api",
            "status": 200
        }

        response = self.app.post('/postInfo', json=postText)

        expectResponse = {
            "query": "Post Info Rest Api",
            "status": 200
        }

        self.assertEqual(expectResponse, response.json, "postInfo RestApi Test 실패")
