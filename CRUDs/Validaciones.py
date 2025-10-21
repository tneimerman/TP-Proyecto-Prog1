import re
def validar_mail(mail):
    if re.search(r"\w@\w.\w", mail) == None:
        raise ValueError("Mail invalido")
    return True

def validar_dni(dni):
    if  dni.isdigit() == False:
        raise ValueError("DNI Invalido")
    return True

def validar_telefono(tel):
    if re.search(r"11\d{8}",tel) == False:
        raise ValueError("Telefono invalido")
    return True

def validar_fecha(fecha):
    if re.search(r"\d{4}/\d{2}/\d{2}", fecha) is None:
        raise ValueError("Fecha invalida")
    return True