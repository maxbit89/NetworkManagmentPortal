class Device:
    def __init__(self):
        self.capabilities = {}
        pass
        
    def getCapabilityName(self, capType):
        return "%s.%s" % (capType.__module__, capType.__name__)
    
    def addCapability(self, capType, capability):
#        print("Add New Capability: %s" % (self.getCapabilityName(capType)))
        if capType in self.capabilities:
            raise Exception("Capability allready known")
        else:
            self.capabilities[capType] = capability
    
    def getCapabilities(self):
        return self.capabilities.keys()
        
    def getCapability(self, capType):
        return self.capabilities[capType]
        
    def backup(self, filePath):
        raise Exception("Not Implemented!")
    
    def restore(self, filePath):
        raise Exception("Not Implemented!")
