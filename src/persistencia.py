
"""Persistencia JSON del sistema, separada de la interfaz y del dominio."""

import json
from pathlib import Path
from typing import Any

from src.personas import Cliente, ClienteVIP, Empleado, Persona


ARCHIVO = Path(__file__).resolve().parent.parent / "datos" / "datos.json"


def _crear_persona(item: dict[str, Any]) -> Persona | None:
    """Reconstruye el objeto apropiado a partir de un registro JSON."""
    datos_comunes = (
        item["nombre"],
        item["direccion"],
        item["telefono"],
        item["email"],
    )
    tipo = item.get("tipo")

    if tipo == "Cliente":
        return Cliente(
            *datos_comunes, item["codigo_cliente"], item["descuento"]
        )
    if tipo == "Empleado":
        return Empleado(
            *datos_comunes,
            item["codigo_empleado"],
            item["salario"],
            item["puesto"],
        )
    if tipo == "ClienteVIP":
        return ClienteVIP(
            *datos_comunes,
            item["codigo_cliente"],
            item["descuento"],
            item["codigo_empleado"],
            item["salario"],
            item["puesto"],
            item["puntos_vip"],
        )
    return None


def guardar_datos(personas: list[Persona]) -> None:
    """Serializa todos los objetos sin modificar la coleccion recibida."""
    datos = [persona.to_dict() for persona in personas]
    ARCHIVO.parent.mkdir(parents=True, exist_ok=True)
    with ARCHIVO.open("w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=2, ensure_ascii=False)
    print("  [OK] Datos guardados exitosamente.")


def cargar_datos() -> list[Persona]:
    """Carga el JSON y omite de forma segura tipos de registro desconocidos."""
    if not ARCHIVO.exists():
        return []

    with ARCHIVO.open("r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    personas = map(_crear_persona, datos)
    return [persona for persona in personas if persona is not None]
