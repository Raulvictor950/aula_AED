class fila:
    def __init__(self):
        self.primeiro = none
        self.ultimo = none
        self.__tamanho = none

    class Nó:
        def __init__(self, conteudo):
            self.proximo = none
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
    def __iter__(self):
        return self

    def __next__(self):
        if self.__iterando is none:
            self.__iterando = self.__primeiro

        else:
            self.__iterando = self.__iterando.proximo

        if self.__iterando is not none:
            return self.__iterando.conteudo
        raise StopIteration

