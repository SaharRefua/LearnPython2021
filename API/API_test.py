# import requests
# import json
# response =requests.get("https://api.stackoverflow.com/2.3/questions/")
# print(response)
# response.raise_for_status()  # raises exception when not a 2xx response
#
# if response.status_code != 204:
#     with open('response.json', 'a') as f:
#         f.write(str(response.content))
#
# for data in response.json():
#      print(data)
#
#
#
#
# #   if response.status_code != 204:
# #    response.decode('utf-8').replace('\0', '')
# # for data in response.json()['items']:
# #     print(data)
# # open('data.json', 'a') as file:
# #     file.write(response)


import requests

# response = requests.get("https://api.github.com")
#
# print(f"My response is: {response}")
# print(f"My Response JSON is: {response.json()}")
#
# response = requests.get("https://api.github.com/user/keys")
# for data in response.json():
#     if "message" in data:
#         print("Found")
myobj = {'userId': 11, 'id': 201, 'title': 'Test Just fake name'}

response = requests.get('https://jsonplaceholder.typicode.com/todos')
response = requests.get('https://jsonplaceholder.typicode.com/posts')
post = requests.post('https://jsonplaceholder.typicode.com/posts',data = myobj, timeout=2.50)
print(post)

response = requests.get('https://jsonplaceholder.typicode.com/posts')
for data in response.json():
    print(data)
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))
