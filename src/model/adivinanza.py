from typing import List

class Adivinanza:
    """
        Representa una palabra a adivinar en el juego del ahorcado.

        Attributes:
            __letras (list[str]): Lista de caracteres que conforman la palabra a adivinar.
            __posiciones (list[bool]): Lista de booleanos que indican si cada letra ha sido adivinada.
    """

    def __init__(self, palabra: str):
        """
            Inicializa la clase Adivinanza
        
            Atributos:
                palabra (str): Palabra a adivinar en el juego
        """

        self.__letras: list[str] = list(palabra)
        self.__posiciones: list[bool] = [False] * len(self.__letras)


    def adivinar(self, letra: str) -> List[int]:
        """
            Metodo para intentar adivinar la palabra

            Atributos:
                letra (str): Letra a verificar si se encuentra en la palabra 

            Returns:
                Si la letra se encuentra en la lista:
                    List: Array con la posición donde está la letra

                Si  no se encuentra:
                    List: Array vacio
        """

        if letra not in self.__letras:
            return []

        posiciones_donde_esta_la_letra = []
        for i in range(len(self.__letras)):
            if self.__letras[i] == letra:
                posiciones_donde_esta_la_letra.append(i)
                self.__posiciones[i] = True
        return posiciones_donde_esta_la_letra
    

    def obtener_letras(self) -> List[str]:
        """
            Metodo para obtener las letras de la palabra a adivinar

            Returns:
                List: Array con las letras que conforman la palabra que se debe adivinar
        """
        return self.__letras
    

    def obtener_posiciones(self) -> List[bool]:
        """
            Metodo para obtener las posiciones de las letras de la palabra a adivinar

            Returns:
                List: Array con las posiciones de las letras
        """
        return self.__posiciones
    

    def obtener_cantidad_posiciones(self) -> int:
        """
            Metodo para obtener la cantidad de posiciones/letras de la palabra a adivinar

            Returns:
                int: Cantidad de letras que conforman la palabra
        """
        return len(self.__letras)
    

    def verificar_si_hay_triunfo(self) -> bool:
        """
            Metodo para verificar si el usuario ha ganado

            Returns:
                Bool: Verifica si se han adivinado todas las letras de la palabra
        """
        return all(self.__posiciones)
