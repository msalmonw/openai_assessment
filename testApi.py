import requests

class TestAPI:
    def testCreatePrompt(self):
        url = 'http://localhost:5000/prompt'
        data = {'prompt': "What is Flask framework?"}
        response = requests.post(url, json=data)
        print(response.text)

    def testGetResponse(self):
        url = 'http://localhost:5000/response'
        data = {'index': 0}
        response = requests.post(url, json=data)
        print(response.text)

    def testUpdate(self):
        url = 'http://localhost:5000/update'
        data = {'index': 0, 'prompt': 'What is django?'}
        response = requests.post(url, json=data)
        print(response.text)

    def testDelete(self):
        url = 'http://localhost:5000/delete'
        data = {'index': 1}
        response = requests.post(url, json=data)
        print(response.text)


if __name__ == '__main__':
    import time
    test = TestAPI()
    test.testCreatePrompt()
    time.sleep(5)
    test.testCreatePrompt()
    time.sleep(5)
    test.testGetResponse()
    time.sleep(5)
    test.testUpdate()
    time.sleep(5)
    test.testDelete()