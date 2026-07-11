# HERENCIA SIMPLE, HERENCIA MULTIPLE Y POLIMORFISMO (TYPE HINTING)

from typing import Any


class Persona:
    """Clase base: representa a una persona generica."""

    def __init__(self, nombre: str, direccion: str, telefono: str, email: str,
                 **kwargs: Any):
        # Inicialización cooperativa: cierra correctamente la cadena del MRO.
        super().__init__(**kwargs)
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

    def mostrar_info(self) -> str:
        """Metodo polimorfico: sera sobrescrito por las subclases."""
        return (
            f"PERSONA\n"
            f"  Nombre:      {self.nombre}\n"
            f"  Direccion:   {self.direccion}\n"
            f"  Telefono:    {self.telefono}\n"
            f"  Email:       {self.email}"
        )

    def to_dict(self) -> dict:
        return {
            "tipo": "Persona",
            "nombre": self.nombre,
            "direccion": self.direccion,
            "telefono": self.telefono,
            "email": self.email,
        }


class Cliente(Persona):
    """Herencia simple: Cliente hereda de Persona."""

    def __init__(self, nombre: str, direccion: str, telefono: str, email: str,
                 codigo_cliente: str, descuento: int, **kwargs: Any):
        super().__init__(
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            email=email,
            **kwargs,
        )
        self.codigo_cliente = codigo_cliente
        self.descuento = descuento

    def mostrar_info(self) -> str:
        """Polimorfismo: misma firma, comportamiento distinto."""
        return (
            f"CLIENTE (cod: {self.codigo_cliente})\n"
            f"  Nombre:      {self.nombre}\n"
            f"  Descuento:   {self.descuento}%\n"
            f"  Telefono:    {self.telefono}\n"
            f"  Email:       {self.email}"
        )

    def to_dict(self) -> dict:
        d = super().to_dict()
        d["tipo"] = "Cliente"
        d["codigo_cliente"] = self.codigo_cliente
        d["descuento"] = self.descuento
        return d


class Empleado(Persona):
    """Herencia simple: Empleado hereda de Persona."""

    def __init__(self, nombre: str, direccion: str, telefono: str, email: str,
                 codigo_empleado: str, salario: float, puesto: str,
                 **kwargs: Any):
        super().__init__(
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            email=email,
            **kwargs,
        )
        self.codigo_empleado = codigo_empleado
        self.salario = salario
        self.puesto = puesto

    def mostrar_info(self) -> str:
        """Polimorfismo: misma firma, comportamiento distinto."""
        return (
            f"EMPLEADO (cod: {self.codigo_empleado})\n"
            f"  Nombre:      {self.nombre}\n"
            f"  Puesto:      {self.puesto}\n"
            f"  Salario:     S/ {self.salario:.2f}\n"
            f"  Email:       {self.email}"
        )

    def to_dict(self) -> dict:
        d = super().to_dict()
        d["tipo"] = "Empleado"
        d["codigo_empleado"] = self.codigo_empleado
        d["salario"] = self.salario
        d["puesto"] = self.puesto
        return d


class ClienteVIP(Cliente, Empleado):
    """HERENCIA MULTIPLE: hereda de Cliente Y Empleado simultaneamente."""

    def __init__(self, nombre: str, direccion: str, telefono: str, email: str,
                 codigo_cliente: str, descuento: int,
                 codigo_empleado: str, salario: float, puesto: str,
                 puntos_vip: int):
        
        # super() recorre Cliente -> Empleado -> Persona según el MRO.
        super().__init__(
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            email=email,
            codigo_cliente=codigo_cliente,
            descuento=descuento,
            codigo_empleado=codigo_empleado,
            salario=salario,
            puesto=puesto,
        )
        self.puntos_vip = puntos_vip

    def mostrar_info(self) -> str:
        """Polimorfismo: tercera version del mismo metodo."""
        return (
            f"CLIENTE VIP (cod cliente: {self.codigo_cliente}, "
            f"cod emp: {self.codigo_empleado})\n"
            f"  Nombre:      {self.nombre}\n"
            f"  Descuento:   {self.descuento}%\n"
            f"  Puesto:      {self.puesto}\n"
            f"  Salario:     S/ {self.salario:.2f}\n"
            f"  Puntos VIP:  {self.puntos_vip}\n"
            f"  Email:       {self.email}"
        )

    def to_dict(self) -> dict:
        # La serialización también sigue cooperativamente el MRO.
        d = super().to_dict()
        d["tipo"] = "ClienteVIP"
        d["puntos_vip"] = self.puntos_vip
        return d
