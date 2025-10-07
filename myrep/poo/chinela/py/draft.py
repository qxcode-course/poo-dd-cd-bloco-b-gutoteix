class Chinela:
    def __init__(self) -> None:
        self.__tamanho = 0  
    
    def __str__(self):
         return f"Tamanho da chinela é: {self.__tamanho}"

    def set_tamanho(self, valor: int) -> None: 
            if valor % 2 == 0 and valor >= 20 and valor <= 50:
                self.__tamanho = valor
        
    def get_tamanho(self) -> int: 
        return self.__tamanho

def main():
    while True:
        chinela = Chinela() 
        print("Informe o tamanho da chinela")
        line = int(input())
        chinela.set_tamanho(line)
    
        if line < 20 or line > 50:
             print("Error!!! Valor inválido")
             break
        
        print(chinela)
        break
main()



