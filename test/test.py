import pytest
from unittest.mock import patch
from main import *

def test_acertar_primeira_tentativa():
    with patch ('random.randint', return_value=42):
        resultado = descubra()
    assert resultado == {"Parabéns, você acertou o número": True, 'num': 42}

def test_numero_invalido():
    with pytest.raises(ValueError):
            descubra()

    with pytest.raises(ValueError):
            descubra("vinte")

    with pytest.raises(ValueError):
            descubra(3.14)