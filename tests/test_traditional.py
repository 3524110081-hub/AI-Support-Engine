
from app.engines.traditional import TraditionalEngine


def test_access_classification():
    engine = TraditionalEngine()
    result = engine.analyze("No puedo iniciar sesión en mi cuenta")

    assert result.category == "ACCESS"
    assert result.priority == "MEDIUM"
    assert result.requiresHumanReview is False
    assert result.mode == "traditional"


def test_bug_classification():
    engine = TraditionalEngine()
    result = engine.analyze("La aplicación muestra un error al guardar")

    assert result.category == "BUG"
    assert result.priority == "MEDIUM"
    assert result.requiresHumanReview is False


def test_feature_classification():
    engine = TraditionalEngine()
    result = engine.analyze("Me gustaría agregar un módulo de reportes")

    assert result.category == "FEATURE"
    assert result.priority == "LOW"
    assert result.requiresHumanReview is False


def test_security_classification():
    engine = TraditionalEngine()
    result = engine.analyze(
        "Encontré una vulnerabilidad que permite acceso no autorizado"
    )

    assert result.category == "SECURITY"
    assert result.priority == "HIGH"
    assert result.requiresHumanReview is True


def test_critical_security_classification():
    engine = TraditionalEngine()
    result = engine.analyze(
        "Se filtraron los datos de todos los clientes"
    )

    assert result.category == "SECURITY"
    assert result.priority == "CRITICAL"
    assert result.requiresHumanReview is True


def test_response_is_not_empty():
    engine = TraditionalEngine()
    result = engine.analyze("No puedo iniciar sesión")

    assert result.response.strip() != ""


def test_response_has_valid_structure():
    engine = TraditionalEngine()
    result = engine.analyze("La aplicación muestra un error")

    data = result.model_dump()

    assert set(data.keys()) == {
        "category",
        "priority",
        "response",
        "requiresHumanReview",
        "mode"
    }