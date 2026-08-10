-- JOINS

use sql_store;

select *
from order_items oi
join sql_inventory.products p
     on oi.product_id = p.product_id;


use sql_inventory;

select *
from sql_store.order_items oi 
join products p
    on oi.product_id = p.product_id;


use sql_hr;

select 
      e.employee_id,
      e.first_name,
      m.first_name as manager
from employees e
join employees m
     on e.reports_to = m.employee_id;

use sql_store;

select 
    o.order_id,
    o.order_date,
    c.first_name,
    c.last_name,
    os.name as status
from orders o
join customers c
     on o.customer_id = c.customer_id
join order_statuses os
     on o.status = os.order_status_id;

use sql_invoicing;     

select 
       p.date,
       p.invoice_id,
       p.amount,
       c.name,
       pm.name as payment_method
from payments p
join payment_methods pm
     on p.payment_method = pm.payment_method_id
join clients c
     on p.client_id = c.client_id;

use sql_store;

select *
from order_items oi
join order_item_notes oin
     on oi.order_id = oin.order_id
     and oi.product_id = oin.product_id;

select *
from orders o
join customers c
    on o.customer_id = c.customer_id;
    
 -- Implicit Join Syntax   
select *
from orders o, customers c
where o.customer_id = c.customer_id;

-- cross join
select *
from orders o, customers c;



select
      c.customer_id,
      c.first_name,
      o.order_id
from customers c
join orders o
    on o.customer_id = c.customer_id
order by c.customer_id;

-- outer joins
-- left joins

select
      c.customer_id,
      c.first_name,
      o.order_id
from customers c
left join orders o
    on o.customer_id = c.customer_id
order by c.customer_id;

-- right joins 
-- outer word is optional

select
      c.customer_id,
      c.first_name,
      o.order_id
from customers c
right join orders o
    on o.customer_id = c.customer_id
order by c.customer_id;

-- exercise

select 
     p.product_id,
     p.name,
     oi.quantity
from products p
left join order_items oi
         on p.product_id = oi. product_id
         
-- outer join between multiple tables
     
select
      c.customer_id,
      c.first_name,
      o.order_id,
      sh.name as shipper
from customers c
left join orders o
    on o.customer_id = c.customer_id
left join shippers sh
     on o.shipper_id = sh.shipper_id
order by c.customer_id;

-- exercise

select
       o.order_id,
       o.order_date,
       c.first_name as customer,
      sh.name as shipper,
      os.name as status
from orders o
join customers c
    on o.customer_id = c.customer_id
left join shippers sh
     on o.shipper_id = sh.shipper_id
     join order_statuses os
     on o.status = os.order_status_id
     order by os.name, o.order_id;

-- self joins

use sql_hr;

select 
       e.employee_id,
       e.first_name,
       m.first_name as manager
from employees e
left join employees m
    on e. reports_to = m.employee_id;
     
-- using clause

use sql_store;

select 
      o.order_id,
      c.first_name,
      sh.name as shipper
from orders o
join customers c
      using (customer_id)
left join shippers sh
     using (shipper_id);

select *
from order_items oi
join order_item_notes oin
     using (order_id, product_id);
     
-- exercise
   
use sql_invoicing;

select 
      p.date,
      p.amount,
      c.name,
      pm.name as status
from payments p
join clients c
     using (client_id)
join payment_methods pm
     on p.payment_method = pm.payment_method_id;
         

-- natural joins

use sql_store;

select 
      o.order_id,
      c.first_name
from orders o 
natural join customers c;

-- cross joins

select 
       c.first_name as customer,
       p.name as product
from customers c
cross join products p
order by c.first_name;

-- exercise

select 
      p.product_id,
      p.name,
      sh.name as shipper,
from products p
cross join shippers sh
order by p.product_id;

select 
      p.product_id,
      p.name,
      sh.name as shipper,
from products p, shippers sh
order by p.product_id;

-- unions


select 
      order_id,
      order_date,
       'active' as status
from orders
where order_date >= '2019-01-01'
union
select 
      order_id,
      order_date,
       'Archived' as status
from orders
where order_date < '2019-01-01';


select first_name
from customers
union
select name 
from shippers;

-- exercise

select 
      customer_id,
      first_name,
      points,
      'Bronze' as type
from customers
where points < '2000'
union 
select 
      customer_id,
      first_name,
      points,
      'Silver' as type
from customers
where points  between 2000 and 3000
union 
select 
      customer_id,
      first_name,
      points,
      'Gold' as type
from customers
where points >= '3000'
order by first_name;


-- inserting a single row

insert into customers (
    first_name,
    last_name,
    birth_date,
    address,
    city,
    state)
values (
'John',
'Smith',
'1990-01-01',
'address',
'city',
'CA'
);

-- inserting multiple rows

insert into shippers (name)
values ('shippers1'),
       ('shippers2'),
       ('shippers3');

-- exercise

insert into products (
         name,
         quantity_in_stock,
         unit_price
)
values ('name1', '2','7.8'),
       ('name2','5','7'),
       ('name3','9','10');

-- inserting hierarchical rows

insert into orders (
           customer_id, order_date, status)
values ( 1, '2019-01-02', 1);

insert into order_items
values 
     (last_insert_id(), 1, 1, 2.95),
     (last_insert_id(), 2, 1, 3.95);


-- creating a copy of a table

create table orders_archived as
select * from orders

select *
from orders_archived

use sql_store;

insert into orders_archived
select *
from orders
where order_date < '2019-01-01'

-- exercise

use sql_invoicing;

create table invoice_archived as
select 
      i.invoice_id, 
      i.number,
      c.name,
      i.invoice_total,
      i.payment_total,
      i.invoice_date,
      i.due_date,
      i.payment_date
from invoices i
join clients c
    using (client_id)
where payment_date is not null

-- updating data in a single row

update invoices
set payment_total = default, payment_date = null
where invoice_id = 1;

update invoices
set
    payment_total = invoice_total * 0.5, 
    payment_date = due_date
where invoice_id = 3;

-- updating multiple rows

update invoices
set
    payment_total = invoice_total * 0.5, 
    payment_date = due_date
where client_id in (3, 4);


-- exercise

use sql_store;

update customers
set points = points + 50
where birth_date <= '1990-01-01';

-- using subqueries in updates

use sql_invoicing;

update invoices
set
    payment_total = invoice_total * 0.5, 
    payment_date = due_date
where invoice_id IN
     (select client_id
      from clients
       where state in ('CA', 'NY'));
       
update invoices
set
    payment_total = invoice_total * 0.5, 
    payment_date = due_date
where payment_date is null;
     
-- exercise

use sql_store;

update orders
set 
   comments = 'GOLD CUSTOMER'
where  customer_id in 
     (select customer_id
      from customers
      where points >= 3000);

-- DELETING ROWS

use sql_invoicing;

delete from invoices
where client_id =
     (select *
      from clients
      where name = 'Myworks')

      


      
      