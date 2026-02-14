#Project Data Visualization
#Query the database for Data visualization
#Query database  pizzaz
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
------------------------------------------------------------------------------------------

#Query Database RFM
WITH raw_data as (
    SELECT
        c.customer_unique_,
        o.order_id,
        o.order_purchase_t,
        oi.price
    FROM olist_orders_dataset o
    JOIN olist_customers_dataset c on o.customer_id = c.customer_id
    JOIN olist_order_items_dataset oi on o.order_id = oi.order_id
    WHERE o.order_status = 'delivered'
),

rfm_table AS (
    SELECT
        customer_unique_,
        CAST(julianday((SELECT MAX(order_purchase_t) FROM raw_data)) - julianday(MAX(order_purchase_t)) as INT) AS recency,
        COUNT(DISTINCT order_id) AS frequency,
        SUM(price) AS monetary
    FROM raw_data
    GROUP by customer_unique_
),


rfm_scores AS(
SELECT 
    NTILE(5) OVER(ORDER BY recency DESC) as r_score,
    NTILE(5) OVER(ORDER BY frequency) as f_score,
    NTILE(5) OVER(ORDER BY monetary) as m_score,
    recency,
    frequency,
    monetary,
    customer_unique_
FROM rfm_table
)
SELECT 
    *,
    (r_score || f_score || m_score) as rfm_score_combine,
    CASE
        WHEN r_score >= 4 AND f_score >= 4 AND m_score>= 4 THEN 'Champions'
        WHEN r_score >= 4 AND f_score >= 2 AND m_score >= 2 THEN 'Potential Loyalists'
        WHEN r_score >= 3 AND f_score >= 3 AND m_score >= 3 THEN 'Loyal Customers'
        WHEN r_score >= 3 AND f_score <= 2 THEN 'Promising / New Customers'
        WHEN r_score <= 2 AND m_score >= 4 THEN 'Can’t Lose Them'
        WHEN r_score <= 2 AND r_score > 1 THEN 'At Risk'
        WHEN r_score = 1 THEN 'Lost Customers'
        ELSE 'Others'
    END AS customer_segment
FROM rfm_scores;
------------------------------------------------------------------------------------------

#Query Database Zomato
SELECT
    name,
    online_order,
    CAST(replace(rate, '/5', ' ') AS FLOAT) AS rating,
    votes,
    location,
    rest_type,
    cuisines,
    CAST(replace([approx_cost(fortwopeople)], ',', ' ') AS INT) AS cost_for_two,
    [listed_in(type)] AS list_type,
    [listed_in(city)] AS list_city
FROM zomato
where rating is not NULL
  AND rating NOT in ('NEW', '-')
  AND cost_for_two is NOT NULL
