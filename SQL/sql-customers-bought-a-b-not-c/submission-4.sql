-- Write your query below
select distinct c.customer_id,customer_name
from customers c
inner join orders o
on c.customer_id=o.customer_id
where o.product_name like 'A'
group by c.customer_id

intersect
(select distinct c.customer_id,customer_name
from customers c
inner join orders o
on c.customer_id=o.customer_id
where o.product_name like 'B'
group by c.customer_id)
except
(select distinct c.customer_id,customer_name
from customers c
inner join orders o
on c.customer_id=o.customer_id
where o.product_name like 'C'
group by c.customer_id)
order by customer_name;
