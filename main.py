
# habit tracker : using "PIXELA API"

import requests
from datetime import datetime

ID= "graph1"
USER_NAME= "abc"
TOKEN= "jkffcjhghghvhgh"
PIXELA_POST_ENDPOINT= "https://pixe.la/v1/users"
PARAMETERS= {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

#graph :
GRAPH_ENDPOINT= f"{PIXELA_POST_ENDPOINT}/{USER_NAME}/graphs"
GRAPH_PARAMETERS= {
    "id": ID,
    "name":"my cycling graph",
    "unit":"Km",
    "type":"float",
    "color": "ajisai"
}

#request header:it provide authentication via this special token made by us
headers= {
    "X-USER-TOKEN":TOKEN	
}

# https://pixe.la/v1/users/username/id/graph1.html  == link to open the graph in browser, user_name and id is needed

#posting a pixel:
current_time= datetime.now() ##autofilling date usign datetime


PIXEL_ENDPOINT= f"{PIXELA_POST_ENDPOINT}/{USER_NAME}/graphs/{ID}"
PIXEL_PARAMETERS={
    "date": current_time.strftime("%Y%m%d"), #we have formatted date time using strftime
    "quantity": input("How many km did u run today?")

}
response= requests.post(url= PIXEL_ENDPOINT, json=PIXEL_PARAMETERS, headers=headers)
print(response.text)

