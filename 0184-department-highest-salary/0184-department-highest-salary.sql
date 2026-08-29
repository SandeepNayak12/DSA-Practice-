# Write your MySQL query statement below
select department,employee,salary
from (select d.name as Department, e.name as Employee, e.salary,
dense_rank () over (partition by d.id order by e.salary desc) as rk
from employee e 
join department d 
on e.departmentId = d.id) t 
where rk = 1