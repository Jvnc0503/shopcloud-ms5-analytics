from fastapi import FastAPI
from app.routes.analytics import router as analytics_router

app = FastAPI(title="MS5 Analytics")

app.include_router(analytics_router, prefix="/analytics")

@app.get("/analytics/ventas-por-categoria")
def ventas_por_categoria():
    return run_mock(VENTAS_POR_CATEGORIA)

@app.get("/analytics/top-productos")
def top_productos():
    return run_mock(TOP_PRODUCTOS)

@app.get("/analytics/usuarios-activos")
def usuarios_activos():
    return run_mock(USUARIOS_ACTIVOS)

@app.get("/analytics/ingresos-por-mes")
def ingresos_por_mes():
    return run_mock(INGRESOS_MES)
