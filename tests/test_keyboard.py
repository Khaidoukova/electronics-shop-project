import pytest
from src.keyboard import Keyboard


def test_change_lang():
    keyboard1 = Keyboard("Defender", 500, 20)
    assert str(keyboard1.name) == "Defender"
    assert str(keyboard1.language) == "EN"
    keyboard1.change_lang()
    assert str(keyboard1.language) == "RU"
    keyboard1.change_lang().change_lang()
    assert str(keyboard1.language) == "RU"
