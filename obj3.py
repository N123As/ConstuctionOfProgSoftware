import threading

class Authenticator:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance =super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self,"initialized"):
            self.users ={}
            self.initialized = True
    
    def add_user(self,username,password):
        self.users[username] = password
    
    def authenticate(self,username,password):
        return self.users.get(username) ==password  

if __name__ == "__main__":
    auth1 = Authenticator()
    auth2 = Authenticator()
    
    auth1.add_user("admin","123")
    
    print(auth2.authenticate("admin", "123"))
    print(auth1 is auth2)
    
#output: True
#        True