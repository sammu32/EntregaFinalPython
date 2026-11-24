import dataset  # Importa la librería dataset para trabajar con bases de datos SQLite de forma sencilla

miBase = dataset.connect("sqlite:///datos.db")  # Conecta (o crea si no existe) la base de datos datos.db

tabla = miBase["Productos"]  # Obtiene la tabla Productos (la crea automáticamente si no existe)


while True:  # Bucle principal del programa. Se repite hasta que el usuario elija salir.

    opciones = input("""
    L - Listar
    A - Agregar 
    Q - Quitar por nombre
    I - Quitar por ID
    B - Buscar primero
    T - Buscar todo 
    S - Salir
    
    """)  # Muestra el menú y guarda la opción elegida por el usuario

    match opciones:  # Evalúa la opción ingresada

        case "B":  # Buscar el primer producto que coincida

            busco = input("\nProducto a buscar: ").strip()  # Pide el nombre y elimina espacios al inicio/final

            encontrado = tabla.find_one(Nombre=busco)  # Busca el primer registro cuyo Nombre coincida

            print(f'{busco} esta en la posicion {encontrado["id"]}')  # Muestra el ID encontrado

        case "T":  # Buscar todos los productos con ese nombre

            busco = input("\nBuscar en toda la base: ").strip()  # Pide el nombre a buscar

            encontrado = tabla.find(Nombre=busco)  # Devuelve todos los registros coincidentes

            for cosa in encontrado:  # Recorre cada resultado encontrado

                print(f'{busco} esta en el ID: {cosa["id"]}')  # Muestra el ID de cada coincidencia

        case "S":  # Salir del programa

            break  # Finaliza el bucle while

        case "A":  # Agregar un nuevo producto

            nombreProducto = input("\nNombre: ")  # Solicita el nombre del producto

            precioProducto = float(input("\nPrecio: "))  # Solicita el precio y lo convierte a número decimal

            categoriaProducto = input("\nCategoría: ")  # Solicita la categoría

            productoAgregar = {
                "Nombre": nombreProducto,
                "Precio": precioProducto,
                "Categoria": categoriaProducto
            }  # Crea un diccionario con los datos del producto

            tabla.insert(productoAgregar)  # Inserta el diccionario como un nuevo registro en la tabla

        case "L":  # Listar todos los productos

            for cosa in tabla:  # Recorre cada registro de la tabla

                print(
                    f"ID: {cosa['id']} | "
                    f"Nombre: {cosa['Nombre']} | "
                    f"Precio: {cosa['Precio']} | "
                    f"Categoria: {cosa['Categoria']}"
                )  # Muestra todos los datos del producto

        case "Q":  # Eliminar productos por nombre

            quitarProducto = input("\nProducto a quitar: ")  # Solicita el nombre del producto

            tabla.delete(Nombre=quitarProducto)  # Elimina todos los registros con ese nombre

            print(f"*** {quitarProducto} eliminado con éxito ***")  # Mensaje de confirmación

        case "I":  # Eliminar un producto por ID

            quitarProducto = int(input("\nId de producto a quitar: "))  # Solicita el ID y lo convierte a entero

            tabla.delete(id=quitarProducto)  # Elimina el registro cuyo ID coincida

            print(f"*** Producto con ID: {quitarProducto} eliminado con éxito ***")  # Confirmación
