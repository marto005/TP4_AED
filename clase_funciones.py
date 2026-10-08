import csv
import os
import pickle


class Ticket:
    def __init__(self, codigo, patente, tipo_vehiculo, forma_pago, pais_cabina, km_recorridos, pais_vehiculo):
        self.codigo = codigo
        self.patente = patente
        self.tipo_vehiculo = tipo_vehiculo
        self.forma_pago = forma_pago
        self.pais_cabina = pais_cabina
        self.km_recorridos = km_recorridos
        self.pais_vehiculo = pais_vehiculo

    def __str__(self):
        cad = f'Código: {self.codigo:<12} Patente: {self.patente:<10} Tipo de Vehículo: {self.tipo_vehiculo:<15} ' \
              f'Forma de Pago: {self.forma_pago:<13} País de Cabina: {self.pais_cabina:<13} ' \
              f'Kilómetros Recorridos: {self.km_recorridos:<8} Pais del vehiculo: {self.pais_vehiculo}'
        return cad


# Complemento consigna 1
def cabina(cabina):
    if cabina == 0:
        cabina = 'Argentina'
    elif cabina == 1:
        cabina = 'Bolivia'
    elif cabina == 2:
        cabina = 'Brasil'
    elif cabina == 3:
        cabina = 'Paraguay'
    elif cabina == 4:
        cabina = 'Uruguay'
    else:
        cabina = 'Pais invalido'
    return cabina


# Complemento consigna 1
def vehiculo(tipo_vehiculo):
    if tipo_vehiculo == 0:
        tipo_vehiculo = 'Motocicleta'
    elif tipo_vehiculo == 1:
        tipo_vehiculo = 'Automovil'
    elif tipo_vehiculo == 2:
        tipo_vehiculo = 'Camion'
    else:
        tipo_vehiculo = 'Tipo invalido'

    return tipo_vehiculo


# Complemento consigna 1
def pago(form_pago):
    if form_pago == 1:
        form_pago = 'Manual'
    elif form_pago == 2:
        form_pago = 'Telepeaje'
    else:
        form_pago = 'Forma de pago invalida'
    return form_pago


# Determinar el pais de procedencia del vehiculo
def pais_vehiculo(patente):
    nombres_paises = ("Chile", "Argentina", "Bolivia", "Brasil", "Paraguay", "Uruguay", "Otro pais")
    if len(patente) == 7:
        pri_c = patente[0]
        seg_c = patente[1]
        ter_c = patente[2]
        cuar_c = patente[3]
        quin_c = patente[4]
        sexto_c = patente[5]
        sept_c = patente[6]
        if pri_c.isalpha() and seg_c.isalpha() and ter_c.isdigit() and cuar_c.isdigit() \
                and quin_c.isdigit() and sexto_c.isalpha() and sept_c.isalpha():
            return nombres_paises[1]
        elif pri_c.isalpha() and seg_c.isalpha() and ter_c.isdigit() and cuar_c.isdigit() \
                and quin_c.isdigit() and sexto_c.isdigit() and sept_c.isdigit():
            return nombres_paises[2]
        elif pri_c.isalpha() and seg_c.isalpha() and ter_c.isalpha() and cuar_c.isdigit() \
                and quin_c.isalpha() and sexto_c.isdigit() and sept_c.isdigit():
            return nombres_paises[3]
        elif pri_c.isalpha() and seg_c.isalpha() and ter_c.isalpha() and cuar_c.isalpha() \
                and quin_c.isdigit() and sexto_c.isdigit() and sept_c.isdigit():
            return nombres_paises[4]
        elif pri_c.isalpha() and seg_c.isalpha() and ter_c.isalpha() and cuar_c.isdigit() \
                and quin_c.isdigit() and sexto_c.isdigit() and sept_c.isdigit():
            return nombres_paises[5]
        else:
            return nombres_paises[6]
    if len(patente) == 6:
        pri_c = patente[0]
        seg_c = patente[1]
        ter_c = patente[2]
        cuar_c = patente[3]
        quin_c = patente[4]
        sexto_c = patente[5]
        if pri_c.isalpha() and seg_c.isalpha() and ter_c.isalpha() and \
                cuar_c.isalpha() and quin_c.isdigit() and sexto_c.isdigit():
            return nombres_paises[0]
        else:
            return nombres_paises[6]
    else:
        return nombres_paises[6]


# Consigna 1
def generar_archivo_binario(archivo_csv, archivo_bin):
    eleccion = 1
    if os.path.exists(archivo_bin):
        eleccion = existe_binario()

    if eleccion == 1:
        if os.path.exists(archivo_csv):
            print()
            print('-' * 60)
            print('Cargando datos, por favor aguarde....')
            with open(archivo_csv, 'rt', newline='', encoding='utf-8') as lector_csv, \
                    open(archivo_bin, 'wb') as creador_binario:
                next(lector_csv, None)
                lector = csv.DictReader(lector_csv)
                for registro in lector:
                    codigo = int(registro['codigo'])
                    patente = registro['patente'].strip().upper()
                    tipo = int(registro['tipo_vehiculo'])
                    form_pago = int(registro['forma_pago'])
                    pais_cabina = int(registro['pais_cabina'])
                    distancia = int(registro['distancia'])

                    ticket = Ticket(codigo, patente, vehiculo(tipo), pago(form_pago),
                                    cabina(pais_cabina), distancia, pais_vehiculo(patente))
                    pickle.dump(ticket, creador_binario)
            print('Datos cargados desde CSV y archivo binario creado con exito.')
        else:
            print('El archivo', archivo_csv, 'no existe...\n')
    else:
        print('-' * 60)
        print('No se realizaron modificaciones.')
    print('-' * 60, '\n')


# Funcion para validar distintos puntos de distintas consignas
def validar_opcion(opcion, limite_inferior, limite_superior, mensaje):
    try:
        valor = int(opcion)
    except (TypeError, ValueError):
        print(mensaje)
        return -1
    if limite_inferior <= valor <= limite_superior:
        return valor
    print(mensaje)
    return -1


def codigo_existente(codigo, archivo_binario):
    with open(archivo_binario, 'rb') as lector:
        tamanio = os.path.getsize(archivo_binario)
        while lector.tell() < tamanio:
            if pickle.load(lector).codigo == codigo:
                return True
    return False


# Consigna 2
def cargar_por_teclado(archivo_binario):
    mensaje = '\nOpcion invalida, cargue una correcta.'
    print()
    print('-' * 90)
    print('Ingrese los datos del ticket:')
    codigo = validar_opcion(input("Código del ticket: "), 0, 2147483647, mensaje)
    while codigo == -1 or codigo_existente(codigo, archivo_binario):
        if codigo != -1:
            print('Ya existe un ticket con ese código.')
        print(mensaje)
        codigo = validar_opcion(input("Código del ticket: "), 0, 2147483647, mensaje)

    patente = input("Patente del vehículo: ")
    patente = patente.upper()
    while patente == "":
        print(mensaje)
        patente = input("Patente del vehículo: \n")

    tipo_vehiculo = validar_opcion(input("Tipo de vehículo (0: motocicleta, 1: automóvil, 2: camión): "), 0, 2, mensaje)
    while tipo_vehiculo == -1:
        tipo_vehiculo = validar_opcion(input("Tipo de vehículo (0: motocicleta, 1: automóvil, 2: camión): "), 0, 2, mensaje)

    forma_pago = validar_opcion(input("Forma de pago (1: manual, 2: telepeaje): "), 1, 2, mensaje)
    while forma_pago == -1:
        forma_pago = validar_opcion(input("Forma de pago (1: manual, 2: telepeaje): "), 1, 2, mensaje)

    pais_cabina = validar_opcion(input("País de la cabina "
                                      "(0: Argentina, 1: Bolivia, 2: Brasil, 3: Paraguay, 4: Uruguay): "), 0, 4, mensaje)
    while pais_cabina == -1:
        pais_cabina = validar_opcion(input("País de la cabina "
                                          "(0: Argentina, 1: Bolivia, 2: Brasil, 3: Paraguay, 4: Uruguay): "), 0, 4, mensaje)

    km_recorridos = validar_opcion(input("Kilómetros recorridos desde la cabina anterior"
                                         " (en caso de ser la primera ingrese 0): "), 0, 2147483647, mensaje)
    while km_recorridos == -1:
        km_recorridos = validar_opcion(input("Kilómetros recorridos desde la cabina anterior"
                                             " (en caso de ser la primera ingrese 0): "), 0, 2147483647, mensaje)

    ticket = Ticket(codigo, patente, vehiculo(tipo_vehiculo), pago(forma_pago),
                    cabina(pais_cabina), km_recorridos, pais_vehiculo(patente))
    with open(archivo_binario, 'ab') as creador_binario:
        pickle.dump(ticket, creador_binario)
    print("Registro agregado exitosamente.")
    print('-' * 90)


# Para asegurar que la consigna 1 ya se realizo
def existe_binario():
    print()
    print('-' * 123)
    eleccion = input('Advertencia: Si crea un nuevo archivo, se eliminarán todos los datos ya cargados'
                     ' en el archivo anterior. ¿Desea continuar?\n0. No\n1. Sí\nPor favor, ingrese su elección: ')
    eleccion = validar_opcion(eleccion, 0, 1, 'Por favor, ingrese una opción válida (0 o 1).')
    while eleccion == -1:
        eleccion = validar_opcion(input('¿Desea continuar?\n0. No\n1. Sí\nPor favor, ingrese su elección: '),
                                  0, 1, 'Por favor, ingrese una opción válida (0 o 1).')
        if eleccion == 0:
            break
    if eleccion == 1:
        print('\nLos datos existentes han sido eliminados.')
        return 1
    else:
        return 0


# Consigna 3
def mostrar_tickets(archivo_binario):
    print()
    print('-' * 200)
    if os.path.exists(archivo_binario):
        print("Tickets almacenados:\n")
        with open(archivo_binario, "rb") as mb:
            t = os.path.getsize(archivo_binario)
            while mb.tell() < t:
                print(pickle.load(mb))
        print()
    else:
        print("El archivo", archivo_binario, "no existe...\n")
    print('-' * 200)


# Consigna 4
def buscar_patente(patente, archivo_binario):
    patente = patente.strip().upper()
    cont = 0

    print('Búsqueda para la patente:', patente)
    print('-' * 200)

    with open(archivo_binario, 'rb') as lector:
        t = os.path.getsize(archivo_binario)
        while lector.tell() < t:
            ticket = pickle.load(lector)
            if ticket.patente.upper() == patente:
                print(ticket)
                cont += 1

    if cont == 0:
        print('No se encontró ningún ticket que coincida con la patente:', patente)
    else:
        print(f'Se encontraron un total de {cont} ticket(s) que coinciden con la patente: {patente}')

    print('-' * 200)
    print()


# Consigna 5
def buscar_codigo(codigo, archivo_binario):
    encontrado = False

    print('Búsqueda para el código:', codigo)
    print('-' * 200)

    with open(archivo_binario, 'rb') as lector:
        t = os.path.getsize(archivo_binario)
        while lector.tell() < t:
            ticket = pickle.load(lector)
            if ticket.codigo == codigo:
                print('Se encontró coincidencia con el ticket:')
                print(ticket)
                encontrado = True
                break

    if not encontrado:
        print('No se encontró coincidencia.')

    print('-' * 200)
    print()


# Para matriz
def cabina_tipo_matriz(pais_cabina, tipo_vehiculo):
    if pais_cabina == 'Argentina':
        pais_cabina = 0
    elif pais_cabina == 'Bolivia':
        pais_cabina = 1
    elif pais_cabina == 'Brasil':
        pais_cabina = 2
    elif pais_cabina == 'Paraguay':
        pais_cabina = 3
    else:
        pais_cabina = 4

    if tipo_vehiculo == 'Motocicleta':
        tipo_vehiculo = 0
    elif tipo_vehiculo == 'Automovil':
        tipo_vehiculo = 1
    else:
        tipo_vehiculo = 2

    return pais_cabina, tipo_vehiculo


# Usado en consigna 6 y 7
def cont_matriz(archi_bin):
    mat = [[0] * 5 for i in range(3)]
    with open(archi_bin, 'rb') as lector:
        t = os.path.getsize(archi_bin)
        while lector.tell() < t:
            ticket = pickle.load(lector)
            n, m = cabina_tipo_matriz(ticket.pais_cabina, ticket.tipo_vehiculo)
            mat[m][n] += 1
    return mat


# Consigna 6
def mostrar(mat):
    print()
    print('\nCantidad total de vehículos por tipo de vehículo y país de cabina:')
    print('-' * 50)
    print(f'{"Tipo de vehículo":<23}{"País de cabina":<15}{"Total":>10}')
    print('-' * 50)

    for i in range(3):
        for j in range(5):
            if mat[i][j] > 0:
                tipo = vehiculo(i)
                pais_cabina = cabina(j)
                total = mat[i][j]
                print(f'  {tipo:<23} {pais_cabina:<17} {total:>4}')
                if (i == 0 and j == 4) or (i == 1 and j == 4):
                    print('-' * 50)

    print('-' * 50, '\n')


# Consigna 7
def totalizar_fil_col_matriz(mat):
    tipo_vehiculo = 0
    pais_cabina = 0
    m = len(mat)
    n = len(mat[0])

    print('\n' + '*' * 50)
    print('Cantidad total de vehículos por tipo:')
    print('-' * 50)
    print(f'{"Tipo de Vehículo":<30}{"Total":>20}')
    print('-' * 50)

    for i in range(m):
        acumulador = 0
        for j in range(n):
            acumulador += mat[i][j]
            tipo_vehiculo = vehiculo(i)
        print(f'{tipo_vehiculo:<30}{acumulador:>20}')

    print('\n' + '*' * 50)
    print('Cantidad total por cabina:')
    print('-' * 50)
    print(f'{"Cabina":<30}{"Total":>20}')
    print('-' * 50)

    for j in range(n):
        acumulador_cab = 0
        for k in range(m):
            acumulador_cab += mat[k][j]
            pais_cabina = cabina(j)
        print(f'{pais_cabina:<30}{acumulador_cab:>20}')

    print('*' * 50, '\n')


# Promedio consigna 8
def promedio_distancia(archivo_binario):
    cont = 0
    acum = 0
    with open(archivo_binario, 'rb') as lector:
        t = os.path.getsize(archivo_binario)
        while lector.tell() < t:
            ticket = pickle.load(lector)
            acum += ticket.km_recorridos
            cont += 1
    if cont != 0:
        promedio = round(acum / cont, 2)
    else:
        promedio = 0
    print()
    print('-' * 200)
    print('La distancia promedio recorrida desde la ultima cabina por todos '
          'los vehiculos del registro es de:', str(promedio) + 'km')
    return promedio


def generar_arreglo(archivo_binario, promedio):
    arreglo = []
    with open(archivo_binario, 'rb') as lector:
        t = os.path.getsize(archivo_binario)
        while lector.tell() < t:
            ticket = pickle.load(lector)
            if ticket.km_recorridos > promedio:
                add_in_order(arreglo, ticket)
    for i in range(len(arreglo)):
        print(arreglo[i])
    print('-' * 200, '\n')


def add_in_order(v, ticket):
    n = len(v)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if v[c].km_recorridos == ticket.km_recorridos:
            pos = c
            break
        if ticket.km_recorridos < v[c].km_recorridos:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [ticket]
