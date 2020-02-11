dns = {
    'resolver1': '187.18.5.9',
    'resolver2': '187.18.5.10'
}
ntp = {
    'server1': 'compos-ntp1.compos.net.br',
    'server2': 'compos.ntp2.compos.net.br'
}
snmp = {
    'Community': 'composnet',
    'Contact': 'root@compos.net.br',
    'Location': None
}
webserver = {
    'serverPort' : 4080,
    'secureServerPort': 40443
}
class radioUB(object):
    def __init__(self, modelo, mode, sysname):
        self.modelo = modelo
        self.mode = mode
        self.sysname = sysname
    @property
    def login(self):
        pass
    def restart(self):
        pass
    def logout(self, teste):
        pass

file = open('./padrao.conf.bkp', 'r')
linhas = []

for linha in file:
    linha = linha.strip()
    linhas.append(linha)

def grep(string, lista, valuer):
    #result = list()
    for item in lista:
        if string in item:
            result = item.split("=")
            result[1] = valuer
    return result

print(grep("radio.1.rts",linhas, "on"))

file.close()

    # instanciando o objeto
    #newConf = radioUB()
    #newConf.modelo