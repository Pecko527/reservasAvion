from enum import Enum 
classs Clase(Enum):

    '''------------------------------#Enumeracion................'''

    claseEjecutiva = 1
    claseEconomica = 2

class ubicacion(Enum):
    """------------------#enumeracion Ubi sillas------------------------"""

    ventana = 1
    pasillo = 2
    centro = 3

class silla:

    def __init__(self, pNumero, pClase, pUbicacion):
        self.__numero = pNumero
        self.__clase = pClase
        self.__ubicacion = pUbicacion 
        self.__pasajero = None

    """------------------#metodos---------------------"""

    def asignarAlPasajero(self, pPasajero, pClase, pUbicacion):
        self.__pasajero == pPasajero
        self.__clase == pClase
        self.__ubicacion == pUbicacion

    def darNumero(self):
        return self.__numero
    
    def asignarSilla(self, pNumero):
        if pNumero == self.__numero:
            return "El asiento se encuentra ocupado en este momento"
        else:
            return "El asiento se encuentra disponible"
        
    def sillaDesasignada(self, pPasajero):
        if pPasajero == self.__numero:
            return None 
