def Grabar():
    cant_autos=0

    if cant_autos==0:
        autos=[["","","",0,0,"","",""]]
    else:
        autos.append(["","","",0,0,"","",""])
        cant_autos += 1

    tipo=str(input("Ingrese el tipo de auto: "))

    patente=str(input("Ingrese la patente: "))

    marca="x"
    while len(marca)<2 or len(marca)>15:
        marca=str(input("Ingrese la marca: "))

    precio=0
    while precio<5000000:
        precio=int(input("Ingrese el precio: "))

    monto=int(input("Ingrese el monto de la multa: "))

    fecha=str(input("Ingrese la fecha de la multa: "))

    registro_fecha=str(input("Ingrese la fecha del registro"))

    duenio_nombre=str(input("Ingrese el nombre del dueño"))

    autos[cant_autos,0]=tipo
    autos[cant_autos,1]=patente
    autos[cant_autos,2]=marca
    autos[cant_autos,3]=precio
    autos[cant_autos,4]=monto
    autos[cant_autos,5]=fecha
    autos[cant_autos,6]=registro_fecha
    autos[cant_autos,7]=duenio_nombre

def Buscar(patente_pedida):
    hallado=0
    for i in range((cant_autos+1)):
        if autos[i-1,1]==patente_pedida:
            print(autos[cant_autos,0])
            print(autos[cant_autos,1])
            print(autos[cant_autos,2])
            print(autos[cant_autos,3])
            print(autos[cant_autos,4])
            print(autos[cant_autos,5])
            print(autos[cant_autos,6])
            print(autos[cant_autos,7])   
            hallado=1
        if hallado==0:
            print("Valor no encontrado")


def Certificados(contaminante, patente, duenio_nombre):
    contaminante = 0
    while contaminante < 1500 or contaminante > 3500:
        contaminante = int(input("Ingrese el valor de la multa por contaminación. Debe ser entre $1.500 y $3.500"))

    print("Certificado de emisión de contaminantes.")
    print("El valor de la multa por contaminación es de: ", contaminante)
    print("Patente del auto:", patente)
    print("Nombre del dueño: ", duenio_nombre)

def Salir():
    break

while True:
    opcion=int(input("Elija una de estas 4 opciones: 1. Grabar, 2. Buscar 3. Imprimir certificado, 4. Salir."))

    if opcion == 1:
        Grabar()
    if opcion == 2:
        Buscar()
    if opcion == 3:
        Certificados()
    if opcion == 4:
        Salir()
