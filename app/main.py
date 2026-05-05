from fastapi import FastAPI
from athena_service import run_query

app = FastAPI()


@app.get("/analytics/ventas-por-categoria")
def ventas_por_categoria():
    sql = """
    SELECT c.nombre AS categoria,
           SUM(dp.cantidad * dp.precio_unitario) AS ingresos
    FROM detalle_pedidos dp
    JOIN productos p ON dp.producto_id = p.id
    JOIN categorias c ON p.categoria_id = c.id
    GROUP BY c.nombre
    ORDER BY ingresos DESC;
    """
    return run_query(sql)


@app.get("/analytics/top-productos")
def top_productos():
    sql = """
    SELECT p.nombre,
           SUM(dp.cantidad) AS unidades_vendidas
    FROM detalle_pedidos dp
    JOIN productos p ON dp.producto_id = p.id
    GROUP BY p.nombre
    ORDER BY unidades_vendidas DESC
    LIMIT 10;
    """
    return run_query(sql)


@app.get("/analytics/usuarios-activos")
def usuarios_activos():
    sql = """
    SELECT u.nombre,
           COUNT(pe.id) AS pedidos_totales
    FROM usuarios u
    JOIN pedidos pe ON u.id = pe.usuario_id
    GROUP BY u.nombre
    ORDER BY pedidos_totales DESC;
    """
    return run_query(sql)


@app.get("/analytics/ingresos-por-mes")
def ingresos_por_mes():
    sql = """
    SELECT DATE_FORMAT(pe.creado_en,'%Y-%m') AS mes,
           SUM(pe.total) AS ingresos_mes
    FROM pedidos pe
    GROUP BY mes
    ORDER BY mes;
    """
    return run_query(sql)
