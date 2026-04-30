import pytest
from app.descuentos import calcular_descuento

def test_descuento_alto():
    assert calcular_descuento(1200) == 1080

def test_error_tipo():
    with pytest.raises(ValueError):
        calcular_descuento("abc")

def test_borde():
    assert calcular_descuento(500) == 475