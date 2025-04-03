import sys

class ln:
    def html(self): pass

class ltxt(ln):
    def __init__(self, txt):
        self.txt = txt  
    def html(self):
        return self.txt 

class G(ln):
    def __init__(self, tag, cls):
        self.tag = tag
        self.cls = cls
        self.children = []
    def add(self, node):
        self.children.append(node)
        return self
    def html(self):
        c = ''.join([ch.html() for ch in self.children]) 
        return f"<{self.tag} class='{self.cls}'>{c}</{self.tag}>"

class factory:
    _pool = {}
    
    def get(self, tag, cls=""):
        k = (tag, cls)
        if k not in self._pool:
            self._pool[k] = G(tag, cls)
        return self._pool[k]


if __name__ == "__main__":
    f = factory()
    nodes = []
    with open("book.txt", "r",encoding="utf-8") as b:
        for i, line in enumerate(b):
            t = line.strip('\n')
            if not t: continue
            
            if i ==0:
                e = f.get("h1")
            elif len(t) < 20:
                e = f.get("h2")
            elif line.startswith(" "):
                e = f.get("block quote")
            else:
                e = f.get("p")
            n = G(e.tag, e.cls)
            n.add(ltxt(t))
            nodes.append(n)
    
    print("==| HTML Preview |==")
    for n in nodes[:5]: print(n.html())
    
    print("\n==| Mrmory Usage |==")
    total = sys.getsizeof(nodes)
    for n in nodes:
        total +=sys.getsizeof(n) + sum(sys.getsizeof(c) for c in n.children)
    print(f"{total} bytes")

