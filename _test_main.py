"""Tomas"""


"""David"""
from Helpers.Validaciones import *

def test_validar_mail(mail):
    assert validar_mail(mail)

mail = "test@test.com"