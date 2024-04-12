def comparar_vlans_native(vlan_native, vlans):
    mensaje = "Las VLANs son iguales y cumplen con el requerimiento" if vlan_native == vlans[0] else "Las VLANs son diferentes y no cumplen con el requerimiento"
    print(mensaje)

def comparar_vlans(vlans_input, vlans):
    vlans_input_list = list(map(int, vlans_input.split(',')))
    mensaje = "Las VLANs son iguales y cumplen con el requerimiento" if vlans_input_list == vlans else "Las VLANs son diferentes y no cumplen con el requerimiento"
    print(mensaje)

def main():
    vlansw1 = [10, 20, 30]
    navsw1 = 99

    vlansw2 = [40, 50, 60]
    navsw2 = 200

    resp1 = int(input("Ingresar VLAN nativa del SW1: "))
    comparar_vlans_native(resp1, [navsw1])

    resp2 = input("Ingresar VLAN n1 del SW1: ")
    resp3 = input("Ingresar VLAN n2 del SW1: ")
    resp4 = input("Ingresar VLAN n3 del SW1: ")
    comparar_vlans(resp2 + ',' + resp3 + ',' + resp4, vlansw1)

    resp5 = int(input("Ingresar VLAN nativa del SW2: "))
    comparar_vlans_native(resp5, [navsw2])

    resp6 = input("Ingresar VLAN n1 del SW2: ")
    resp7 = input("Ingresar VLAN n2 del SW2: ")
    resp8 = input("Ingresar VLAN n3 del SW2: ")
    comparar_vlans(resp6 + ',' + resp7 + ',' + resp8, vlansw2)

if __name__ == "__main__":
    main()
