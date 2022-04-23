import datetime

boleta ={}
rut_cliente=input('Ingrese el rut del cliente para asociarlo a sus puntos: ')
correo_cliente = input('Ingrese el correo del cliente para su boleta virtual: ')
fecha_actual= datetime.date.today()
boleta['rut_cliente']= rut_cliente
boleta['correo_cliente']=correo_cliente
boleta['fecha_actual']= fecha_actual
boleta['detalle']= []
print('INICIA EL INGRESO DE PRODUCTOS: ')

estado = True
while estado:
    codigo_producto = input('ingrese el código del producto: ')
    nombre_producto = input('ingrese el nombre del producto: ')
    categoria = input('ingrese la categoria del producto: ')
    precio_producto = input('ingrese el precio del producto: ')
    cantidad = input('ingrese la cantidad de los productos comprados: ')

#creación del diccionario {}. El valor no va entre "" por que el
# dato ingresado es una variable, no es una constante. De ser cte, sería ""

    detalle={
        'codigo_producto': codigo_producto,
        'nombre_producto': nombre_producto,
        'categoria': categoria,
        'precio_producto': precio_producto,
        'cantidad': cantidad
    }
    #.get para capturar el detalle de la línea 10: key del atributo de la boleta
    #que es una lista
    #.append(detalle) acá se está llamando al diccionario
    boleta.get('detalle').append(detalle)
    respuesta= input('¿Desea continuas? si/no: ')
    if respuesta == 'no':
        estado = False

print('IMPRESIÓN DE LA BOLETA EN LA CONSOLA')

#al trabajar con interporlación los datos ingresados
# deben estar con doble comilla
print(f'Cliente: {boleta.get("rut_cliente")}')
print(f'Correo: {boleta.get("correo_cliente")}')
print(f'Fecha: {boleta.get("fecha_actual")}')

total=0
#detalle = lista
for producto in boleta.get('detalle'):
    #[] capturar la clave del diccionario
    print(f'{producto["codigo_producto"]} {producto["nombre_producto"]} {producto["cantidad"]} {producto["precio_producto"]} {int(producto["cantidad"]) * int(producto["precio_producto"])}')
    total += int(producto["cantidad"]) * int(producto["precio_producto"])
print(f'Total a pagar: {total}')

#ESCRITURA DE ARCHIVO--> SIMULANDO IMPRESIÓN DE BOLETA
#
with open('boleta.txt', 'w') as archivo:
    archivo.write(f'Cliente: {boleta.get("rut_cliente")}\n')
    archivo.write(f'Correo: {boleta.get("correo_cliente")}\n')
    archivo.write(f'Fecha: {boleta.get("fecha_actual")}\n')
    for producto in boleta.get('detalle'):
        archivo.write(f'{producto["codigo_producto"]} {producto["nombre_producto"]} {producto["cantidad"]} {producto["precio_producto"]} {int(producto["cantidad"]) * int(producto["precio_producto"])}\n')
    archivo.write(f'Total a pagar: {total}')
