import paramiko
from PyQt5 import QtWidgets

class RemoteConnection(QtWidgets.QWidget):
    def __init__(self, host, username, password):
        super().__init__()
        self.host = '192.168.0.177'
        self.username = 'root'
        self.password = 'lktime-dev'

        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.load_system_host_keys()
        self.client.connect(self.host, username=self.username, password=self.password)

    def run_command(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        return stdout.read()

    def close(self):
        self.client.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    conn = RemoteConnection("192.168.0.177", "root", "lktime-dev")
    output = conn.run_command(input())
    print(output)
    conn.close()
