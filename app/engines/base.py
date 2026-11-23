
from abc import ABC, abstractmethod

from app.application.schemas import SupportResponse


class SupportEngine(ABC):
    """
    Interfaz base para los motores del AI Support Engine.

    Los motores tradicional y generativo deberán implementar
    el método analyze() y devolver una respuesta estructurada.
    """

    @abstractmethod
    def analyze(self, message: str) -> SupportResponse:
        """
        Analiza una solicitud de soporte.

        Args:
            message: Mensaje enviado por el usuario.

        Returns:
            Respuesta estructurada con categoría, prioridad,
            respuesta, revisión humana y modo de procesamiento.
        """
        pass