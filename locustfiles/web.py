from locust import TaskSet, task, between

from common import config


class WebUserBehavior(TaskSet):
	wait_time = between(1, 5)


	def __init__(self, parent):
		super(WebUserBehavior, self).__init__(parent)
		self.headers = config.HEADERS


	def on_start(self):
		self.login()


	def login(self):
		pass


	@task
	def task_1(self):
		pass


	@task
	def task_2(self):
		pass

	@task
	def task_3(self):
		pass