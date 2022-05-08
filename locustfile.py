from locust import HttpUser, task, between


class FdnTest(HttpUser):
    # * wait_timeis used to specify how long a simulated user should wait between executing tasks,
    # *and the decorator task is used to specify that the hello_world method is a task that should get executed by the simulated user.
    wait_time = between(0.5, 2.5)

    #cek lansung /
    # @task
    # def hello_world(self):
    #      self.client.get('/')

    # @task
    # def auth_login(self):
    #     with self.client.post(
    #         '/auth/login',
    #         json={"username": "superadmin", "password": "fdntendean34"},
    #         catch_response=True
    #     ) as response:
    #         datas = response.json()["data"]["token"]
    #         if datas: 
    #             print("TOKEN TRUE")
    #         else:
    #             print("TOKEN FALSE:", response.json()["data"]["token"])
    #             response.failure("Did not get expected value in greeting")


    @task
    def predefined(self):
         self.client.get('https://api.femaledaily.com/app/v2/user/predefined')
