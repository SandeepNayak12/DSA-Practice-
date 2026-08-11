# Write your MySQL query statement below
select e1.unique_id,e.name from employees as e left join EmployeeUNI as e1
on e.id =e1.id