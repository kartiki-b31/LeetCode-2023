# Write your MySQL query statement below

select customer_id,count(visits.visit_id) as count_no_trans 
from Visits natural left join Transactions
where Transactions.visit_id is NULL
group by customer_id
order by count_no_trans DESC;


