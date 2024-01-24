nota=int(input("Por favor inserta la nota del estudiante de 1 a 100\n"))
if nota>=90:
    nota="A"
elif nota>=70:
    nota="B"
elif nota>=50:
    nota="C"
else:
 if nota>=0:
     nota="D"
 else:
     print("usted no seleccionó una opción valida")

print("Su calificacion es", nota)
