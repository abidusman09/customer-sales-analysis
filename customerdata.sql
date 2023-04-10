CREATE VIEW customer_sales_data AS
SELECT 
    c.customer_id, 
    c.customer_name, 
    p.product_name, 
    s.sales_date, 
    s.sales_amount
FROM 
    customers c 
JOIN 
    sales s ON c.customer_id = s.customer_id 
JOIN 
    products p ON s.product_id = p.product_id