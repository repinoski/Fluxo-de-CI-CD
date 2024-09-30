import pytest
import random
from main import descubra

def test_acertar_primeira_tentativa():
    random.seed(42)
    num = random.randint(1, 100)
    resultado = descubra()
    assert resultado == "Parabéns, você acertou o número"

def test_numero_invalido():
    with pytest.raises(ValueError):
            descubra()

    with pytest.raises(ValueError):
            descubra("vinte")

    with pytest.raises(ValueError):
            descubra(3.14)
