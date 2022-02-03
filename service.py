import requests
from variables import KEY, TOKEN

def trello(event):
    key = KEY
    token = TOKEN
    name = event['name']
    desc = event['desc']

    if event['list'] == 'task':
        id_list = '61fbeb68e1d100417ca760a6'

    if event['list'] == 'bug':
        id_list = '61fbf10b130b6388f6ad7361'

    if event['list'] == 'issue':
        id_list = '61fbf46d8053b619566baa54'

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

