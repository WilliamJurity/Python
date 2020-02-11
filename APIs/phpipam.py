import json
import requests

class phpipamAPI(object):
    headers = {'Content-Type': 'application/json'}
    def __init__(self, api_user, api_password, your_app, server):
        self.api_url_base = f'{server}/api/{your_app}'
        self.api_url = f'https://{api_user}:{api_password}@{self.api_url_base}'

    @property
    def login(self):
        try:
            response = requests.post(f'{self.api_url}/user/', headers=phpipamAPI.headers)
            if response.status_code == 200:
                self.result = json.loads(response.content.decode('utf-8'))
                self.token = self.result['data']['token']
                self.tokenExpire = self.result['data']['expires']
                self.authCod = self.result['code']
                phpipamAPI.headers.update({'phpipam-token': self.token})
                return self.result["success"]
            else:
                erro = json.loads(response.content.decode('utf-8'))
                return erro['message']
        except:
            raise print('Ocorreu um erro ao se conectar com o servidor.')

    def get_devices(self):
        try:
            response = requests.get(f'https://{self.api_url_base}/devices/', headers=phpipamAPI.headers)
            if response.status_code == 200:
                self.result = json.loads(response.content.decode('utf-8'))
                return self.result['data']
            else:
                erro = json.loads(response.content.decode('utf-8'))
                return erro['message']
        except:
            raise print('Ocorreu um erro ao se conectar com o servidor.')

    def logout(self):
        try:
            response = requests.delete(f'{self.api_url}/user/', headers=phpipamAPI.headers)
            if response.status_code == 200:
                result = json.loads(response.content.decode('utf-8'))
                return result
            else:
                erro = json.loads(response.content.decode('utf-8'))
                return erro['message']
        except:
            print('Ocorreu um erro ao se conectar com o servidor.')

api_user = 'api'
api_password = 'SXqoVoBPbv'
server = 'compos-ip.compos.com.br'
app = 'compos'
ipam = phpipamAPI(api_user,api_password,app,server)

ipam.login
print(ipam.get_devices())
print(ipam.logout())