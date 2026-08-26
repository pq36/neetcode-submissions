-- Write your query below
select name from customers
where name not in
(select name from customers c
inner join orders o
on c.id=o.customer_id
group by c.id);

