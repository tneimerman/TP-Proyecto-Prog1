from Helpers.Validaciones import validar_mail
from Helpers.Archivos import obtener_lista_por_dato, obtener_matriz
from CRUDs.Aerolineas import getNewIdAerolinea
from Helpers.JSON import obtener_diccionario_por_id


aero = obtener_matriz("Archivos/Aerolinea.txt")
print(aero)
def test_getNewIdAerolinea():
    assert getNewIdAerolinea() == len(aero) + 1
    
def test_obtener_diccionario_por_id():
    assert obtener_diccionario_por_id(1) == {"ID":1,"IdPasajero": 1,"IdVuelo": 3}


def test_validar_mail():
    mail = "test@test.com"
    valid = validar_mail(mail)
    assert valid == True

lista = obtener_lista_por_dato("Juan", "Archivos/Pasajeros.txt")
def test_obtener_lista_por_id():
    assert lista[0] == '1'

