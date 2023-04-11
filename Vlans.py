nvlan = int(input("Ingrese numero de VLAN: "))
if nvlan == 0 or nvlan == 4095:
    print("Este es una Vlan Reserved.")
elif nvlan >= 1 and nvlan <= 1005:
    print ("Esta es una Vlan Normal.")
elif nvlan >= 1006 and nvlan <= 4094:
    print ("Esta es una Vlan Extended.")
else:
    print("El valor ingresado no es una Vlan")
