condicion=True
while condicion:
    contrasenacorrecta="kelilopz"
    contrasena=str(input("por favor inserta tu contraseña \n"))
    if contrasena!=contrasenacorrecta:
        print("Contraseña incorrecta")
        condicion=True
    else:
        print("Contraseña correcta \n ingreso correcto ")
        condicion=False
