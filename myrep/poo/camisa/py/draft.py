class Roupa:
    def __init__(self):
        self.__tamanho = ""

    def __str__(self):
        return f"O tamanho da sua roupa é: {self.__tamanho}"

    def set_tamanho(self, valor: str) -> bool:
        tamanhos_valido = ["PP", "P", "M", "G", "GG", "XG"]

        if valor not in tamanhos_valido:
            print("Valor não permitido! Apenas PP, P, M, G, GG e XG.")
            return False 

        self.__tamanho = valor
        return True  

    def get_tamanho(self) -> str:
        return self.__tamanho


def main():
    roupa = Roupa() 

    while True:
        print("Informe o tamanho da roupa:")
        line = input().strip().upper()  

        if roupa.set_tamanho(line): 
            break
            
    print(roupa)


main()