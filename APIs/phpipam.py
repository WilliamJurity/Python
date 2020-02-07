import json
import requests

api_url_base = 'compos-ip.compos.com.br/api/compos'
api_user = 'api'
api_password = 'SXqoVoBPbv'
headers = {'Content-Type': 'application/json'}

def get_auth():
    api_url = f'https://{api_user}:{api_password}@{api_url_base}/user/'
    response = requests.post(api_url, headers=headers)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        None

auth = get_auth()
token = auth['data']['token']
headers.update({'phpipam-token': token})

def get_devices():
    api_url = f'https://{api_user}:{api_password}@{api_url_base}/devices/'
    response = requests.get(api_url, headers=headers)
    return json.loads(response.content.decode('utf-8'))

def get_subnets():
    api_url = f'https://{api_user}:{api_password}@{api_url_base}/subnets/custom_fields/'
    response = requests.get(api_url, headers=headers)
    return json.loads(response.content.decode('utf-8'))

def revokeToken():
    api_url = f'https://{api_user}:{api_password}@{api_url_base}/user/'
    response = requests.delete(api_url, headers=headers)
    return json.loads(response.content.decode('utf-8'))

devices = get_devices()

print(devices["data"])


print(revokeToken())