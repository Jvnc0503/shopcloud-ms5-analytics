from fastapi import APIRouter
from app.athena_service import run_query
from app.queries import *

router = APIRouter(prefix="/analytics", tags=["analytics"])

@router.get("/ventas-por-categoria")
def ventas_categoria():
    return run_query(VENTAS_POR_CATEGORIA)

@router.get("/top-productos")
def top_productos():
    return run_query(TOP_PRODUCTOS)

@router.get("/usuarios-activos")
def usuarios_activos():
    return run_query(USUARIOS_ACTIVOS)

@router.get("/ingresos-por-mes")
def ingresos_mes():
    return run_query(INGRESOS_MES)
