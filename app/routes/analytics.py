from fastapi import APIRouter
from app.athena_service import run_query
from app.queries import *

router = APIRouter()

@router.get("/ventas-por-categoria")
def ventas_categoria():
    return run_query(query_ventas_categoria)

@router.get("/top-productos")
def top_productos():
    return run_query(query_top_productos)

@router.get("/usuarios-activos")
def usuarios_activos():
    return run_query(query_usuarios_activos)

@router.get("/ingresos-por-mes")
def ingresos_mes():
    return run_query(query_ingresos_mes)
