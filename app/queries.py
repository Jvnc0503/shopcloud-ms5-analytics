VENTAS_POR_CATEGORIA = """
SELECT 
    c.nombre AS categoria,
    COUNT(dp.id) AS total_items,
    SUM(dp.cantidad * dp.precio_unitario) AS ingresos
FROM detalle_pedidos dp
JOIN productos p ON dp.producto_id = p.id
JOIN categorias c ON p.categoria_id = c.id
GROUP BY c.nombre
ORDER BY ingresos DESC;
"""

TOP_PRODUCTOS = """
SELECT 
    p.nombre AS producto,
    SUM(dp.cantidad) AS unidades_vendidas,
    SUM(dp.cantidad * dp.precio_unitario) AS ingresos
FROM detalle_pedidos dp
JOIN productos p ON dp.producto_id = p.id
GROUP BY p.nombre
ORDER BY unidades_vendidas DESC
LIMIT 10;
"""

USUARIOS_ACTIVOS = """
SELECT 
    u.nombre,
    u.email,
    COUNT(pe.id) AS numero_pedidos,
    SUM(pe.total) AS gasto_total
FROM usuarios u
JOIN pedidos pe ON u.id = pe.usuario_id
GROUP BY u.id, u.nombre, u.email
ORDER BY numero_pedidos DESC;
"""

INGRESOS_MES = """
SELECT 
    DATE_FORMAT(pe.creado_en, '%Y-%m') AS mes,
    SUM(pe.total) AS ingresos
FROM pedidos pe
GROUP BY mes
ORDER BY mes;
"""
