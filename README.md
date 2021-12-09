### Load Testing(https://locust.io/)
Read the docs [here](http://docs.locust.io/en/stable/)

## How to add a new test?
I have divided the test scripts into 3, which are represented by the files under /locustfiles folder.

- api.py     - for load testing backend api's
- mobile.py  - for testing mobile user like behavior
- web.py     - for testing web user like behavior
Feel free to edit common/config.py as needed

## Where to put test files for upload?
You are free to add files of any type in /files folder

## How to run the tests?
```sh
$ locust -f [path to locustfile.py]  --host https://[your target host]
```
Then open the web ui in your browser
