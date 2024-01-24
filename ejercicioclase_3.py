condicion=True
while condicion:
    comida=int(input("por favor inserta el numero del el tipo de comida que deseas consumir \n 1) Comida China \n 2) Comida italiana \n 3) Comida mexicana \n"))
    if comida==1:
        print("Tu puedes ir a los siguientes restaurantes \n -la Casona China \n -Chinese food and chicken \n -Restaurante Chino /n")
        condicion=False
    elif comida==2:
        print("Tu puedes elegir entre los siguientes restaurantes \n -Batutto pasta y risoto \n -Mama mía pizza y pasta \n -Venneto pasta y café")
        condicion=False
    elif comida==3:
        print("Si quieres comida mexicana podría ir a \n -Tacos y más tacos \n -Birria y tacos \n -Mexicanisima restaurante ")
        condicion=False
    else:
        print("Por favor elija una opción valida")
