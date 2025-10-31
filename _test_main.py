"""Tomas"""
from CRUDs.Archivos import save_info
assert save_info("Archivos/Aerolinea.txt", ["4", "Air France", "Boeing 777"])

"""David"""
from Helpers.Validaciones import *

def test_validar_mail(mail):
    assert validar_mail(mail)

mail = "test@test.com"