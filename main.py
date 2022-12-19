
from persona import Persona
from producto import Producto
from factura import Factura
from factura_detalle import FacturaDetalle
from datetime import datetime
from colorama import init, Fore, Back, Style
init()
personas: Persona = []
productos: Producto = []
facturas: Factura = []


def persona():
    dni: str = str(input("Ingrese DNI: "))
    nombres: str = str(input("Ingrese Nombres: "))
    apellidos: str = str(input("Ingrese Apellidos: "))
    direccion: str = str(input("Ingrese Direccion: "))
    telefono: str = str(input("Ingrese Telefono: "))
    persona: Persona = Persona(dni, nombres, apellidos, direccion, telefono)
    personas.append(persona)
 
def listar_personas():
    for persona in personas:
        Persona.convertir_a_string(persona)


def buscar_persona():
    dni: str = str(input("Ingrese DNI para buscar persona: "))
    for persona in personas:
        if persona.dni == dni:
            Persona.convertir_a_string(persona)
            return persona


def editar_persona():
    dni: str = str(input("Ingrese DNI para buscar persona: "))
    for persona in personas:
        if persona.dni == dni:
            Persona.convertir_a_string(persona)
            persona.nombres = str(input("Ingrese nuevo nombre: "))
            Persona.convertir_a_string(persona)


def eliminar_persona():
    dni: str = str(input("Ingrese DNI para buscar persona: "))
    for indice, persona in enumerate(personas):
        if persona.dni == dni:
            personas.pop(indice)


def producto():
    codigo: str = str(input("Ingrese código del producto: "))
    nombre: str = str(input("Ingrese nombre del producto: "))
    bebida: str = str(input("ingrese bebida: "))
    precio: float = float(input("Ingrese precio del producto: "))
    bebida: float = float(input("ingrese precio: "))

    #marca: str = str(input("Ingrese marca del producto: "))
    producto: Producto = Producto(codigo, nombre, precio,bebida)
    productos.append(producto)


def listar_producto():
    for producto in productos:
        Producto.convertir_a_string(producto)


def buscar_producto():
    codigo: str = str(input("Ingrese Código para buscar el producto: "))
    for producto in productos:
        if producto.codigo == codigo:
            Producto.convertir_a_string(producto)
            return producto


def nueva_factura():
    print("para generar una factura busca un cliente")
    cliente: Persona = buscar_persona()
    factura: Factura = Factura(len(facturas)+1, cliente, datetime.now())
    continuar: bool = True
    while continuar:

        producto: Producto = buscar_producto()
        cantidad: int = int(input("Ingrese la cantidad: "))
        factura.detalle.append(FacturaDetalle(
            producto.codigo, producto.nombre, cantidad, producto.precio))
        
        condicion: str = str(input("SI para agregar productos: "))

        if condicion == "SI":
            continuar = True
        else:
            continuar = False
            factura.calcular_igv()
            facturas.append(factura)
        
            
           

def listar_factura():
    for factura in facturas:
        Factura.convertir_a_string(factura)

def buscar_factura():
    numero:int=int(input("Ingrese el numero de la factura: "))
    for factura in facturas:
        if factura.numero==numero:
            
            print("Polleria el  gordito")
            print("|serie | numero | cliente dni | nombre | base imponible | igv | total | fecha |")
            print("--------------------------------------------------------------------")
            Factura.convertir_a_string(factura)
            print("===================================================")
            for detalle in factura.detalle:
                FacturaDetalle.convertir_a_string(detalle)
            print("_______________________________________________")
            
def main():
    continuar: bool = True

    while continuar:
        print("*****************************************")
        print("***********SISTEMA DE VENTAS*************")
        print("                                         ")
        print("===================MENÚ==================")
        print("**************INGRESE OPCIONES***********")
        print(Fore.CYAN+Back.BLACK+"       1: PARA AGREGAR PERSONA"+ Back.RESET)
        print(Fore.CYAN+Back.BLACK+"       2: PARA LISTAR PERSONAS"+ Back.RESET)
        print(Fore.CYAN+Back.BLACK+"       3: PARA BUSCAR PERSONA"+ Back.RESET)
        print(Fore.CYAN+Back.BLACK+"       4: PARA EDITAR PERSONA"+ Back.RESET)
        print(Fore.CYAN+Back.BLACK+"       5: PARA ELIMINAR PERSONA"+ Back.RESET)
        print(Fore.CYAN+Back.BLACK+"       6: PARA AGREGAR PRODUCTO"+ Back.RESET)
        print(Fore.CYAN+Back.BLACK+"       7: PARA LISTAR PRODUCTO"+ Back.RESET)
        print(Fore.CYAN+Back.BLACK+"       8: PARA CREAR FACTURA"+ Back.RESET)
        print(Fore.CYAN+Back.BLACK+"       9: PARA LISTAR  FACTURA"+ Back.RESET)
        print(Fore.CYAN+Back.BLACK+"       10: PARA BUSCAR FACTURA"+ Back.RESET)
        print(Fore.CYAN+Back.BLACK+"       11: PARA SALIR"+ Back.RESET)
        caso: str = str(input(Fore.RED+Back.BLACK+"INGRESE OPCIÓN: "+ Back.RESET))
        match caso:
            case "1":
                persona()
            case "2":
                listar_personas()
            case "3":
                buscar_persona()
            case "4":
                editar_persona()
            case "5":
                eliminar_persona()
            case "6":
                producto()
            case "7":
                listar_producto()
            case "8":
                nueva_factura()
            case "9":
                listar_factura()
            case "10":
                buscar_factura()

            case "11":
                continuar = False


if __name__ == '__main__':
    main()
 