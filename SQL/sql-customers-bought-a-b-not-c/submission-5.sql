-- Write your query below
select distinct c.customer_id,customer_name
from customers c
inner join orders o
on c.customer_id=o.customer_id
where o.product_name like 'A'
AND c.customer_id in
(select o.customer_id
from orders o
where o.product_name like 'B')
AND c.customer_id not in 
(select o.customer_id
from orders o
where o.product_name like 'C')
order by customer_name;
