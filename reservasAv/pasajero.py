from reservasAvion import reservasAvion

class pasajero:

    def __init__(self, pCedula, pNombre):
        self.__nombre = pNombre
        self.__cedula = pCedula

        """----------#metodos--------------"""

    def darNombre(self):
        return self.__nombre
    
    def darCedula(self):
        return self.__cedula
    