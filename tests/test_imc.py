import pytest
from imc import calcular_imc


def test_imc_correcto():
    """Caso normal"""
    resultado = calcular_imc(70, 1.75)
    assert round(resultado, 2) == 30

def test_imc_caso_limite():
    """Caso límite con valores pequeños válidos"""
    resultado = calcular_imc(1, 1)
    assert resultado == 1


def test_imc_error():
    """Caso error cuando altura es negativa"""
    with pytest.raises(ValueError):
        calcular_imc(70, -1.75)