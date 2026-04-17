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
    filas_actualizadas = []
    
    with open(filename, "r", encoding="utf-8") as f:
        lector = csv.reader(f)
        encabezado = next(lector, None)
        if encabezado:
            filas_actualizadas.append(encabezado)
        for fila in lector:
            if len(fila) >= 3:
                fila[2] = caesar_encrypt(fila[2])
                filas_actualizadas.append(fila)
                
    with open(filename, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerows(filas_actualizadas)


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
    password_encriptada = caesar_encrypt(password)
    with open(filename, "a", newline="",) as f:

        escritor = csv.writer(f)

        escritor.writerow([website_name, username, password_encriptada])

