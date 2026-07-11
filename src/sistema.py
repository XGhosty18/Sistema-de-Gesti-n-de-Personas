# METODOS PROCEDIMENTALES Y FUNCIONES DE ENTRADA DE DATOS

from src.funcional import filtrar_por_nombre
from src.personas import Cliente, Empleado, ClienteVIP


# FUNCIONES PROCEDIMENTALES DE ENTRADA DE DATOS

def leer_texto(mensaje):
    """Funcion generica para entrada de texto."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("  [!] Error: el valor no puede estar vacio.")


def leer_entero(mensaje):
    """Funcion generica para entrada de numeros enteros."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  [!] Error: ingrese un numero entero valido.")


def leer_flotante(mensaje):
    """Funcion generica para entrada de numeros decimales."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor >= 0:
                return valor
            print("  [!] Error: el valor no puede ser negativo.")
        except ValueError:
            print("  [!] Error: ingrese un numero valido.")


# USO DE SETS (COLECCIONES) PARA VALIDACION

def obtener_codigos_existentes(personas):
    """
    Usa un SET (conjunto) para almacenar los codigos.
    Los sets no permiten duplicados y sus busquedas son O(1).
    """
    codigos = set()
    for p in personas:
        if hasattr(p, 'codigo_cliente'):
            codigos.add(p.codigo_cliente)
        if hasattr(p, 'codigo_empleado'):
            codigos.add(p.codigo_empleado)
    return codigos


# FUNCIONES PROCEDIMENTALES DEL SISTEMA

def registrar_cliente(personas):
    print("\n  --- REGISTRAR CLIENTE ---")
    codigos_set = obtener_codigos_existentes(personas)
    
    codigo = leer_texto("  Codigo de cliente: ")
    if codigo in codigos_set:
        print("  [!] Error: codigo de cliente ya existe en el sistema.")
        return

    nombre = leer_texto("  Nombre: ")
    direccion = leer_texto("  Direccion: ")
    telefono = leer_texto("  Telefono: ")
    email = leer_texto("  Email: ")
    descuento = leer_entero("  Descuento (%): ")

    cliente = Cliente(nombre, direccion, telefono, email, codigo, descuento)
    personas.append(cliente)
    print(f"  [OK] Cliente '{nombre}' registrado.")


def registrar_empleado(personas):
    print("\n  --- REGISTRAR EMPLEADO ---")
    codigos_set = obtener_codigos_existentes(personas)
    
    codigo = leer_texto("  Codigo de empleado: ")
    if codigo in codigos_set:
        print("  [!] Error: codigo de empleado ya existe en el sistema.")
        return

    nombre = leer_texto("  Nombre: ")
    direccion = leer_texto("  Direccion: ")
    telefono = leer_texto("  Telefono: ")
    email = leer_texto("  Email: ")
    salario = leer_flotante("  Salario: S/ ")
    puesto = leer_texto("  Puesto: ")

    empleado = Empleado(nombre, direccion, telefono, email, codigo, salario, puesto)
    personas.append(empleado)
    print(f"  [OK] Empleado '{nombre}' registrado.")


def registrar_cliente_vip(personas):
    print("\n  --- REGISTRAR CLIENTE VIP (Herencia Multiple) ---")
    codigos_set = obtener_codigos_existentes(personas)
    
    cod_cliente = leer_texto("  Codigo de cliente: ")
    cod_empleado = leer_texto("  Codigo de empleado: ")
    
    if cod_cliente in codigos_set or cod_empleado in codigos_set:
         print("  [!] Error: Uno de los codigos ingresados ya existe en el sistema.")
         return

    nombre = leer_texto("  Nombre: ")
    direccion = leer_texto("  Direccion: ")
    telefono = leer_texto("  Telefono: ")
    email = leer_texto("  Email: ")
    descuento = leer_entero("  Descuento (%): ")
    salario = leer_flotante("  Salario: S/ ")
    puesto = leer_texto("  Puesto: ")
    puntos = leer_entero("  Puntos VIP: ")

    vip = ClienteVIP(nombre, direccion, telefono, email,
                     cod_cliente, descuento,
                     cod_empleado, salario, puesto, puntos)
    personas.append(vip)
    print(f"  [OK] Cliente VIP '{nombre}' registrado.")


# VISTA ESTILIZADA EN CONSOLA

def mostrar_todos(personas):
    """Muestra los datos utilizando un formato de tabla estilizada en consola."""
    print("\n" + "=" * 75)
    print(f"{'TIPO':<15} | {'NOMBRE':<20} | {'CONTACTO':<15} | {'DETALLE EXTRA':<15}")
    print("-" * 75)
    
    if not personas:
        print("  No hay personas registradas en la base de datos.")
        print("=" * 75)
        return

    for p in personas:
        tipo = type(p).__name__
        nombre = p.nombre[:19]
        contacto = p.telefono[:14]
        
        detalle = ""
        if tipo == "Cliente":
            detalle = f"Desc: {p.descuento}%"
        elif tipo == "Empleado":
            detalle = f"Sueldo: S/{p.salario}"
        elif tipo == "ClienteVIP":
            detalle = f"Ptos: {p.puntos_vip}"
            
        print(f"{tipo:<15} | {nombre:<20} | {contacto:<15} | {detalle:<15}")
    print("=" * 75)


def buscar_persona(personas):
    print("\n--- BUSCAR PERSONA ---")
    if not personas:
        print("  [!] No hay personas registradas.")
        return
    nombre = input("  Ingrese nombre a buscar: ").strip().lower()
    encontrados = filtrar_por_nombre(personas, nombre)
    if not encontrados:
        print("  [!] No se encontraron personas con ese nombre.")
        return
    for p in encontrados:
        print(f"\n  {type(p).__name__}: {p.nombre} ({p.email})")


def demo_polimorfismo(personas):
    """Demostracion explicita de polimorfismo."""
    print("\n--- DEMOSTRACION DE POLIMORFISMO ---")
    if not personas:
        print("  [!] Registre al menos una persona primero.")
        return

    print("  Llamando a mostrar_info() en cada objeto...")
    print("  Cada clase responde de forma DISTINTA aunque el metodo")
    print("  se llame IGUAL. Eso es polimorfismo.\n")

    for p in personas:
        print(f"  >> Objeto: {type(p).__name__}")
        print(f"     Clase base (MRO): {[c.__name__ for c in type(p).__mro__]}")
        print(f"     {p.mostrar_info()}")
        print()
