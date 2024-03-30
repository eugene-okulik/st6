import random
import unittest
import requests


class TestPublicationsAPIWithPrecondition(unittest.TestCase):

    def setUp(self):
        print('preparing test data')
        payload = {
            "title": "My title",
            "Body": "My publication content",
            "userId": 1
        }
        headers = {
            'Content-type': 'application/json'
        }
        response = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload, headers=headers)
        self.post_id = response.json()['id']
        print('finishing preparing test data')
        print(f'publication with post id {self.post_id} created')

    def tearDown(self):
        requests.delete(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}')
        print(f'Post {self.post_id} deleted')

    @staticmethod
    def generate_title():
        return random.choice(['sdfsdf', 'sdfsd', 'sdsdfs'])

    def test_get_by_id(self):
        print('Test is running')
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}')
        self.assertEqual(response.status_code, 200, 'Status code is not Ok')
        self.assertEqual(response.json()['id'], self.post_id)


class TestPublicationAPIWoutPrecond(unittest.TestCase):
    def test_create_publication(self):
        payload = {
            "title": "My title",
            "Body": "My publication content",
            "userId": 1
        }
        headers = {
            'Content-type': 'application/json'
        }
        response = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload, headers=headers)
        self.assertEqual(response.status_code, 201, 'Status code is not Ok')
        self.assertEqual(response.json()['title'], payload['title'], 'Invalid title')
