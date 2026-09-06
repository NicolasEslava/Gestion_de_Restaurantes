from fastapi import FastAPI, HTTPException
from datos.datos_mesas import inicializar_mesas
from servicios.mesa_servicio import MesaServicio
from esquema.mesa_esquema import MesaCrear, MesaActualizar
from servicios.platos_servicios import Platoservicio
from esquema.plato_esquema import (PlatoCrear, PlatoActualizar)
from datos.datos_platos import inicializar_platos
from servicios.pedido_servicio import (
    crear_pedido, agregar_detalle, modificar_detalle, eliminar_detalle, obtener_pedido, calcular_pedido)
from esquema.pedido_esquema import (
    PedidoCrear, PedidoRespuesta, DetallePedidoCrear, DetallePedidoModificar)

app = FastAPI(title="sistema de gestion de Restuarantes",
              description="gestion de mesas del restaurante", version="1.0")
servicio = MesaServicio()
plato_servicio = Platoservicio()
inicializar_mesas()
inicializar_platos()


@app.get("/")
def inicio():
    return {"mensaje": "sistema de gestion de restaurantes",
            "modulo": "mesas",
            "estado": "activo"
            }


@app.get("/mesas")
def listar_mesas():
    mesas = servicio.listar_mesas()

    return [
        {
            "id_mesa": mesa.id_mesa,
            "numero": mesa.numero,
            "estado": mesa.estado
        }
        for mesa in mesas
    ]


@app.get("/mesas/{numero}")
def buscar_mesas(numero: int):
    mesa = servicio.buscar_mesa(numero)

    if mesa is None:
        return {
            "mensaje": "mesa no encontrada"
        }

    return {
        "id_mesa": mesa.id_mesa,
        "numero": mesa.numero,
        "estado": mesa.estado
    }


@app.post("/mesas")
def crear_mesa(datos: MesaCrear):

    mesa = servicio.crear_mesa(datos.numero)
    if mesa is None:
        raise HTTPException(
            status_code=409, detail="ya existe una measa con el mismo numero ")

    return {
        "mensaje": "mesa creada correctamente",
        "id_mesa": mesa.id_mesa,
        "numero": mesa.numero,
        "estado": mesa.estado
    }


@app.put("/mesas/{numero}")
def actualizar_mesa(numero: int, datos: MesaActualizar):
    mesa = servicio.actualizar_mesa(numero, datos.nuevo_numero)
    if mesa is None:
        raise HTTPException(
            status_code=404,
            detail="no se puede actualizar la mesa"
        )
    return {
        "mensaje": "mesa actualizada correctamente",
        "id:mesa": mesa.id_mesa,
        "numero": mesa.numero,
        "estado": mesa.estado

    }


@app.delete("/mesas/{numero}")
def eliminar_mesa(numero: int):
    mesa = servicio.eliminar_mesa(numero)

    if mesa is None:
        raise HTTPException(
            status_code=404, detail="no se puedo eliminar la mesa")

    return {
        "mensaje": "mesa eliminada correctamente",
        "id_mesa": mesa.id_mesa,
        "numero": mesa.numero
    }


@app.put("/mesas/{numero}/ocupar")
def ocupar_mesa(numero: int):

    mesa = servicio.ocupar_mesa(numero)

    if mesa is None:
        raise HTTPException(
            status_code=404,
            detail="No se pudo ocupar la mesa"
        )
    return {
        "mensaje": "mesa ocupada correctamente",
        "id_mesa": mesa.id_mesa,
        "numero": mesa.numero,
        "estado": mesa.estado
    }


@app.put("/mesas/{numero}/liberar")
def liberar_mesa(numero: int):
    mesa = servicio.liberar_mesa(numero)
    if mesa is None:
        raise HTTPException(
            status_code=404,
            detail="no se pudo liberar la mesa"
        )
    return {
        "mensaje": "mesa liberada correctamente",
        "id_mesa": mesa.id_mesa,
        "numero": mesa.numero,
        "estado": mesa.estado
    }


@app.get("/platos")
def listar_platos():

    platos = plato_servicio.listar_platos()

    return [
        {
            "id_plato": plato.id_plato,
            "nombre": plato.nombre,
            "precio": plato.precio,
            "categoria": plato.categoria,
            "disponible": plato.disponible
        }
        for plato in platos
    ]


@app.get("/platos/{id_plato}")
def buscar_plato(id_plato: int):

    plato = plato_servicio.buscar_plato(id_plato)

    if plato is None:

        raise HTTPException(
            status_code=404,
            detail="Plato no encontrado"
        )

    return {
        "id_plato": plato.id_plato,
        "nombre": plato.nombre,
        "precio": plato.precio,
        "categoria": plato.categoria,
        "disponible": plato.disponible
    }


@app.post("/platos")
def crear_plato(datos: PlatoCrear):

    plato = plato_servicio.crear_plato(
        datos.nombre,
        datos.precio,
        datos.categoria
    )

    return {
        "mensaje": "Plato creado correctamente",
        "id_plato": plato.id_plato,
        "nombre": plato.nombre,
        "precio": plato.precio,
        "categoria": plato.categoria,
        "disponible": plato.disponible
    }


@app.put("/platos/{id_plato}")
def actualizar_plato(
    id_plato: int,
    datos: PlatoActualizar
):

    plato = plato_servicio.actualizar_plato(
        id_plato,
        datos.nombre,
        datos.precio,
        datos.categoria,
        datos.disponible
    )

    if plato is None:

        raise HTTPException(
            status_code=404,
            detail="Plato no encontrado"
        )

    return {
        "mensaje": "Plato actualizado correctamente",
        "id_plato": plato.id_plato,
        "nombre": plato.nombre,
        "precio": plato.precio,
        "categoria": plato.categoria,
        "disponible": plato.disponible
    }


@app.delete("/platos/{id_plato}")
def eliminar_plato(id_plato: int):

    plato = plato_servicio.eliminar_plato(id_plato)

    if plato is None:

        raise HTTPException(
            status_code=404,
            detail="Plato no encontrado"
        )

    return {
        "mensaje": "Plato eliminado correctamente",
        "id_plato": plato.id_plato,
        "nombre": plato.nombre
    }


@app.post("/pedidos")
def crear_pedido_endpoint(datos: PedidoCrear):

    return crear_pedido(
        datos.id_mesa
    )


@app.post("/pedidos/{id_pedido}/detalles")
def agregar_detalle_endpoint(
    id_pedido: int,
    datos: DetallePedidoCrear
):

    return agregar_detalle(
        id_pedido=id_pedido,
        id_plato=datos.id_plato,
        cantidad=datos.cantidad,
        observacion=datos.observacion
    )


@app.get("/pedidos/{id_pedido}")
def obtener_pedido_endpoint(
    id_pedido: int
):

    return calcular_pedido(
        id_pedido
    )


@app.delete(
    "/pedidos/{id_pedido}/detalles/{id_detalle}"
)
def eliminar_detalle_endpoint(
    id_pedido: int,
    id_detalle: int
):

    return eliminar_detalle(
        id_pedido,
        id_detalle
    )


@app.put(
    "/pedidos/{id_pedido}/detalles/{id_detalle}"
)
def modificar_detalle_endpoint(
    id_pedido: int,
    id_detalle: int,
    datos: DetallePedidoModificar
):

    return modificar_detalle(
        id_pedido=id_pedido,
        id_detalle=id_detalle,
        cantidad=datos.cantidad,
        observacion=datos.observacion
    )
