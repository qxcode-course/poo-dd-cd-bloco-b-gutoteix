class Bateria:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.carga = capacidade
    
    def mostrar(self):
        print(f"({self.carga}/{self.capacidade})")

class Carregador:
    def __init__(self, potencia):
        self.potencia = potencia
    
    def mostrar(self):
        print(f"Carregador {self.potencia}W")

class Notebook:
    def __init__(self):
        self.ligado = False
        self.bateria = None
        self.carregador = None

    def ligar(self):
        if (self.bateria and self.bateria.carga > 0) or self.carregador:
            self.ligado = True
            print("Notebook ligado")
        else:
            print("Não foi possível ligar")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print("Notebook desligado")

    def mostrar(self):
        s = "Ligado" if self.ligado else "Desligado"
        b = f"({self.bateria.carga}/{self.bateria.capacidade})" if self.bateria else "Sem bateria"
        c = f"{self.carregador.potencia}W" if self.carregador else "Sem carregador"
        print(f"{s} | Bateria: {b} | Carregador: {c}")

    def usar(self, tempo):
        if not self.ligado:
            print("Notebook desligado")
            return
        if self.bateria:
            if self.bateria.carga <= 0:
                print("Notebook descarregado")
                self.desligar()
            else:
                self.bateria.carga -= tempo
                print(f"Usando por {tempo} minutos")
        elif self.carregador:
            print("Usando ligado no carregador")
        else:
            print("Sem energia para usar")

def main():
    nb = Notebook()
    nb.mostrar()
    nb.ligar()

    b = Bateria(50)
    nb.bateria = b
    nb.ligar()
    nb.usar(10)
    nb.mostrar()

    c = Carregador(2)
    nb.carregador = c
    nb.mostrar()

main()
