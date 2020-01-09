from paramiko import SSHClient
import paramiko

class SSH():
    def __init__(self, host, usuario, senha, porta):
        self.ssh=SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=host, username=usuario, password=senha, port=porta)

    def exec_cmd(self, cmd):
        stdin,stdout,stderr = self.ssh.exec_command(cmd)
        if stderr.channel.recv_exit_status() != 0:
            print(stderr.read().decode('UTF-8'))
        else:
            return stdout.read().decode("UTF-8")

    def close(self):
        self.ssh.close()

if __name__ == '__main__':
    cmd = "/interface print"
    ssh = SSH(host='192.168.122.82',usuario='admin',senha='',porta='22')
    result = ssh.exec_cmd(cmd)
    ssh.close()
    print(result)
    linhas = result.split("\n")
    last = len(linhas) - 3
    print(linhas[last])