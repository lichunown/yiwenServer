import hashlib,random  

# m2 = hashlib.md5()   
# m2.update(src)   
# print m2.hexdigest()  

class Token(object):
    def __init__(self):
        self._loginTokens = {}
        self._md5 = hashlib.md5() 
    def createToken(self,user):
        self._md5.update(str(user.username)+str(random.random()))
        self._loginTokens[str(self._md5.hexdigest())] = user
        return str(self._md5.hexdigest())
    def getUser(self,token):
        return self._loginTokens.get(str(token))
    def dropToken(self,token):
        print self._loginTokens
        try:
            user = self._loginTokens.pop(token)
            return user
        except KeyError:
            return None

userToken = Token()