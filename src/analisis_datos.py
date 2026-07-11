"""Limpieza, transformacion y analisis de registros con pandas y NumPy."""

from typing import Any, Iterable

import numpy as np
import pandas as pd

from src.funcional import aplicar_pipeline, totalizar, transformar_registros
from src.personas import Persona


COLUMNAS = [
    "tipo",
    "nombre",
    "direccion",
    "telefono",
    "email",
    "codigo_cliente",
    "descuento",
    "codigo_empleado",
    "salario",
    "puesto",
    "puntos_vip",
]
COLUMNAS_TEXTO = [
    "tipo",
    "nombre",
    "direccion",
    "telefono",
    "email",
    "codigo_cliente",
    "codigo_empleado",
    "puesto",
]
COLUMNAS_NUMERICAS = ["descuento", "salario", "puntos_vip"]


def personas_a_registros(personas: Iterable[Persona]) -> list[dict[str, Any]]:
    """Adapta objetos del dominio a datos usando una transformacion funcional."""
    return list(map(lambda persona: persona.to_dict(), personas))


def limpiar_dataframe(registros: list[dict[str, Any]]) -> pd.DataFrame:
    """Limpia nulos, tipos, duplicados y valores numericos fuera de rango."""
    dataframe = pd.DataFrame(registros).reindex(columns=COLUMNAS)
    if dataframe.empty:
        return dataframe

    for columna in COLUMNAS_TEXTO:
        dataframe[columna] = (
            dataframe[columna].astype("string").str.strip().replace("", pd.NA)
        )

    for columna in COLUMNAS_NUMERICAS:
        dataframe[columna] = pd.to_numeric(
            dataframe[columna], errors="coerce"
        ).fillna(0)

    # NumPy realiza transformaciones vectorizadas, sin ciclos por registro.
    dataframe["descuento"] = np.clip(dataframe["descuento"], 0, 100)
    dataframe["salario"] = np.maximum(dataframe["salario"], 0)
    dataframe["puntos_vip"] = np.maximum(dataframe["puntos_vip"], 0)
    dataframe["nomina_anual"] = np.where(
        dataframe["salario"] > 0, dataframe["salario"] * 12, 0
    )
    dataframe["nivel_descuento"] = np.select(
        [dataframe["descuento"] >= 20, dataframe["descuento"] > 0],
        ["Alto", "Regular"],
        default="Sin descuento",
    )

    return dataframe.drop_duplicates(
        subset=["tipo", "codigo_cliente", "codigo_empleado", "email"],
        keep="last",
    ).reset_index(drop=True)


def preparar_dataframe(personas: Iterable[Persona]) -> pd.DataFrame:
    """Integra POO, funciones puras y pandas en un unico pipeline de datos."""
    return aplicar_pipeline(
        personas,
        personas_a_registros,
        transformar_registros,
        limpiar_dataframe,
    )


def calcular_resumen(dataframe: pd.DataFrame) -> dict[str, Any]:
    """Calcula indicadores relevantes mediante pandas, NumPy y reduce."""
    if dataframe.empty:
        return {}

    salarios = dataframe.loc[dataframe["salario"] > 0, "salario"].to_numpy()
    descuentos = dataframe.loc[
        dataframe["descuento"] > 0, "descuento"
    ].to_numpy()

    return {
        "total_registros": int(dataframe.shape[0]),
        "por_tipo": dataframe["tipo"].value_counts().to_dict(),
        "salario_promedio": float(np.mean(salarios)) if salarios.size else 0.0,
        "salario_maximo": float(np.max(salarios)) if salarios.size else 0.0,
        "salario_minimo": float(np.min(salarios)) if salarios.size else 0.0,
        "nomina_mensual": totalizar(salarios),
        "nomina_anual": float(dataframe["nomina_anual"].sum()),
        "descuento_promedio": (
            float(np.mean(descuentos)) if descuentos.size else 0.0
        ),
        "contactos_completos": int(
            dataframe[["telefono", "email"]].notna().all(axis=1).sum()
        ),
    }


def mostrar_estadisticas(personas: Iterable[Persona]) -> None:
    """Presenta el resultado del proceso de limpieza y analisis."""
    dataframe = preparar_dataframe(personas)
    resumen = calcular_resumen(dataframe)

    print("\n--- ANALISIS DE DATOS (PANDAS + NUMPY) ---")
    if not resumen:
        print("  [!] No hay datos para analizar.")
        return

    print(f"  Registros limpios y unicos: {resumen['total_registros']}")
    print("  Distribucion por tipo:")
    for tipo, cantidad in resumen["por_tipo"].items():
        print(f"    - {tipo:<12}: {cantidad}")

    print("-" * 45)
    print(f"  Salario promedio:       S/ {resumen['salario_promedio']:.2f}")
    print(f"  Salario minimo/maximo:  S/ {resumen['salario_minimo']:.2f} / "
          f"S/ {resumen['salario_maximo']:.2f}")
    print(f"  Nomina mensual:         S/ {resumen['nomina_mensual']:.2f}")
    print(f"  Proyeccion anual:       S/ {resumen['nomina_anual']:.2f}")
    print(f"  Descuento promedio:     {resumen['descuento_promedio']:.2f}%")
    print(f"  Contactos completos:    {resumen['contactos_completos']}")

    columnas_vista = [
        "tipo", "nombre", "salario", "descuento", "nivel_descuento"
    ]
    print("\n  Vista de datos transformados:")
    print(dataframe[columnas_vista].fillna("-").to_string(index=False))
