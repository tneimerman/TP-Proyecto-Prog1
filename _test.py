from Helpers.Validaciones import validar_mail, validar_fecha
from Helpers.Archivos import obtener_max_archivo
from CRUDs.Aerolineas import getNewIdAerolinea


def max_id():
    return obtener_max_archivo("Archivos/Aerolinea.txt")

def get_fecha():
    return "2025/02/29"

def get_mail():
    return "test@test.com"

def test_getNewIdAerolinea():
    #Arrange
    count = max_id()
    #Act
    resultado = getNewIdAerolinea()
    #Assert
    assert resultado == count+1
    
def test_validar_fecha():
    #Arrange
    fecha = get_fecha()
    #Act
    resultado = validar_fecha(fecha)
    #Assert
    assert resultado == True

def test_validar_mail():
    #Arrange
    mail = get_mail()
    #Act
    resultado = validar_mail(mail)
    #Assert
    assert resultado == True



