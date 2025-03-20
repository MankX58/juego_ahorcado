from src.model.diccionario import Diccionario
from src.model.adivinanza import Adivinanza
from src.model.error_intentos_insuficientes import ErrorIntentosInsuficientes
from typing import List


class Juego:
    """
        Representa el juego a ejecutar

        Atributos:
            self.__dificultad(str): Representa la dificultad del juego, baja, media o alta
            self.__intentos_realizados(int): Los intentos que ha realizado el usuario por adivinar la palabra
            self.__diccionario(Diccionario): Diccionario de palabras y letras a usar en el juego
            self.__adivinanza(Adivinanza): La adivinanza para el juego
    """
    DIFICULTAD_BAJA = "DIFICULTAD_BAJA"
    DIFICULTAD_MEDIA = "DIFICULTAD_MEDIA"
    DIFICULTAD_ALTA = "DIFICULTAD_ALTA"

    def __init__(self):
        """
            Inicializa el juego con dificultad baja por defecto y sin una palabra generada.
        """
        self.__dificultad = Juego.DIFICULTAD_BAJA
        self.__intentos_realizados: int = 0
        self.__diccionario = Diccionario()
        self.__adivinanza: Adivinanza = None

    def obtener_intentos_realizados(self) -> int:
        """
            Metodo para obtener la cantidad de intentos realizados

            Returns:
                int: Número de intentos realizados por el usuario
        """
        return self.__intentos_realizados

    def obtener_adivinanza(self) -> Adivinanza:
        """
            Metodo para obtener la adivinanza para uasr en el juego

            Returns:
                Adivinanza: Instancia de la clase adivinanza con la palabra a usar en el juego
        """
        return self.__adivinanza

    def __generar_palabra(self) -> str:
        """
            Metodo para obtener una palabra del diccionario
        """
        return self.__diccionario.obtener_palabra()

    def calcular_intentos_permitidos(self) -> int:
        """
            Calcula la cantidad de intentos permitidos según la dificultad del juego.

            Returns:
                int: Cantidad de intentos permitidos.
        """
        if self.__dificultad == self.DIFICULTAD_BAJA:
            return 20
        if self.__dificultad == self.DIFICULTAD_MEDIA:
            return 10
        if self.__dificultad == self.DIFICULTAD_ALTA:
            return 5

        return 0

    def modificar_dificultad(self, dificultad: str) -> None:
        """
            Modifica la dificultad del juego.

            Args:
                dificultad (str): Dificultad a asignar al juego.
        """
        self.__dificultad = dificultad

    def iniciar_partida(self) -> int:
        """
            Inicia una nueva partida.

            Returns:
                int: Cantidad de posiciones de la palabra a adivinar.
        """
        palabra = self.__generar_palabra()
        self.__adivinanza: Adivinanza = Adivinanza(palabra)
        self.__intentos_realizados = self.calcular_intentos_permitidos()
        return self.__adivinanza.obtener_cantidad_posiciones()

    def adivinar(self, letra: str) -> List[int]:
        """
            Intenta adivinar una letra de la palabra.

            Args:
                letra (str): Letra que el jugador quiere adivinar.

            Returns:
                list[int]: Lista con las posiciones donde aparece la letra en la palabra. Vacía si la letra no está.

            Raises:
                ErrorIntentosInsuficientes: Si no quedan intentos disponibles.
        """
        if self.__intentos_realizados < 0:
            raise ErrorIntentosInsuficientes()
        self.__intentos_realizados -= 1
        return self.__adivinanza.adivinar(letra)

    def verificar_si_hay_intentos(self) -> bool:
        """
            Verifica si el jugador aún tiene intentos disponibles.

            Returns:
                bool: True si quedan intentos, False si no.
        """
        return self.__intentos_realizados >= 0

    def verificar_triunfo(self) -> bool:
        """
            Verifica si el jugador ha ganado.

            Returns:
                bool: True si el jugador ha ganado, False si no.
        """
        return self.__adivinanza.verificar_si_hay_triunfo()