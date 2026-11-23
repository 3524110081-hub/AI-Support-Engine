
import unicodedata

from app.engines.base import SupportEngine
from app.application.schemas import SupportResponse


class TraditionalEngine(SupportEngine):
    """
    Motor tradicional basado en reglas y palabras clave.

    Clasifica solicitudes de soporte, determina su prioridad
    y genera respuestas predeterminadas.
    """

    def normalize(self, text: str) -> str:
        """
        Convierte el texto a minúsculas y elimina acentos
        para facilitar la comparación de palabras clave.
        """
        text = text.lower().strip()

        text = unicodedata.normalize("NFD", text)
        text = "".join(
            char for char in text
            if unicodedata.category(char) != "Mn"
        )

        return text

    def analyze(self, message: str) -> SupportResponse:
        """
        Analiza una solicitud y devuelve una respuesta estructurada.
        """

        text = self.normalize(message)

        # Palabras clave para identificar cada categoría.
        security_keywords = [
            "vulnerabilidad",
            "hackeo",
            "hackear",
            "acceso no autorizado",
            "filtracion de datos",
            "robo de informacion",
            "malware",
            "phishing",
            "inyeccion sql",
            "ataque",
            "cuenta comprometida",
            "datos expuestos",
            "brecha de seguridad",
            "intrusion",
            "se filtraron los datos",
            "filtraron los datos",
            "datos de todos los clientes",
            "datos de clientes",
            "exposicion de datos",
            "base de datos expuesta"
        ]

        access_keywords = [
            "iniciar sesion",
            "inicio de sesion",
            "no puedo entrar",
            "no puedo acceder",
            "acceso bloqueado",
            "cuenta bloqueada",
            "contrasena",
            "password",
            "login",
            "credenciales",
            "autenticacion"
        ]

        
        feature_keywords = [
            "nueva funcionalidad",
            "nueva funcion",
            "agregar una funcion",
            "agregar una opcion",
            "agregar un modulo",
            "agregar una herramienta",
            "me gustaria agregar",
            "me gustaria que",
            "solicito una funcion",
            "seria util que",
            "permitir que",
            "implementar",
            "mejora",
            "feature"
        ]


        bug_keywords = [
            "error",
            "falla",
            "fallo",
            "no funciona",
            "dejo de funcionar",
            "se congela",
            "se cierra",
            "pantalla en blanco",
            "crash",
            "bug",
            "excepcion",
            "no carga",
            "problema tecnico"
        ]

        # 1. Clasificación.
        # La categoría SECURITY tiene prioridad de detección
        # para no ignorar posibles incidentes de seguridad.

        if any(word in text for word in security_keywords):
            category = "SECURITY"

        elif any(word in text for word in access_keywords):
            category = "ACCESS"

        elif any(word in text for word in feature_keywords):
            category = "FEATURE"

        elif any(word in text for word in bug_keywords):
            category = "BUG"

        else:
            # Categoría de respaldo porque el contrato
            # únicamente permite las cuatro categorías.
            category = "BUG"

        # 2. Determinación de prioridad.

        critical_keywords = [
            "filtracion de datos",
            "datos expuestos",
            "robo de informacion",
            "cuenta comprometida",
            "ataque activo",
            "servidor comprometido",
            "perdida de datos",
            "sistema caido",
            "todos los usuarios",
            "todos los clientes",
            "se filtraron los datos",
            "filtraron los datos",
            "datos de todos los clientes"
        ]

        high_keywords = [
            "vulnerabilidad",
            "hackeo",
            "hackear",
            "acceso no autorizado",
            "malware",
            "phishing",
            "inyeccion sql",
            "brecha de seguridad",
            "intrusion",
            "no funciona para todos",
            "servicio caido",
            "bloquea a todos",
            "perdida de informacion"
        ]

        if any(word in text for word in critical_keywords):
            priority = "CRITICAL"

        elif any(word in text for word in high_keywords):
            priority = "HIGH"

        elif category == "FEATURE":
            priority = "LOW"

        elif category == "BUG":
            priority = "MEDIUM"

        elif category == "ACCESS":
            priority = "MEDIUM"

        elif category == "SECURITY":
            priority = "HIGH"

        else:
            priority = "LOW"

        # 3. Respuestas predeterminadas por categoría.

        default_responses = {
            "ACCESS": (
                "Lamentamos el inconveniente con el acceso. "
                "Verifique sus credenciales y utilice la opción "
                "de recuperación de contraseña si es necesario."
            ),

            "BUG": (
                "Lamentamos el inconveniente. Nuestro equipo "
                "revisará el error reportado. Proporcione los "
                "pasos para reproducirlo y cualquier mensaje de error."
            ),

            "FEATURE": (
                "Gracias por compartir su sugerencia. "
                "La solicitud de nueva funcionalidad será "
                "registrada para su evaluación por el equipo de desarrollo."
            ),

            "SECURITY": (
                "Se ha identificado un posible incidente de seguridad. "
                "El caso requiere revisión inmediata por parte del "
                "equipo especializado. Evite compartir contraseñas "
                "o información confidencial."
            )
        }

        # 4. Revisión humana para incidentes de seguridad.

        requires_human_review = category == "SECURITY"

        # 5. Construcción de la respuesta estructurada.

        return SupportResponse(
            category=category,
            priority=priority,
            response=default_responses[category],
            requiresHumanReview=requires_human_review,
            mode="traditional"
        )