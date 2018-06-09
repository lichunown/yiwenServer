
class MessageData():
    def __init__(self,mfrom = None, data = None):
        self.mfrom = mfrom
        self.data = data

class Messages():
    def __init__(self):
        self.mess = {}
    def addmessage(self,user,data):
        print('add to:',user)
        if self.mess.get(user) is None:
            self.mess[user] = []
        self.mess[user].append(data)

    def getmeaages(self,user):
        print('get from',user)
        return self.mess.get(user)

    def cleanmessages(self, user):
        self.mess[user] = []

tmpMessages = Messages()