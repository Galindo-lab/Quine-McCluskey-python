class Term():

    def __init__(self, implicants, binary):
        self.implicants = implicants
        self.binary = binary
        self.n_ones = Term.count_ones(binary)

    @classmethod
    def from_int(cls: type, number: int, n_variables: int) -> type:
        """ Crear un termino a partir de un valor en vez de una Lista, se usa para genera la primera tabla """
        return cls([number], Term.bindigits(number, n_variables))

    @classmethod
    def join(cls: type, a: type, b: type) -> type:
        """ Une dos instancias del tipo 'Term' y retorna su union """
        return cls(a.implicants + b.implicants,
                   Term.combine_bin(a.binary, b.binary))

    @classmethod
    def bindigits(cls: type, number: int, digits: int) -> str:
        """ Convertir numero a binario de tamaño fijo """
        return "{0:0{1}b}".format(number, digits)

    @classmethod
    def count_ones(cls: type, a: str) -> int:
        """ Cuenta cuantos '1' aparecen en un string """
        return a.count("1")

    @classmethod
    def combine_bin(cls: type, a: str, b: str) -> str:
        """ Une el dos 'Term.binary' y coloca un '-' en los caracteres diferentes"""
        conv = ''
        for i in range(len(a)):
            conv += '-' if a[i] != b[i] else a[i]
        return conv
