from locust import TaskSet, task, tag, between

from common import config


class APIUserBehavior(TaskSet):
	wait_time = between(5, 10)


	def __init__(self, parent):
		super(APIUserBehavior, self).__init__(parent)
		self.headers = config.HEADERS


	@task(30)
	def api_test_1(self):
		pass

	@task(30)
	def api_test_2(self):
		pass
