
class ClaseEntrada:

    def __init__(self, filaEntrada, columnaEntrada):
        self.filaEntrada = filaEntrada
        self.columnaEntrada = columnaEntrada

class ClaseMaqueta:

    def __init__ (self, nombreMaqueta, filaMaqueta, columnaMaqueta, entradaMaqueta, objetivosMaqueta, estructuraMaqueta):
        self.nombreMaqueta = nombreMaqueta
        self.filaMaqueta = filaMaqueta
        self.columnaMaqueta = columnaMaqueta
        self.entradaMaqueta = entradaMaqueta
        self.objetivosMaqueta = objetivosMaqueta
        self.estructuraMaqueta = estructuraMaqueta

class ClaseObjetivo:

    def __init__(self, nombreObjetivo, filaObjetivo, columnaObjetivo):
        self.nombreObjetivo = nombreObjetivo
        self.filaObjetivo = filaObjetivo
        self.columnaObjetivo = columnaObjetivo

class ClasePosiciones:

    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
