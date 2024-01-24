palabra=str(input("Escribe la palabra que crees es palindromo"))
if palabra==palabra[::-1]:
    print("Esta palabra es palindromo")
else:
    print("Tu palabra no es palindromo")
