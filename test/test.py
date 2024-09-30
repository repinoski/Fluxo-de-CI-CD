import pytest
from unittest.mock import patch
from io import StringIO
from main import *

def test_acertar_primeira_tentativa():
    with patch ('random.randint', return_value=42), \
         patch ('sys.stdin', new=StringIO ('42')):
        resultado = descubra()
    assert resultado == "Parabéns, você acertou o número"

def test_numero_invalido():
    with patch('sys.stdin', new=StringIO('dois')):
        with pytest.raises(ValueError):
            descubra()
