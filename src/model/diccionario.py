import random


class Diccionario:

    def __init__(self):
        """
            Inicializa una instancia de la clase Diccionario, cargando las palabras desde un archivo.
        """
        self.palabras: list[str] = self.__cargar_palabras()

    def __cargar_palabras(self) -> list[str]:
        """
            Se encarga de cargar las palabras desde el archivo .txt que las contiene

            Returns:
                List: Array con las palabras elegibles para el juego
        """
       
        palabras = []
        with open("assets/palabras.txt", "r", encoding="utf8") as archivo:
            for line in archivo:
                palabras.append(line.strip())

        return palabras

    def obtener_palabra(self) -> str:
        """
            Selecciona una palabra al azar de las palabras previamente cargadas

            Returns:
                Str: Palabra a adivinar en el juego
        """
        indice_aleatorio = random.randint(0, len(self.palabras) - 1)
        return self.palabras[indice_aleatorio]
