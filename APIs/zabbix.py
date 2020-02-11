import json
import requests
from zabbix_api import ZabbixAPI
from .phpipam import phpipamAPI
teste = phpipamAPI()
teste.api_url()


api_server = 'https://compos-zabbix.compos.com.br'
api_user = 'wjurity'
api_password = 'Kn0w73dg3'

#Instanciando a API
zapi = ZabbixAPI(server = api_server, path="", log_level=6)
zapi.login(api_user, api_password)

hosts = zapi.host.get({"output": hostgroup)
print(len(hosts))
