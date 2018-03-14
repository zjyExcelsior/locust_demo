from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    """"task set"""

    def on_start(self):
        """on_start is called when a Locust start before any task is scheduled"""
        self.login()

    def login(self):
        self.client.post('/login', {
            'usernmae': 'ellen_key',
            'password': 'education'
        })

    @task(2)
    def index(self):
        self.client.get('/')

    @task(1)
    def profile(self):
        self.client.get('/profile')

    @task(1)
    def my_task(self):
        print("Locust instance (%r) executing my_task" % (self.locust))


class WebsiteUser(HttpLocust):
    """一个类实例代表了一个user"""
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
