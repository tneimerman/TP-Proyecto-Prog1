

referenciaPasajeros = ["ID", "Contraseña","Mail", "DNI", "Nombre", "Apellido", "Telefono", "Fecha Nacimiento"]
Pasajeros = [
    [1, "12345","jperez@gmail.com", "40123456", "Juan", "Perez", "1134567890", "1990-05-14"],
    [2, "23456", "mgonzalez@yahoo.com.ar", "39234567", "Maria", "Gonzalez", "1145678901", "1987-10-22"],
    [3, "35467","carlosramirez@gmail.com" "38456789", "Carlos", "Ramirez", "1156789012", "1995-07-03"],
    [4, "45678","lufernandez@hotmail.com", "41234567", "Lucia", "Fernandez", "1167890123", "1992-01-19"],
    [5, "56789","anamartinez@yahoo.com.ar", "37567890", "Ana", "Martinez", "1178901234", "1985-03-28"],
]

referenciaDestinos = ["ID", "Destino", "Descripcion"]
Destinos = [
    [1, "Brasil", "Playas tropicales y carnaval en Rio de Janeiro"],
    [2, "Espana", "Turismo cultural e historico en Madrid y Barcelona"],
    [3, "Mexico", "Playas de Cancun y ruinas mayas"],
    [4, "Italia", "Arte y gastronomia en Roma y Florencia"],
    [5, "Japon", "Tecnologia y tradicion en Tokio y Kioto"],
]

referenciaVuelos = ["ID", "Empresa", "IDDestino" "FechaLlegada", "Escala"]
Vuelos = [
    [1, "LATAM", 1, "2025-09-10", "Directo"],
    [2, "Iberia", 2, "2025-09-15", "Escala en Paris"],
    [3, "Aeromexico", 3, "2025-10-05", "Directo"],
    [4, "Alitalia", 4, "2025-09-22", "Escala en Frankfurt"],
    [5, "ANA", 5, "2025-11-01", "Directo"],
    ]


referenciaAerolinea = ["ID", "Nombre", "Modelo"]
Aerolinea = [
    [1, "Aerolinea de Argentina", "Airbus A330-200"],
    [2, "Qatar Airways", "Boeing 777"],
    [3, "Copa", "Boeing 737 MAX 9-A"],
    [4, "Flybondi", "Airbus A320"],
    [5, "JetSMART", "Airbus A321neo"],   
]
referenciaPackUser = ["ID","IDPack","User"]
PackUser = []