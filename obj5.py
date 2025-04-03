class ln:
    def html(self): pass
    def inr(self): pass

class ltxt(ln):
    def __init__(self, txt):
        self.txt = txt
    def html(self):
        return self.txt
    def inr(self):
        return self.txt

class classss(ln):
    def __init__(self, tag, block=True, 
    selfclose=False):
        self.tag = tag
        self.block = block
        self.selfclose = selfclose
        self.cls = []
        self.children = []
    def add_class(self, c):
        self.cls.append(c)
        
    def add(self, node):
        self.children.append(node)
        return self
    def html(self):
        cls = f' class="{' '.join(self.cls)}"' if self.cls else ''
        if self.selfclose:
           # return f"<{self.tag}{cls}/>">
            return f"<{self.tag}{cls}/>"
        inner = ''.join([n.html() for n in self.children])
        return f"<{self.tag}{cls}>{inner}</{self.tag}>"
    def inr(self):
        return ''.join([n.html() for n in self.children])
    def count(self):
        return len(self.children)

if __name__ == "__main__":
    ul = classss("ul")
    ul.add_class("menu")
    ul.add(classss("li")).add(ltxt("Home"))
    ul.add(classss("li")).add(ltxt("About"))
    ul.add(classss("li")).add(ltxt("Contact"))
    
    print("==| Outer HTML |==")
    print(ul.html())
    print("\n==| Inner HTML |==")
    print(ul.inr())
    print("\n==| Children Count |==")
    print(ul.count())

