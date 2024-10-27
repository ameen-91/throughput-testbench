from locust import HttpUser, task

class User(HttpUser):
    @task
    def predict(self):
        self.client.post("predict/",json={"text":"""Scientists have calculated that the chances of something so patently absurd actually existing are millions to one.
But magicians have calculated that million-to-one chances crop up nine times out of ten."""})