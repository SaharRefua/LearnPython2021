import requests
import json
resposnse =requests.get("https://api.stackoverflow.com/2.3/questions/")
print(resposnse)
resposnse.raise_for_status()  # raises exception when not a 2xx response

if resposnse.status_code != 204:
    with open('API/resposnse.json', 'w') as f:
        f.write(str(resposnse.content))


   # if resposnse.status_code != 204:
#    resposnse.decode('utf-8').replace('\0', '')
# for data in resposnse.json()['items']:
#     print(data)
# open('data.json', 'a') as file:
#     file.write(resposnse)
