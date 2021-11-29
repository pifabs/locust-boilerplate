BASE_URL = "http://localhost:8001"
BASE_PATH = "/custom/api"
API_VERSION = "/v1"
API_TOKEN = ""
X_ACCESS__TOKEN = ""
HEADERS = {
	"accept": "application/json",
	"content-type": "application/json"
}


def get_uri():
	return f"{BASE_URL}{BASE_PATH}{API_VERSION}"
