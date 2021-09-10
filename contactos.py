opcion=1
contactos = []


while opcion !=0:
    print('.............................')
    print('  SELECCIONE UNA OPCION DEL')
    print('         MENÚ     ')
    print('1. crear contacto')
    print('2. leer todos los contactos')
    print('3. actualizar un contacto')
    print('4. eliminar contacto')
    print('5. SALIR')
    opcion= int(input())

    if opcion == 1:
        print('CREAR NUEVO CONTACTO')
        nombre= input('NOMBRE: ')
        apellido= input('APELLIDO: ')
        celuar= input('CELULAR: ')
        correo= input('CORREO: ')

        contactos.append({
            'nombre': nombre,
            'apellido': apellido,
            'celular': celuar,
            'correo': correo,
        })
        input('GUARDADO / presiones tecla para continuar')
    elif opcion == 2:
        print('LISTAR CONTACTOS')
        for lis in contactos:
            print(contactos['nombre'])
        input('GUARDADO / presiones tecla para continuar')
    elif opcion == 3:
        contactos['nombre'] = input('NOMBRE: ')
        print(contactos['nombre'])
        input('GUARDADO / presiones tecla para continuar')