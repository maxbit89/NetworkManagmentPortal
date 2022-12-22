import json

class CredentialUsernamePassword():
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Identity:
    def __init__(self, name):
        self.name = name
        self.credentials = {}
    
    def addCredential(self, capType, credential):
        capType = type(capType)
        if capType in self.credentials:
            raise Exception("There is already Credentials for this Capability")
        else:
            self.credentials[capType] = credential
        
    def getCredential(self, capType):
        capType = type(capType)
        return self.credentials[capType]
        
def importCredential(savename):
    with open("./confidential/"+savename+".json", "r") as file:
        jsonContent = file.read()
        return json.loads(jsonContent)

if __name__ == "__main__":
    import sys
    print(" ".join(sys.argv))
    
    def printHelp():
        print("%s genCred <savename> <username> <password>" % (sys.argv[0]))
    
    if len(sys.argv) != 5:
        printHelp()
        exit(-1)
    if sys.argv[1] == "genCred":
        savename = sys.argv[2]
        if "/" in savename or "." in savename:
            printHelp()
            exit(-1)
        with open("./confidential/"+savename+".json", "w") as file:
            credential = CredentialUsernamePassword(sys.argv[3], sys.argv[4])
            data = json.dumps(credential, default=lambda o: o.__dict__)
            file.write(data)
    else:
        printHelp()
        
