from data import Vuelos, Aerolinea, Destinos, referenciaVuelos

found = []
def show_results(data):
    for aero in Aerolinea:
        if aero[0] == data[1]:
            data[1] = aero[1]
            break
    for dest in Destinos:
        if dest[0] == data[2]:
            data[2] = dest[1]
            break
    print(f"╔{"="*58}╗")
    print(f"║{"Aerolinea":<10}║{"Destino":<10}║{referenciaVuelos[3]:<15}║{referenciaVuelos[4]:<20}║")
    print(f"╠{"="*58}╣")
    print(f"║{data[1]:<10}║{data[2]:<10}║{data[3]:<15}║{data[4]:<20}║")
    print(f"╚{"="*58}╝")

assert show_results(Vuelos[3]) == Vuelos[3]