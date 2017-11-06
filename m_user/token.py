#encoding:utf-8
import hashlib,random  

# m2 = hashlib.md5()   
# m2.update(src)   
# print m2.hexdigest()  

class Token(object): 
    def __init__(self):
        self._loginTokens = {}
        self._logingUser = {}
        self._md5 = hashlib.md5() 
    def createToken(self,user):
        self._md5.update((str(user.username)+str(random.random())).encode())
        token = str(self._md5.hexdigest())
        if self._logingUser.get(user):
            print("重复登陆 %s"%user.username)
            del self._loginTokens[self._logingUser[user]]
        self._logingUser[user] = token
        self._loginTokens[token] = user
        return str(token)
    def getUser(self,token):
        return self._loginTokens.get(str(token))
    def dropToken(self,token):
        try:
            user = self._loginTokens.pop(token)
        except KeyError:
            return None
        del self._logingUser[user]
        return user

userToken = Token()