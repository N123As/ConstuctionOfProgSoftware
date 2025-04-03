from colorama import Fore, Style, init
init(autoreset=True)

class lg:#beautiful colorful texts
    def log(self, msg):
        print(Fore.GREEN + msg) 
    def err(self, msg):
        print(Fore.RED + msg) 
    def wrn(self, msg):
        print(Fore.YELLOW + msg) 

class fw:
    def w(self, txt):
        with open("log.txt","a") as f:
            f.write(txt)
    def wl(self, txt):
        with open("log.txt", "a") as f:
            f.write(txt +"\n")

class flg:
    def __init__(self,writer):
        self.wr = writer    
    def log(self, msg): 
        self.wr.wl("LOG: "+ msg)
    def err(self, msg):    
        self.wr.wl("ERR: "+ msg)
    def wrn(self, msg): 
        self.wr.wl("WRN: "+ msg)

if __name__ == "__main__":
    l = lg()
    l.log("all good")
    l.err("fatal crash")
    l.wrn("not optimal")

    f = flg(fw())
    f.log("file ok")
    f.err("file missing")
    f.wrn("low space")
