import re
def fecha_validacion(fecha, validar):
    año = fecha[:4]
    mes = fecha[5:7]
    dia = fecha[8:10]
    separacion = [fecha[4:], fecha[7:]]

    msg = ""
    validar, msg = verificar_año(año)
    if not validar:
        return False, msg

    validar, msg = verificar_dias(mes, dia, año)
    if not validar:
        return False, msg

    validar, msg = verificar_mes(mes)
    if not validar:
        return False, msg

    validar, msg = verificar_separacion(separacion)
    if not validar:
        return False, msg

    return True, ""
    
    

def verificar_dias(mes, dia, año):
    dias_fixed = "01|02|03|04|05|06|07|08|09|"
    patron = ""
    dia_a_numero = int(dia)
    año_a_numero = int(año)
    if dia_a_numero > 0 and dia_a_numero < 31 :
        match mes:
            case "01" | "03" | "05" | "07" | "08" | "10" | "12":
                patron = f"{dias_fixed}[10-31]"
            case "04" | "06" | "09" | "11":
                patron = f"{dias_fixed}[10-30]"
            case "02":
                if año_a_numero % 4 == 0:
                    print(año_a_numero%4)
                    patron = f"{dias_fixed}[10-29]"
                else:
                    print(año_a_numero%4)
                    patron = f"{dias_fixed}[10-28]"
            case _:
                return False
        respuesta = re.match(patron,dia)
        if respuesta == None:
            return False, f"Dia invalido para el mes {mes}"
        return True, ""
    else:
        return False, "Dia invalido"
def verificar_mes(mes):
    lista_meses = ["01","02","03","04","05","06","07","08","09","10","11","12"]
    counter = 0
    for i in lista_meses:
        if mes == i:
            counter+=1
    if counter != 1:
        return False, f"Mes invalido: {mes}"
    return True, ""
def verificar_año(año):
    año_a_numero = int(año)
    if año_a_numero < 1900 or año_a_numero>2100:
        return False, "Año invalido"
    return True, ""
def verificar_separacion(separacion):
    patron = r"\/"
    for i in separacion:
        respuesta = re.match(patron,i)
        if(respuesta == None):
            return False,r"Separacion invalida, tiene que ser: \/"
    return True,""
