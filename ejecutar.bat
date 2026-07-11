@echo off
title Sistema de Ventas y Facturacion
echo ============================================
echo   SISTEMA DE VENTAS Y FACTURACION
echo   Iniciando...
echo ============================================
echo.

if not exist ".venv" (
    echo [1/3] Creando entorno virtual...
    python -m venv .venv
)

echo [2/3] Instalando dependencias...
call .venv\Scripts\activate.bat
pip install -r requirements.txt -q

echo [3/3] Iniciando sistema...
echo.
python main.py

echo.
echo ============================================
echo   Sistema finalizado.
echo ============================================
pause
