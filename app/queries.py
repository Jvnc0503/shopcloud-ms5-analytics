VENTAS_POR_CATEGORIA = """
SELECT 
    c.nombre AS categoria,
    SUM(dp.cantidad) AS total_items,
    SUM(dp.subtotal) AS ingresos
FROM detalle_pedidos dp
JOIN productos p ON dp.productoid = p.id
JOIN categorias c ON p.categoria_id = c.id
GROUP BY c.nombre
ORDER BY ingresos DESC
"""

TOP_PRODUCTOS = """
SELECT 
    p.nombre AS producto,
    SUM(dp.cantidad) AS unidades_vendidas,
    SUM(dp.subtotal) AS ingresos
FROM detalle_pedidos dp
JOIN productos p ON dp.productoid = p.id
GROUP BY p.nombre
ORDER BY unidades_vendidas DESC
LIMIT 10
"""

USUARIOS_ACTIVOS = """
SELECT 
    u.nombre,
    u.apellido,
    u.email,
    COUNT(pe.id) AS numero_pedidos,
    SUM(pe.total) AS gasto_total
FROM usuarios u
JOIN pedidos pe ON u.email = pe.usuarioid
GROUP BY u.nombre, u.apellido, u.email
ORDER BY numero_pedidos DESC
LIMIT 20
"""

INGRESOS_MES = """
SELECT 
    date_format(creadoen, '%Y-%m') AS mes,
    SUM(total) AS ingresos
FROM pedidos
GROUP BY 1
ORDER BY 1
"""
