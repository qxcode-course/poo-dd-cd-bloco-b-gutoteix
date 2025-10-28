class Lead:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.thickness = thickness
        self.hardness = hardness
        self.size = size

    def usagePerSheet(self) -> int:
        if self.hardness == "HB":
            return 1
        elif self.hardness == "2B":
            return 2
        elif self.hardness == "4B":
            return 4
        elif self.hardness == "6B":
            return 6
        return 0

    def __str__(self):
        return f"[{self.thickness}:{self.hardness}:{self.size}]"

class Pencil:
    def __init__(self, thickness: float):
        self.thickness = thickness
        self.tip = None  

    def hasGrafite(self) -> bool:
        return self.tip is not None

    def insert(self, lead: Lead):
        if self.hasGrafite():
            print("fail: ja existe grafite")
            return
        if lead.thickness != self.thickness:
            print("fail: calibre incompativel")
            return
        self.tip = lead
    def remove(self):
        if not self.hasGrafite():
            print("fail: nao existe grafite")
            return None
        removed = self.tip
        self.tip = None
        return removed

    def writePage(self):
        if not self.hasGrafite():
            print("fail: nao existe grafite")
            return

        gasto = self.tip.usagePerSheet()

        if self.tip.size <= 10:
            print("fail: tamanho insuficiente")
            return
        final = self.tip.size - gasto

        if final < 10:
            self.tip.size = 10
            print("fail: folha incompleta")
            return

        self.tip.size -= gasto

    def __str__(self):
        grafite = str(self.tip) if self.tip else "null"
        return f"calibre: {self.thickness}, grafite: {grafite}"


def main():
    pencil = None
    while True:
        try:
            line = input()
        except EOFError:
            break
        if not line:
            continue
       
        if line.startswith("$"):
            echo = line
        else:
            echo = f"${line}"
        print(echo)
        args = line.split()
        
        if args[0].startswith("$"):
            args[0] = args[0][1:]

        if args[0] == "end":
            break
        elif args[0] == "init":
            calibre = float(args[1])
            pencil = Pencil(calibre)
        elif args[0] == "show":
            if pencil is None:
                print("calibre: None, grafite: null")
            else:
                print(pencil)
        elif args[0] == "insert":
            calibre = float(args[1])
            dureza = args[2]
            tamanho = int(args[3])
            lead = Lead(calibre, dureza, tamanho)
            pencil.insert(lead)
        elif args[0] == "remove":
            pencil.remove()
        elif args[0] == "write":
            pencil.writePage()
main()
