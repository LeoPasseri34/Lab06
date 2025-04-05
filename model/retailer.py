
class Retailer:

    def __init__(self, codice, nome, tipo, stato):
        self.codice = codice
        self.nome = nome
        self.tipo = tipo
        self.stato = stato

    def __eq__(self, other):
        return self.codice == other.codice

    def __hash__(self):
        return hash(self.codice)

    def stampaBella(self):
        return f"Il rivenditore {self.nome} con codice {self.codice}"

    def __str__(self):
        return self.nome