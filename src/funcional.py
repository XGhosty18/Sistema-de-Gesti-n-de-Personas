"""[PARADIGMA FUNCIONAL] Utilidades funcionales puras del sistema.

Este modulo concentra transformaciones sin entrada/salida ni estado global.
Integra programacion funcional con la capa orientada a objetos.
Uso de map, filter, reduce y funciones puras.
"""

from functools import reduce
from typing import Any, Callable, Iterable, TypeVar


T = TypeVar("T")


# [FUNCIONES PURAS] Funciones sin efectos colaterales
def aplicar_pipeline(valor: T, *funciones: Callable[[Any], Any]) -> Any:
    """Aplica funciones de izquierda a derecha sin modificar el valor original."""
    return reduce(lambda acumulado, funcion: funcion(acumulado), funciones, valor)


def limpiar_registro(registro: dict[str, Any]) -> dict[str, Any]:
    """Devuelve una copia del registro con sus textos sin espacios sobrantes."""
    return {
        clave: valor.strip() if isinstance(valor, str) else valor
        for clave, valor in registro.items()
    }


# [MAP] Transformacion funcional de registros
def transformar_registros(
    registros: Iterable[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Transforma registros mediante ``map`` y conserva inmutables los originales."""
    return list(map(limpiar_registro, registros))


# [FILTER] Filtrado funcional de personas por nombre
def filtrar_por_nombre(personas: Iterable[T], consulta: str) -> list[T]:
    """Selecciona personas por nombre mediante ``filter`` y un predicado."""
    texto = consulta.strip().casefold()
    coincide = lambda persona: texto in persona.nombre.casefold()
    return list(filter(coincide, personas))


# [REDUCE] Suma funcional de valores numericos
def totalizar(valores: Iterable[float]) -> float:
    """Suma una secuencia numérica mediante una reducción funcional."""
    return reduce(lambda total, valor: total + float(valor), valores, 0.0)
