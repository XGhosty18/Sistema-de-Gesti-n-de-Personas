# Sistema de gestión de personas

Proyecto de consola que integra programación orientada a objetos, procedural y
funcional, con persistencia JSON y análisis de datos mediante pandas y NumPy.

## Instalación y ejecución

Requiere Python 3.10 o superior.

```powershell
python -m pip install -r requirements.txt
python main.py
```

También puede ejecutarse con `uv`:

```powershell
uv venv
uv pip install --python .venv\Scripts\python.exe -r requirements.txt
.venv\Scripts\python.exe main.py
```

En el menú principal selecciona **Módulo de Consultas y Reportes** y después
**Análisis de Datos (pandas y NumPy)**.

## Organización modular

- `personas.py`: clases, herencia simple/múltiple, MRO y polimorfismo.
- `sistema.py`: validación, altas, consultas e interfaz procedural.
- `funcional.py`: funciones puras, `map`, `filter`, `reduce` y pipeline.
- `analisis_datos.py`: limpieza, transformación vectorizada y estadísticas.
- `persistencia.py`: lectura y escritura de `datos.json`.
- `main.py`: menús y orquestación de los módulos.

## Correspondencia con los criterios

1. **Paradigmas:** POO en las entidades, programación procedural en los menús y
   programación funcional en búsquedas y en el pipeline que convierte objetos
   en un `DataFrame`.
2. **Diseño y modularidad:** cada módulo tiene una responsabilidad concreta y
   las funciones de transformación pueden reutilizarse y probarse aisladamente.
3. **Tratamiento de datos:** pandas limpia nulos, tipos y duplicados; NumPy
   corrige rangos, crea campos derivados y calcula indicadores estadísticos.

El reporte calcula distribución por tipo, salarios promedio/mínimo/máximo,
nómina mensual y anual, descuento promedio y cantidad de contactos completos.
