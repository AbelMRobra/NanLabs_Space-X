import requests
import json
from variables import KEY, TOKEN

def get_list():
    key = KEY
    token = TOKEN
    headers = {"Accept": "application/json"}
    id_board = "61fbd5b7c5ba827c61818ed3"
    url = f"https://api.trello.com/1/boards/{id_board}/lists"
    query = {'key':key, 'token':token}

    responseTrello = requests.request("GET", url, headers=headers, params=query)

    response = {}

    responseData = json.loads(responseTrello.text)
    for data in responseData:
        response[str(data['name']).capitalize()] = data['id']

    return response


def trello(event):
    key = KEY
    token = TOKEN
    name = event['name']
    desc = event['desc']
    id_list = event['list']

    request_type = 'POST'
    url = "https://api.trello.com/1/cards"
    headers = {"Accept": "application/json"}
    query = {'key':key, 'token':token, 'idList': id_list, 'name': name, 'desc':desc, 'idLabels':'61fbf48af555546090a2ad98'}

    response = requests.request("POST", url, headers=headers, params=query)

    if response.status_code == 200:
        message = "Success"
    else:
        message = response.text
    
    return message

