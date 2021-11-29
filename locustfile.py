from locust import FastHttpUser

from locustfiles import mobile, api, web


class TestUser(FastHttpUser):
	tasks = {
		mobile.MobileAppBehavior: 30,
		api.APIUserBehavior: 25,
		web.WebUserBehavior: 20
	}
