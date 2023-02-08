# Write your MySQL query statement below

select Customers.name as Customers from Customers where id not in (select Customers.id from Customers join Orders where Orders.customerId=Customers.id);