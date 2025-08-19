

referenciaUsuarios = ["Usuario", "Contraseña","Mail", "DNI", "Nombre", "Apellido", "Telefono", "Fecha Nacimiento"]
Usuarios = [
    ["Jperez", "12345","jperez@gmail.com", "40123456", "Juan", "Perez", "1134567890", "1990-05-14"],
    ["Mgonza", "23456", "mgonzalez@yahoo.com.ar", "39234567", "Maria", "Gonzalez", "1145678901", "1987-10-22"],
    ["Crami", "35467","carlosramirez@gmail.com" "38456789", "Carlos", "Ramirez", "1156789012", "1995-07-03"],
    ["Lufernan", "45678","lufernandez@hotmail.com", "41234567", "Lucia", "Fernandez", "1167890123", "1992-01-19"],
    ["Amarti", "56789","anamartinez@yahoo.com.ar", "37567890", "Ana", "Martinez", "1178901234", "1985-03-28"],
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

referenciaActividades = ["ID", "Tipo", "Descripcion", "Fecha"]
Actividades = [
    [1, "Tour", "Recorrido por el Cristo Redentor y Pan de Azucar", "2025-09-11"],
    [2, "Museo", "Visita al Museo del Prado y recorrido por Madrid historico", "2025-09-16"],
    [3, "Excursion", "Visita a Chichen Itza y cenote Ik Kil", "2025-10-06"],
    [4, "Gastronomia", "Tour gastronomico por Roma y clase de pasta fresca", "2025-09-23"],
    [5, "Cultura", "Visita a templos de Kioto y ceremonia del te", "2025-11-02"],
]

referenciaHoteleria = ["ID", "Nombre", "Descripcion", "Ubicacion", "Rating"]
Hoteleria = [
    [1, "Copacabana Palace", "Hotel de lujo frente a la playa", "Rio de Janeiro, Brasil", 5],
    [2, "Hotel Ritz Madrid", "Hotel clasico en el centro de Madrid", "Madrid, Espana", 5],
    [3, "Hard Rock Hotel", "Resort frente al mar con entretenimiento", "Cancun, Mexico", 4],
    [4, "Hotel Bernini Palace", "Hotel boutique en el corazon de Florencia", "Florencia, Italia", 4],
    [5, "Park Hyatt Tokyo", "Hotel moderno con vistas al Monte Fuji", "Tokio, Japon", 5],   
]

referenciaPack = ["ID", "Nombre", "Precio", "IDDestino", "IDVuelo", "IDActividad", "IDHotel","IDAerolinea"]
Pack = [
    [1, "Brasil Aventura", 1200, 1, 1, 1, 1, 1],
    [2, "Espana Cultural", 1500, 2, 2, 2, 2, 2],
    [3, "Mexico Historico", 1100, 3, 3, 3, 3, 3],
    [4, "Italia Gourmet", 1700, 4, 4, 4, 4, 4],
    [5, "Japon Tradicion", 2500, 5, 5, 5, 5, 5],
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