import datetime

boleta ={}
rut_cliente=input('Ingrese el rut del cliente para asociarlo a sus puntos: ')
correo_cliente = input('Ingrese el correo del cliente para su boleta virtual: ')
fecha_actual= datetime.date.today()
boleta['rut_cliente']= rut_cliente
boleta['correo_cliente']=correo_cliente
boleta['fecha_actual']= fecha_actual

print(boleta)

#productos_en_compra: [codigo, nombre, categoria, cantidad, precio]