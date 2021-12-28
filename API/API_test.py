# import requests
# import json
# resposnse =requests.get("https://api.stackoverflow.com/2.3/questions/")
# print(resposnse)
# resposnse.raise_for_status()  # raises exception when not a 2xx response
#
# if resposnse.status_code != 204:
#     with open('resposnse.json', 'a') as f:
#         f.write(str(resposnse.content))
#
# for data in resposnse.json():
#      print(data)
#
#
#
#
# #   if resposnse.status_code != 204:
# #    resposnse.decode('utf-8').replace('\0', '')
# # for data in resposnse.json()['items']:
# #     print(data)
# # open('data.json', 'a') as file:
# #     file.write(resposnse)


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
