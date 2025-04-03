class h:
    def __init__(self, n):
        self.n = n
    def dsc(self):
        return self.n

class warrior(h):
    def __init__(self):
        super().__init__("Warrior")

class mage(h):
    def __init__(self):
        super().__init__("Mage")

class p(h):
    def __init__(self):
        super().__init__("Palladin")

class inv:
    def __init__(self, base):
        self.base = base
    def dsc(self):
        return self.base.dsc()

class wd(inv):
    def dsc(self):
        return self.base.dsc() + " with sword" 
class rg(inv):
    def dsc(self):
        return self.base.dsc() + " in armor" 
class af(inv):
    def dsc(self):
        return self.base.dsc() + " holding artifact" 

if __name__ == "__main__":
    a = wd(rg(af(warrior())))
    b = rg(af(mage()))
    c = af(wd(p()))
    print(a.dsc())
    print(b.dsc())
    print(c.dsc())


