from Device import Device

class CredentialSshKeys:
    def __init__(self, keyFile, password):
        self.keyFile = keyFile
        self.password = password
        

class DeviceSsh(Device):
    def __init__(self):
        super().__init__()
        import paramiko
        self.client = paramiko.SSHClient()
        self.client.load_system_host_keys()
        self.addCapability(type(self.client), self.client)

        
    
