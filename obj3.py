class rnd:
    def r(self, n): pass

class px(rnd):
    def r(self, n):
        print(f"drawing {n} as pixels")

class vecttt(rnd):
    def r(self, n):
        print(f"drawing {n} as vectors")

class shp:
    def __init__(self,r):
        self.r = r
    def d(self): pass

class circle(shp):
    def d(self):
        self.r.r("circle")
class sqqure(shp):
    def d(self):
        self.r.r("square")
class tr(shp):
    def d(self):
        self.r.r("triangle")
        
#i hope i understood it right?
if __name__ == "__main__":
    a = circle(px())
    b = tr(vecttt())
    c = sqqure(px())
    a.d()
    b.d()
    c.d()
    
    
