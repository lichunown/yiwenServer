
class MessageData():
    def __init__(self,mfrom = None, data = None):
        self.mfrom = mfrom
        self.data = data

class Messages():
    def __init__(self):
        self.mess = {}
    def addmessage(self,user,data):
        if self.mess.get(user) is None:
            self.mess[user] = []
        self.mess[user].append(data)

    def getmeaages(self,user):
        return self.mess.get(user)

tmpMessages = Messages()