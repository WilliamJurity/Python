from random import choice
# from random import randrange

class NewConfigUB(object):
    def __init__(self, template): # Inicialização da classe
        with open(template, 'r') as arquivo: # Abre o arquivo padrão de configuração
            self.espelho = []
            for linha in arquivo: # Adiciona cada linha do arquivo em uma lista
                linha = linha.strip()
                self.espelho.append(linha)

    # Substituição e adição de atributos
    def replaceConfig(self, atributo, valor):
        replace = False
        for l in range(0, len(self.espelho)): # Percorre a lista criado na inicialização procurando o atributo que será adicionado / substituido
            if atributo in self.espelho[l]:
                explode = self.espelho[l].split("=") # Separa o item encontrado, altera o atributo e devolve a lista
                explode[1] = valor
                self.espelho[l] = f'{explode[0]}={explode[1]}'
                replace = True
        if not replace: # Se o atributo não existir, adiciona.
            self.addConfig(atributo, valor)

    # Adiciona um atributo dentro da lista
    def addConfig(self, atributo, valor):
        self.espelho.append(f'{atributo}={valor}')

    # Cria um novo arquivo de configuração com base no espelho criado com as modificações.
    def get_newConfig(self):
        with open('./new_arquivo.conf', 'w') as newFile:
            for parametro in self.espelho:
                newFile.write(f'{parametro}\n')

    # Retorna uma sequencia de caracteres para servir uma senha ou chave
    def new_key(self, lenth=12):
        base = "0123456789abcdefghijlmnopqrstuvxzkwYABCDEFGHIJLMNOPQRSTUVXZKWY!#$%*()-_=+"
        passwd = ''
        for char in range(0, lenth):
            passwd += choice(base)
        return passwd # .join([chr(randrange(48, 122)) for x in range(0, lenth)])

newConf = NewConfigUB("./padrao.conf.bkp")
print(newConf.espelho)
newConf.replaceConfig("vlan.status", "enable")
newConf.replaceConfig("gui.language", "pt-br")
newConf.replaceConfig("aaa.1.devname", "ath2")
newConf.replaceConfig("resolv.host.1.name", "NanoBridge")
print(newConf.espelho)
print(newConf.new_key(lenth=10))

configs = {
    'wireless': [{
        'ssid': 'CMSSIDPADRAO',
        'channel': '40',
        'frequency': 'auto',
        'secure': [dict(auth='wpa2', cripto='eap')]
    }],

    'network': [{

    }],
    'services': [{

    }],
    'sistema': [{

    }]
}

config = {
    'init' : 'configuração padrão',
    'replace': 'substitui parâmetros',
    'get_config': 'obtem a nova configuração',
    'get_pass': 'obtem uma sequencia de caracteres (senhas)'

}
