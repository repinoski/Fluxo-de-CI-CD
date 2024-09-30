import pytest
from unittest.mock import patch
from main import *

def test_acertar_primeira_tentativa():
    with patch ('random.randint', return_value=42):
        resultado = descubra()
    assert resultado == "Parabéns, você acertou o número"
