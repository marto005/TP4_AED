# Sistema de gestión de tickets de peajes

Este programa permite administrar los tickets registrados en distintas cabinas de peaje. Está desarrollado en Python y utiliza un archivo CSV como fuente inicial de datos y un archivo binario para guardar los tickets.

## Archivos principales

- `principal.py`: contiene el menú principal y controla la interacción con el usuario.
- `clase_funciones.py`: define la clase `Ticket` y las funciones de carga, búsqueda, conteo y cálculo.
- `peajes-tp4.csv`: archivo de entrada con los registros iniciales.
- `tickets.dat`: archivo binario generado por el programa. Se crea al utilizar la opción 1.

## Cómo ejecutar el programa

Desde una terminal ubicada en la carpeta del proyecto, ejecutar:

```bash
python principal.py
```

Al iniciar, se muestra un menú de opciones.

## Opciones disponibles

### 1. Crear archivo binario desde CSV

Lee los registros de `peajes-tp4.csv`, convierte cada fila en un objeto `Ticket` y los guarda en `tickets.dat`.

Si `tickets.dat` ya existe, el programa pregunta si se desea reemplazarlo. Al confirmar, se eliminan los datos anteriores y se genera nuevamente el archivo.

Cada ticket contiene:

- Código.
- Patente del vehículo.
- Tipo de vehículo.
- Forma de pago.
- País de la cabina.
- Distancia recorrida desde la cabina anterior.
- País de procedencia del vehículo, calculado a partir del formato de la patente.

### 2. Cargar datos de un ticket por teclado

Permite ingresar manualmente un nuevo ticket y agregarlo al final de `tickets.dat`.

Se solicitan el código, la patente, el tipo de vehículo, la forma de pago, el país de la cabina y los kilómetros recorridos.

### 3. Mostrar todos los tickets

Lee el archivo binario y muestra en pantalla todos los tickets almacenados.

### 4. Buscar tickets por patente

Solicita una patente y muestra todos los tickets asociados a ella.

### 5. Buscar un ticket por código

Solicita el código de un ticket y muestra el primer registro que coincida.

### 6. Contar vehículos por tipo y país de cabina

Calcula cuántos vehículos hay para cada combinación de:

- Motocicleta, automóvil o camión.
- Argentina, Bolivia, Brasil, Paraguay o Uruguay.

Solo muestra las combinaciones cuyo total sea mayor que cero.

### 7. Totalizar vehículos por tipo y por país de cabina

Muestra dos totales:

1. La cantidad total de motocicletas, automóviles y camiones.
2. La cantidad total de vehículos registrados en cada país de cabina.

### 8. Calcular la distancia promedio

Calcula la distancia promedio recorrida entre cabinas y muestra los tickets cuya distancia sea superior a ese promedio.

Los tickets mostrados se ordenan de menor a mayor según los kilómetros recorridos.

### 0. Salir

Finaliza el programa.

## Formato del archivo CSV

El archivo CSV contiene una cabecera y luego una fila por ticket, con las siguientes columnas:

```text
codigo,patente,tipo_vehiculo,forma_pago,pais_cabina,distancia
```

Los códigos numéricos utilizados son:

- `tipo_vehiculo`: `0` motocicleta, `1` automóvil, `2` camión.
- `forma_pago`: `1` pago manual, `2` telepeaje.
- `pais_cabina`: `0` Argentina, `1` Bolivia, `2` Brasil, `3` Paraguay, `4` Uruguay.

## Validaciones y controles

- Los datos ingresados por teclado se convierten al mismo formato que los datos importados desde el CSV.
- No se permiten códigos de ticket repetidos.
- Las opciones numéricas vuelven a solicitar el dato si se ingresa un valor inválido.
- Las búsquedas por patente no distinguen entre mayúsculas y minúsculas.
- Los archivos se cierran automáticamente después de cada operación.
