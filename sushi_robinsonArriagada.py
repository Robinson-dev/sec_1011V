
#Robinson Arriagada


resp = True
salir = 5
compra = 0
compra1 = 0
compra2 = 0
compra3 = 0
compra4 = 0
compratotal = 0
desc = 0


print(" ")
print("Bienvenido al Sushi ")
print(" ")
print(" Elija  ")
print(" ")

while salir == 5: 

    print(" 1.- Pikachu Roll $4.500 cu ")
    print(" 2.- Otaku Roll $5.000 cu ")
    print(" 3.- Pulpo Venenoso Roll $5.200 cu")
    print(" 4.- Anguila Electrica Roll $4.800 cu ")
    print(" 5.- Salir")
    print("")
    try:
        eleccion =(int(input(  "Por favor seleccione una opcion del menu 1-5 :")))
    except ValueError:
        print(" ERROR: Ingrese una alternativa entre 1 - 5, por favor ")


while salir == 5:   
    
    if eleccion == 1:
        compra1=input(int(print(" indique la cantidad de Pikachu Roll a comprar ")))
        compra1 * 4500
        compratotal = compra1 + compra2 + compra3 + compra4
    elif eleccion == 2 :
            compra2=input(int(print(" indique la cantidad de Otaku Roll a comprar ")))
            compra2 * 5000
            compratotal = compra1 + compra2 + compra3 + compra4
    elif eleccion == 3:
            compra3=input(int(print(" indique la cantidad de Pulpo Venenoso a comprar ")))
            compra3* 5200
            compratotal = compra1 + compra2 + compra3 + compra4
    elif eleccion == 4:
        compra3=input(int(print(" indique la cantidad de Anguila Electrica Roll a comprar ")))
        compra4 * 4800
        compratotal = compra1 + compra2 + compra3 + compra4
    else:
        eleccion== 5
        salir = 4

print(" gracias por comprar en nuetros sushi")

print(f" usted a comprado ${compra1} de Pikachu Roll ")
print(f" usted a comprado ${compra2} de Otaku Roll ")
print(f" usted a comprado ${compra3} de Pulpo Venenoso ")
print(f" usted a comprado ${compra4} de Anguila Electrica Roll ")
print(" ")
print( f" su compra totas es de ${compratotal}")
        
while True:
    try:
        resp=(input(" ingrese un codigo de descuento para un 10 por ciento de desc en su compra total "))
    except ValueError:
        print(" ERROR: Ingrese un còdigo de descuento vàlido ")

        if resp == soyotaku:
            valor_final= compratotal * 10//100
            print(f" le valor final a pagar es de {valor_final} ")
        else :
           print(" Ingrese un còdigo de descuento vàlido ")

