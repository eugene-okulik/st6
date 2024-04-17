from locust import task, HttpUser
import random


class PublicationUser(HttpUser):
    post_ids = set()
    token = None

    # def on_start(self):
    #     response = self.client.post('/authorize', json={'name': 'Bob'}).json()
    #     self.token = response['token']

    @task(7)
    def get_all_posts(self):
        self.client.get('/posts', headers={'Authorization': self.token})

    @task(1)
    def create_publication(self):
        payload = {
            "title": "My tile",
            "body": "my body",
            "userId": 1
        }
        response = self.client.post('/posts', json=payload).json()  # noqa F841
        # self.post_ids.add(response['id'])
        self.post_ids.add(random.randrange(1, 100))

    def on_stop(self):
        for post_id in self.post_ids:
            self.client.delete(f'/posts/{post_id}')
