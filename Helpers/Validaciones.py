import re
from Helpers.fecha_validacion import fecha_validacion
def validar_mail(mail):
    if re.search(r"\w@\w.\w", mail) == None:
        raise ValueError("Mail invalido")
    return True

def validar_dni(dni):
    if  dni.isdigit() == None:
        raise ValueError("DNI Invalido")
    return True

def validar_telefono(tel):
    if re.search(r"11\d{8}",tel) == None:
        raise ValueError("Telefono invalido")
    return True

def validar_fecha(fecha):
    ok, msg = fecha_validacion(fecha, True)
    if ok != True:
        raise ValueError(msg)
    else:
        return True