from locust import HttpUser, task, between
import random

class MyApiUser(HttpUser):
    wait_time = None
    def on_start(self):
        pass
    @task
    def change_user_balance(self):
        user_id = random.randint(1, 100000)
        with self.client.get(f"/users/{user_id}", 
                              catch_response=True, 
                              name="/users") as response:
            if response.status_code != 200:
                response.failure(f"Got status code {response.status_code}")