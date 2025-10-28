class Bateria:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.carga = capacidade

class Carregador:
    def __init__(self, potencia):
        self.potencia = potencia

class Notebook:
    def __init__(self):
        self.ligado = False
        self.bateria = None
        self.carregador = None

    def ligar(self):
        if self.bateria and self.bateria.carga > 0:
            self.ligado = True
            print("notebook ligado")
        else:
            print("não foi possível ligar")

    def usar(self, tempo):
        if not self.ligado:
            print("notebook desligado")
            return
        if self.bateria:
            print(f"usando por {tempo} minutos")
            self.bateria.carga -= tempo
        else:
            print("sem bateria")

    def mostrar(self):
        print("ligado:", self.ligado)
        if self.bateria:
            print("bateria:", self.bateria.carga)

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
