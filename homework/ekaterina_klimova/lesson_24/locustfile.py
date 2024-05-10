from locust import task, HttpUser


class PublicationUser(HttpUser):
    token = None
    meme_ids = []
    post_ids = []

    def on_start(self):
        response = self.client.post("/authorize", json={"name": "Kate"}).json()
        self.token = response["token"]
        all_memes = self.client.get("/meme", headers={'Authorization': self.token}).json()
        self.meme_ids = [int(i["id"]) for i in all_memes["data"]]

    @task(1)
    def get_meme_by_id(self):
        if self.meme_ids:
            meme_id = self.meme_ids[1]
            self.client.get(f"/meme/{meme_id}")

    @task(3)
    def post_meme(self):
        payload = {
            'text': 'It is meme',
            'url': 'https://ru.pinterest.com/pin/755197431266837222/',
            'tags': ['heheh', 'zhiza'],
            'info': {"cost": 15}
        }
        response = self.client.post("/post/meme", json=payload, headers={'Authorization': self.token}).json()
        self.post_ids.append(int(response["data"]["id"]))

    def on_stop(self):
        for post_id in self.post_ids:
            self.client.delete(f"/DELETE /meme/{post_id}", headers={'Authorization': self.token})
