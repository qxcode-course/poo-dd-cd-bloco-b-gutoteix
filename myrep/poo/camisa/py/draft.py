class Roupa:
    def __init__(self):
        self.__tamanho = ""
    
    def __str__(self):
         return f"O tamanho da sua roupa é: {self.__tamanho}"
    
    def set_tamanho(self, valor: int) -> None: 
                if valor != "PP" and valor != "P" and valor != "M" and valor != "G" and valor != "GG" and valor != "XG":
                    print("Valor não permitido! Apenas PP, P, M, G, GG e XG")
                    return
                
                self.__tamanho = valor
    def get_tamanho(self) -> int: 
        return self.__tamanho

def main():
    while True:
        roupa = Roupa()
    
        print("Informe o tamanho da roupa")
        line = input()
        roupa.set_tamanho(line)
        
        print(roupa)
        break
main()