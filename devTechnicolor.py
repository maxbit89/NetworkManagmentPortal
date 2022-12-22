from Device import Device
import requests
from lxml import html

class DeviceTechnicolorModem(Device):
    def __init__(self, host):
        super().__init__()
        self.host = host
    
    def login(self, identity):
        #Get CSRFValue
        url = 'http://'+self.host+'/'
        page = requests.get(url)
        if not(page.status_code == 200):
            raise Exception("HTTP not accessable!")
        tree = html.fromstring(page.content)
        CSRFValue = tree.xpath("//form/input")[0].get("value", "")

        #login
        credentials = identity.getCredential(self.__class__)
        pload = {'CSRFValue':CSRFValue, 'loginUsername':credentials.username, 'loginPassword':credentials.password, 'logoffUser': '1'}
        resp = requests.post(url+'goform/login',data = pload)
        if not(resp.status_code == 200):
            raise Exception("HTTP not accessable!")
        with open("debug.htm", "wb") as file:
            file.write(resp.content)

    def getConfiguration(self, saveFile):
        url = 'http://'+self.host+'/GatewaySettings.bin'
        download = requests.get(url)
        with open(saveFile, "wb") as file:
            file.write(download.content)
    
    def setConfiguration(self, uploadFile):
        #Get CSRFValue
        url = 'http://'+self.host+'/RgBackupRestore.asp'
        page = requests.get(url)
        tree = html.fromstring(page.content)
        CSRFValue = tree.xpath("//form/input")[0].get("value", "")
        print(CSRFValue)
        
        #upload configuration
        url = 'http://'+self.host+'/goform/RgBackupRestore'
        files = {'ImportFile': open(uploadFile, "rb")}
        values = {'CSRFValueRestore': CSRFValue}

        resp = requests.post(url, files=files, data=values)
        if not(resp.status_code == 200):
            raise Exception("HTTP not accessable!")
