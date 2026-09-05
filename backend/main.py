from fastapi import FastAPI, HTTPException
from datos.datos_mesas import inicializar_mesas
from servicios.mesa_servicio import MesaServicio
from esquema.mesa_esquema import MesaCrear, MesaActualizar

app = FastAPI(title="sistema de gestion de Restuarantes",
              description="gestion de mesas del restaurante", version="1.0")
servicio = MesaServicio()
inicializar_mesas()


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
