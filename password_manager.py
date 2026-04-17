import csv

from caesar import caesar_encrypt


def encrypt_single_pass(filename: str) -> None:
    with open(filename, "r") as H:
        password = H.read().strip()

    encr_pass = caesar_encrypt(password)

    with open(filename, "w") as H:
        H.write(encr_pass)
    pass


def encrypt_passwords_in_file(filename: str) -> None:
    datos_actualizados = []

    with open(filename, "r",) as f:
        lector = csv.reader(f)
        titutlos = next(lector)
        datos_actualizados.append(titutlos)
        
        for fila in lector:
            fila[2] = caesar_encrypt(fila[2])
            datos_actualizados.append(fila)
            

    with open(filename, "w", newline="", ) as f:
        escritor = csv.writer(f)
        escritor.writerows(datos_actualizados)


def change_password(filename: str, website: str, password: str) -> bool:
    filas_actualizadas = []
    encontrado = False

    with open(filename, "r") as f:
        lector = csv.reader(f)
        for fila in lector:
            if fila: 
                if fila[0] == website:
                    fila[2] = caesar_encrypt(password)
                    encontrado = True
                
                filas_actualizadas.append(fila)

    if not encontrado:
        return False

    with open(filename, "w", newline="") as f:
        escritor = csv.writer(f)
        escritor.writerows(filas_actualizadas)
    return True


def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    """TODO: Parte 4."""
    pass

encrypt_passwords_in_file("examples/example2.csv")
