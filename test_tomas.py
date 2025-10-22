from Helpers.Validaciones import validar_mail
from data import Pasajeros
idPasajero = 1

while True:
    try:
        print("Inserte el nuevo mail:")
        nuevoMail = input()
        valid_mail = validar_mail(nuevoMail)
        Pasajeros[idPasajero][2] = nuevoMail
        break
    except ValueError:
        print("Mail invalido, intente devuelta")
        continue
print(Pasajeros[idPasajero])