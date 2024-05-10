from .models import Vehiculo, Chofer, RegistroContabilidad
from datetime import date
from django.core.exceptions import ObjectDoesNotExist

def crear_vehiculo(patente, marca, modelo,año):
    """
    Crea un nuevo vehículo en la base de datos.

    Args:
        patente (str): La patente del vehículo.
        marca (str): La marca del vehículo.
        modelo (str): El modelo del vehículo.
        año (int): El año del vehículo.

    Returns:
        Vehiculo: El objeto Vehiculo recién creado.
    """
    vehiculo = Vehiculo.objects.create(patente=patente, marca=marca, modelo=modelo, año=año)
    return Vehiculo

def crear_chofer(rut, nombre, apellido, activo, creacion_registro, vehiculo_id):
    """
    Crea un nuevo chofer en la base de datos.

    Args:
        rut (str): El RUT del chofer.
        nombre (str): El nombre del chofer.
        apellido (str): El apellido del chofer.
        activo (bool): Indica si el chofer está activo o no.
        creacion_registro (date): La fecha de creación del registro.
        vehiculo_id (str): La patente del vehículo asociado al chofer.

    Returns:
        Chofer: El objeto Chofer recién creado."""
    vehiculo = Vehiculo.objects.get(patente=vehiculo_id)
    chofer= Chofer.objects.create(rut=rut, nombre=nombre, apellido=apellido, activo=activo, creacion_registro=creacion_registro, vehiculo_id=vehiculo)
    return chofer


def crear_registro_contable(fecha_compra, valor, vehiculo_id):
    """
    Crea un nuevo registro contable en la base de datos.

    Args:
        fecha_compra (date): La fecha de compra del vehículo.
        valor (float): El valor de la compra del vehículo.
        vehiculo_id (str): La patente del vehículo asociado al registro contable.

    Returns:
        RegistroContabilidad: El objeto RegistroContabilidad recién creado.
    """
    vehiculo = Vehiculo.objects.get(patente=vehiculo_id)
    registro_contable = RegistroContabilidad.objects.create(fecha_compra = fecha_compra, valor=valor, vehiculo=vehiculo)
    return registro_contable

def deshabilitar_chofer(rut):
    """ 
    Deshabilita un chofer exitente en la base de datos, si no lo encuentra pasa

    Args: 
        rut(str): El rut del chofer a deshabilitar  
     """
    try:
        chofer = Chofer.objects.get(rut=rut)
        chofer.activo = False
        chofer.save()
    except ObjectDoesNotExist:
        pass
def deshabilitar_vehiculo(patente):
    """
    Deshabilita un vehiculo existente de la base de datos

    Args: 
        patente(str): La patente del vehiculo a deshabilitar 
     """
    try:
        vehiculo = Vehiculo.objects.get(patente=patente)
        vehiculo.activo = False
        vehiculo.save()
    except ObjectDoesNotExist:
        pass
 
def habilitar_chofer(rut):
    """ 
    Habilita un chofer existente en la base de datos
    
    Args:
        rut(str): El rut del chofer a habilitar
    """
    try:
        chofer = Chofer.objects.get(rut=rut)
        chofer.activo = True
        chofer.save()
    except ObjectDoesNotExist:
        pass

def habilitar_vehiculo(patente):
    """ 
    Habilita un vehiculo existente en la base de datos

    Args: 
        patente(str): La patente del vehiculo a habilitar
    """
    try:
        vehiculo.Vehiculo.objects.get(patente=patente)
        vehiculo.activo = True
        vehiculo.save()
    except ObjectDoesNotExist:
        pass


def obtener_chofer(rut):
    """ 
    Obtiene un chofer de la base de datos

    Args:
        rut(str): El rut del chofer que queremos obtener
    
    Returns:
        chofer: objeto Chofer correspondiente al rut que proporcionamos
    """
    try:
        chofer = Chofer.objects.get(rut=rut)
        return chofer
    except ObjectDoesNotExist:
        return None

def obtener_vehiculo(patente):
    """
    Obtiene un vehiculo de la base de datos

    Args:
        patente: La patente del vehiculo que queremos obtener

    Returns: 
        vehiculo: objeto Vehiculo correspondiente a la patente que proporcionamos 
     """
    try:
        vehiculo = Vehiculo.objects.get(patente=patente)
        return vehiculo
    except ObjectDoesNotExist:
        return None


def asignar_chofer_a_vehiculo(rut, patente):
    """ 
    Asigna un chofer a un vehiculo existente en la base de datos

    Args:
        rut(str): El rut del chofer
        patente(str): La patente del vehiculo
    """
    try:
        chofer = Chofer.objects.get(rut=rut)
        vehiculo = Vehiculo.objects.get(patente=patente)
        chofer.vehiculo_id = vehiculo
        chofer.save()
    except ObjectDoesNotExist:
        pass

def imprimir_datos_vehiculo(patente):
    """
    Imprime los datos de un vehiculo existente en la base de datos

    Args:
        patente(str): La patente del vehiculo
     """
    try:
        vehiculo = Vehiculo.objects.get(patente=patente)
        print(f"Patente: {vehiculo.patente}")
        print(f"Marca: {vehiculo.marca}")
        print(f"Modelo: {vehiculo.modelo}")
        print(f"Año: {vehiculo.año}")
    except ObjectDoesNotExist:
        print("El vehiculo no existe en la base de datos")


