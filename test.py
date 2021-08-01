import requests

BASE = "http://127.0.0.1:5000/"

data = [{'likes':100, 'name':'Tim', 'views':202020}, 
        {'likes':1000, 'name':'Kenneth', 'views':200},
        {'likes':10, 'name':'HOW to make rest api', 'views':21000}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

response = requests.delete(BASE, "video/0")
print(response)
input()
response = requests.get(BASE + "video/6")
print(response.json())
