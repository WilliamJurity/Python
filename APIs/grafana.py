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

