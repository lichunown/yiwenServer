import time

class MessageData():
    def __init__(self,mfrom = None, data = None):
        self.mfrom = mfrom
        self.data = data

class Messages():
    def __init__(self):
        self.mess = {}
    def addmessage(self, user, froms, data):
        print('add to:',user)
        if self.mess.get(user) is None:
            self.mess[user] = {}
        if self.mess[user].get(froms) is None:
            self.mess[user][froms] = []
        self.mess[user][froms].append((list(time.localtime(time.time())), data))

    def getmeaages(self,user, froms = None):
        print('get from',user)
        if froms is None:
            r = self.mess.get(user)
        else:
            r = [] if not self.mess.get(user) else self.mess[user].get(froms)
        if self.mess.get(froms) is not None:
            r = (r, self.mess[froms].get(user))
        return r

    def cleanmessages(self, user):
        self.mess[user] = {}

    def listsender(self, user):
        if self.mess.get(user):
            return self.mess[user].keys()
        else:
            return []

tmpMessages = Messages()