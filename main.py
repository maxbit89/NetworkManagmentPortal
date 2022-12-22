import requests
from devTechnicolor import DeviceTechnicolorModem
from Identity import Identity, CredentialUsernamePassword, importCredential

print("Backing up Modem")
modemDocsys = DeviceTechnicolorModem("192.168.1.1")
idCoreNetworkManager = Identity("CoreNetworkManager")
idCoreNetworkManager.addCredential(DeviceTechnicolorModem, importCredential("modem01"))
modemDocsys.login(idCoreNetworkManager)
modemDocsys.getConfiguration("modemConfig.bin")
#modemDocsys.setConfiguration("org_modemConfig.bin")

print("Backing up CoreRouter")

