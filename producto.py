class Producto:
    """ Clase que construye producto """

    def __init__(self, codigo, nombre, precio,bebida): #marca):
        self.codigo: str = codigo
        self.nombre: str = nombre
        self.bebida:str= bebida
        self.precio: str = precio
        #self.marca: str = marca
        print(self.convertir_a_string())
        pass

    def convertir_a_string(self):
        return print("| {} | {} | {} |".format(self.codigo, self.nombre, self.precio, self.bebida))#self.marca))