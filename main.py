from password_manager import encrypt_passwords_in_file, change_password, add_login

def main():
    filename = input("Enter the CSV file name: ")
    encrypt_passwords_in_file(filename)

    while True:
        # 2. Mostrar el menú de opciones
        print("Options: (1) Change Password, (2) Add Password, (3) Quit: ", end="")
        option = input()

        if option == "1":
            datos = input("Enter the website and the new password: ").split()
            
            if len(datos) < 2:
                print("Input is in the wrong format!")
            elif len(datos[1]) < 12:
                print("Password is too short!")
            else:
                website = datos[0]
                nueva_pass = datos[1]
                if change_password(filename, website, nueva_pass):
                    print("Password changed.")
                else:
                    print("Website not found! Operation failed.")

        elif option == "2":
            datos = input("Enter the website, username, and password: ").split()
            
            if len(datos) < 3:
                print("Input is in the wrong format!")
            elif len(datos[2]) < 12:
                print("Password is too short!")
            else:
                website, user, password = datos[0], datos[1], datos[2]
                add_login(filename, website, user, password)
                print("Login added.")

        elif option == "3":
            break
        
        else:
            print("Invalid option selected!")

if __name__ == "__main__":
    main()
