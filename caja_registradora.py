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

print(boleta)

#productos_en_compra: [codigo, nombre, categoria, cantidad, precio]