#Query the database for Data visualization
SELECT
    od.order_id, 
    o.date,
    o.time,
    pt.name AS pizza_name,
    pt.category,
    p.size,
    p.price,
    od.quantity,
    (p.price * od.quantity) AS total_revenue,
    pt.ingredients
FROM order_details od
JOIN orders o ON od.order_id = o.order_id
JOIN pizzas p ON od.pizza_id = p.pizza_id
JOIN pizza_types pt ON p.pizza_type_id = pt.pizza_type_id;