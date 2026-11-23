
from app.engines.generative import (
    normalize_text,
    detect_security_incident,
    detect_critical_incident
)


def test_normalize_text_removes_accents():
    result = normalize_text("Filtración de información")
    assert result == "filtracion de informacion"


def test_detect_security_incident():
    message = "Se filtraron las contraseñas de los clientes"
    assert detect_security_incident(message) is True


def test_detect_critical_incident():
    message = "Se filtraron los datos personales de todos los clientes"
    assert detect_critical_incident(message) is True


def test_detect_access_is_not_security():
    message = "No puedo iniciar sesión en mi cuenta"
    assert detect_security_incident(message) is False


def test_detect_feature_is_not_security():
    message = "Me gustaría agregar un módulo de reportes"
    assert detect_security_incident(message) is False
