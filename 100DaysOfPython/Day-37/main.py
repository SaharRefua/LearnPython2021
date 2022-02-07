import requests
from datetime import datetime
# requests.get()#Get data
# requests.post() #create data
# requests.put() # update data
# requests.delete() #delete data
TOKEN = "daskjdasd798123"
# Create user
create_user_parameters = {
    "token": "daskjdasd798123",
    "username": "sahar",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
pixel_endpoint = "https://pixe.la/v1/users"
# response = requests.post(url=pixel_endpoint, json=create_user_parameters)
# print(response.text)


# Create graph
create_graph_endpoint = "https://pixe.la/v1/users/sahar/graphs"
headers = {
    "X-USER-TOKEN": TOKEN
}

create_graph_parameters = {
    "id": "graph",
    "name": "Sahar graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}

# response = requests.post(url=create_graph_endpoint, json=create_graph_parameters, headers=headers)
# print(response.text)

# Post pixel in graph
post_pixel_endpoint = "https://pixe.la/v1/users/sahar/graphs/graph"

today = datetime.now()
yestrday= datetime(year=2022, month=2, day=5)
today = today.strftime("%Y%m%d")
print(today)
create_pixel_parameters = {
    "date": today,
    "quantity": "5",

}
#"20220206"
#"optionalData": "{\"BusyDay\":\"True\"}"
response = requests.post(url=post_pixel_endpoint, json=create_pixel_parameters, headers=headers)
print(response.text)





#PUT pixel in graph

put_pixel_endpoint = "https://pixe.la/v1/users/sahar/graphs/graph/20220206"
put_pixel_parameters = {
    "quantity": "5"

}
# response = requests.put(url=put_pixel_endpoint, json=put_pixel_parameters, headers=headers)
# print(response.text)

# DELETE pixel in graph
delete_pixel_endpoint = "https://pixe.la/v1/users/sahar/graphs/graph/20220206"


# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)