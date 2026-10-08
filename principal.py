from clase_funciones import *

def principal():
    arch_csv = 'peajes-tp4.csv'
    arch_binario = 'tickets.dat'
    opcion = True

    while opcion:
        print('\n' + '*' * 86)
        print('*' * 35 + 'Menú de Opciones' + '*' * 35)
        print('*' * 86)
        print('1. Crear archivo binario desde CSV')
        print('2. Cargar datos de un ticket por teclado')
        print('3. Mostrar todos los tickets')
        print('4. Buscar tickets por patente')
        print('5. Buscar ticket por codigo')
        print('6. Calcular cantidad de vehículos según cada tipo de vehículo y país de cabina ')
        print('7. Totalizar cantidad de vehículos por tipo y país de cabina')
        print('8. Calcular distancia promedio y mostrar tickets con distancia superior al promedio')
        print('0. Salir')
        print('*' * 86)

        opcion = input('Elija una opción: ')
        try:
            opcion_numerica = int(opcion)
        except ValueError:
            print('Porfavor ingrese una opción válida.')
            continue

        if 0 <= opcion_numerica <= 8:
            if opcion == '0':
                print('\n' + '*' * 60)
                print('¡Gracias por usar el sistema de gestión de tickets!')
                print('Esperamos que hayas tenido una experiencia agradable.')
                print('¡Hasta la próxima!')
                print('*' * 60)
                opcion = False
            elif opcion == '1':
                generar_archivo_binario(arch_csv, arch_binario)
            elif not os.path.exists(arch_binario):
                print()
                print('-' * 60)
                print('No se han encontrado datos registrados en el archivo binario.')
                print('Por favor, primero ingrese los datos utilizando la opción 1.')
                print('-' * 60)
            else:
                if opcion == "2":
                    cargar_por_teclado(arch_binario)
                elif opcion == "3":
                    mostrar_tickets(arch_binario)
                elif opcion == '4':
                    patente = input('\nPatente que desea buscar:').strip().upper()
                    buscar_patente(patente, arch_binario)
                elif opcion == '5':
                    try:
                        codigo = int(input('\nCodigo que desea buscar:'))
                    except ValueError:
                        codigo = -1
                    while codigo < 0:
                        print('Por favor ingrese un codigo valido.')
                        try:
                            codigo = int(input('\nCodigo que desea buscar:'))
                        except ValueError:
                            codigo = -1
                    buscar_codigo(codigo, arch_binario)
                elif opcion == '6':
                    mostrar(cont_matriz(arch_binario))
                elif opcion == '7':
                    totalizar_fil_col_matriz(cont_matriz(arch_binario))
                elif opcion == '8':
                    promedio = promedio_distancia(arch_binario)
                    generar_arreglo(arch_binario, promedio)
        else:
            print('Porfavor ingrese una opcion valida.')


if __name__ == '__main__':
    principal()
