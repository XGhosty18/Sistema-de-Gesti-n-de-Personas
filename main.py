# SISTEMA DE VENTAS Y FACTURACION

from src.sistema import (
    registrar_cliente, registrar_empleado, registrar_cliente_vip,
    mostrar_todos, buscar_persona, demo_polimorfismo
)
from src.analisis_datos import mostrar_estadisticas
from src.persistencia import cargar_datos, guardar_datos

# USO DE TUPLAS
ESTILOS = (
    "=" * 70,
    "-" * 70,
    "*" * 70,
    "~" * 70
)

# FUNCIONES DE DISEÑO DE SALIDA EN CONSOLA
def imprimir_cabecera(titulo, estilo=0):
    """Diseño de salida: Centra el texto y coloca bordes estéticos."""
    print(f"\n{ESTILOS[estilo]}")
    print(f"{titulo:^70}")
    print(f"{ESTILOS[estilo]}")

def imprimir_pie():
    print(f"{ESTILOS[1]}\n")


# FUNCIONES DE MENÚS (ENTRADA Y SALIDA DE DATOS)
def menu_principal():
    imprimir_cabecera("SISTEMA DE GESTIÓN DE PERSONAS", 0)
    print("  [ 1 ] Módulo de Registros (Clientes/Empleados)")
    print("  [ 2 ] Módulo de Consultas y Reportes")
    print("  [ 3 ] Demostrar Polimorfismo Técnico")
    print("  [ 4 ] Guardar Datos y Salir del Sistema")
    imprimir_pie()
    return input("  > Seleccione una opción principal: ").strip()


def menu_registros(personas):
    activo = True
    while activo:
        imprimir_cabecera("MÓDULO DE REGISTROS", 1)
        print("  [ 1 ] Alta de Cliente Regular")
        print("  [ 2 ] Alta de Empleado")
        print("  [ 3 ] Alta de Cliente VIP (Herencia Múltiple)")
        print("  [ 4 ] Volver al Menú Principal")
        imprimir_pie()
        
        opcion = input("  > Elija qué registrar: ").strip()
        
        if opcion == '1':
            registrar_cliente(personas)
        elif opcion == '2':
            registrar_empleado(personas)
        elif opcion == '3':
            registrar_cliente_vip(personas)
        elif opcion == '4':
            activo = False
        else:
            print("  [!] Opción inválida. Intente de nuevo.")


def menu_consultas(personas):
    activo = True
    while activo:
        imprimir_cabecera("MÓDULO DE CONSULTAS Y REPORTES", 1)
        print("  [ 1 ] Directorio Completo (Vista de Tabla)")
        print("  [ 2 ] Búsqueda de Persona por Nombre")
        print("  [ 3 ] Análisis de Datos (pandas y NumPy)")
        print("  [ 4 ] Volver al Menú Principal")
        imprimir_pie()
        
        opcion = input("  > Elija un reporte: ").strip()
        
        if opcion == '1':
            mostrar_todos(personas)
        elif opcion == '2':
            buscar_persona(personas)
        elif opcion == '3':
            mostrar_estadisticas(personas)
        elif opcion == '4':
            activo = False
        else:
            print("  [!] Opción inválida. Intente de nuevo.")


# ORQUESTADOR PRINCIPAL
def main():
    imprimir_cabecera("INICIANDO SISTEMA...", 3)

    personas = cargar_datos()
    
    if personas:
        print(f"  [OK] Base de datos cargada: {len(personas)} registro(s).")
    else:
        print("  [!] Base de datos vacía. Iniciando de cero.")

    sistema_activo = True
    while sistema_activo:
        opcion = menu_principal()
        
        match opcion:
            case '1':
                menu_registros(personas)
            case '2':
                menu_consultas(personas)
            case '3':
                demo_polimorfismo(personas)
            case '4':
                imprimir_cabecera("GUARDANDO Y CERRANDO SISTEMA", 0)
                guardar_datos(personas)
                print(" ¡Hasta pronto!")
                sistema_activo = False
            case _:
                print("\n  [!] Error: Seleccione una opción válida (1-4).")

if __name__ == "__main__":
    main()
