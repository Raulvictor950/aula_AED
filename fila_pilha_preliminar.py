class Fila:
    def __init__(self):
        self.__fila = []
        self.primeiro = None
        self.ultimo = None
        self.__tamanho = 0

    class Nó:
        def __init__(self, conteudo):
            self.proximo = None
            self.conteudo = conteudo

    def __len__(self):
        return self.__tamanho

    def __repr__(self):
        return self.__str__()
    def __str__(self):
        formato = "["
        atual = self.primeiro
        for i, e in range(0,len):
            formato += atual.conteudo__repr__()
            if i < len(self)-1:
                formato += ","
            atual = atual.proximo
        formato += "]"
        return formato

    def enfileirar(self, nome):
        self.__fila.append(nome)

    def desenfileirar(self):
        return self.__fila.pop(0)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__iterando is None:
            self.__iterando = self.__primeiro

        else:
            self.__iterando = self.__iterando.proximo

        if self.__iterando is not None:
            return self.__iterando.conteudo
        try:
            return self.desenfileirar()
        except IndexError:
            raise StopIteration

    def __getitem__(self, item):
        return self.__fila[item-1]

    def __setitem__(self, item, value):
        self.__fila[item-1] = value
fila = Fila()

fila.enfileirar('Rsul')
fila.enfileirar('Victor')
fila.enfileirar('Luiz')

print(format(fila[2]))
print(format(fila[1]))