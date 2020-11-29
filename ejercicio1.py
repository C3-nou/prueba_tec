arr = []
i = 0
while i < 4:
    var = input("Ingresa variable número {num}: ".format(num = (i+1)))
    if int(var) > 0:
        if i == 1 and int(var) > arr[0]:
            print("La segunda variable debe ser menor a la primera.")
        elif i == 2 and int(var) < arr[0]:
            print("La tercera variable no debe ser menor a la primera.")
        elif i == 3 and ((int(var) % 2 == 0 and arr[2] % 2 == 0) or (int(var) % 2 != 0 and arr[2] % 2 != 0 )):
            print("Si la tercera variable es par la cuarta debe de ser impar o vicerversa")
        else:
            arr.append(int(var))
            i += 1
    else:
        print("Número no entero mayor a cero")

print("""Los numeros ingresados son: {x}""".format(x='-'.join(map(str, arr))))

#arr[]


#variable1 = input("Ingresar")