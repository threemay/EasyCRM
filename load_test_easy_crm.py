from types import SimpleNamespace
from locust import HttpUser, task, between, events
import logging

class QuickstartUser(HttpUser):
    # wait_time = between(5, 9)
    # cookies = {}

    # @task
    # def index_page(self):
    #     self.client.get("/")

    @task(3)
    def view_organisation(self):
        self.client.get("/organisation/1", cookies=self.cookies)

    def on_start(self):
        files = {
            'username': (None, 'test@gmail.com'),
            'password': (None, 'shh'),
        }
        response = self.client.post("/login/", {"username":"test@gmail.com", "password":"shh"})
        self.cookies = response.cookies

    @events.test_stop.add_listener
    def _(environment, **kw):
        if environment.stats.total.fail_ratio > 0.01:
            logging.error("Test failed due to failure ratio > 1%")
            environment.process_exit_code = 1
        elif environment.stats.total.avg_response_time > 200:
            logging.error("Test failed due to average response time ratio > 200 ms")
            environment.process_exit_code = 1
        elif environment.stats.total.get_response_time_percentile(0.95) > 800:
            logging.error("Test failed due to 95th percentile response time > 800 ms")
            environment.process_exit_code = 1
        else:
            environment.process_exit_code = 0
