def verificar_tipo_acl(numero_acl):
    try:
        numero_acl = int(numero_acl)
    except ValueError:
        return "Número de ACL inválido. Debe ser un número entero."

    if numero_acl >= 1 and numero_acl <= 99:
        return "ACL Estándar"
    elif numero_acl >= 100 and numero_acl <= 199:
        return "ACL Extendida"
    else:
        return "Número de ACL no corresponde a una lista de acceso"

numero_acl = input("Ingrese el número de ACL IPv4: ")

tipo_acl = verificar_tipo_acl(numero_acl)

print("El número de ACL", numero_acl, "corresponde a una", tipo_acl)
