import re   #реглярні вирази

class strd:
    def read(self, path):
        with open(path, "r",encoding="utf-8") as f: 
            return [list(line.strip()) for line in f.readlines()]   

class chk:
    def __init__(self, target):
        self.t = target
    def read(self, path):
        print(f"opening: {path}")
        try:
            data = self.t.read(path)
            print("Reading complete")
            print("Closing file")
            print(f"lines: {len(data)}")
            print(f"chars: {sum(len(l) for l in data)}")    
            return data
        except Exception as e:
            print("ERROR:", e)
            return []

class lcoker:
    def __init__(self, target,rgx):
        self.t = target
        self.rgx = rgx
    def read(self, path):
        if re.match(self.rgx,path):
            print("access denied!")
            return []
        return self.t.read(path)

if __name__ == "__main__":
    path = "t.txt"
    with open(path, "w",encoding="utf-8") as f: 
        f.write("Ivonchik_VT231\n!")
    
    print("== checker ==")
    c = chk(strd())
    c.read(path)
    
    print("\n== locker ==")
    l = lcoker(strd(), r".*secret.*")
    l.read("secret_data.txt")
    l.read(path)

