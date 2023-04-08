import pytest
from lab3 import palindrom
from lab3 import validate_ip
from lab3 import get_os


def test_palindrom():
    with pytest.raises(TypeError):
        palindrom()

    with pytest.raises(TypeError):
        palindrom(123)

    assert palindrom("Hello world") == []
    assert palindrom("kayak deified repaper word") == ['kayak', 'deified', 'repaper']


def test_validate_ip():
    with pytest.raises(TypeError):
        validate_ip()

    with pytest.raises(TypeError):
        validate_ip(123)

    assert validate_ip('192.111.212.53') == True
    assert validate_ip('222.147.1.0') == False
    assert validate_ip('150.160.0') == False
    assert validate_ip('254.134.125.1') == False


def test_get_os():
    assert get_os() == 'Windows'
