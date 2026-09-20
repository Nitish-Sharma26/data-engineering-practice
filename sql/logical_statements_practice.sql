-- where clause

use parks_and_recreation;

select * 
from employee_salary
where first_name = 'Leslie';

select * 
from employee_salary
where salary >= 50000;

select * 
from employee_salary
where salary <= 50000;

select *
from employee_demographics
where gender != 'female';

select *
from employee_demographics
where birth_date > '1985-01-01';

-- AND OR NOT -- LOGICAL OPERATORS

select *
from employee_demographics
where birth_date > '1985-01-01'
and GENDER ='male';

select *
from employee_demographics
where birth_date > '1985-01-01'
or not GENDER ='male';

select *
from employee_demographics
where (first_name = 'Leslie'
      and age = 44) or age > 55;

-- LIKE STATEMENT

select *
from employee_demographics
where first_name like 'jer%';

select *
from employee_demographics
where first_name like '%er%';

select *
from employee_demographics
where first_name like 'a__';

select *
from employee_demographics
where first_name like 'a___';

select *
from employee_demographics
where first_name like 'a__%';

select *
from employee_demographics
where birth_date 
like '1988%';

-- group by

select gender
from employee_demographics
group by gender;

select gender, avg(age)
from employee_demographics
group by gender;

select occupation, salary 
from employee_salary
group by occupation, salary;

select gender, avg(age), max(age), min(age), count(age)
from employee_demographics
group by gender;

-- order by

select *
from employee_demographics
order by first_name desc;

select *
from employee_demographics
order by gender, age;


-- having vs where

select gender, avg(age)
from employee_demographics
group by gender
having avg(age);

select occupation, avg(salary)
from employee_salary
where occupation like '%manager%'
group by occupation
having avg(salary) > 75000;

-- limit and aliasing 

select *
from employee_demographics
order by age desc
limit 2, 1;

-- aliasing

select gender, avg(age) as avg_age  
from employee_demographics
group by gender
having avg(age) > 40;

-- joins

select *
from employee_demographics;

select *
from employee_salary;


select 
      ed.employee_id,
      age,
      occupation
from employee_demographics ed
inner join employee_salary es
          on ed.employee_id = es.employee_id;

-- outer join

select 
      ed.employee_id,
      age,
      occupation
from employee_demographics ed
left join employee_salary es
          on ed.employee_id = es.employee_id;

select 
      ed.employee_id,
      age,
      occupation
from employee_demographics ed
right join employee_salary es
          on ed.employee_id = es.employee_id;

-- self join

select es1.employee_id as emp_santa,
        es1.first_name as first_name_santa,
        es1.last_name as last_name_santa,
         es1.employee_id as emp_santa,
        es2.first_name as first_name_santa,
        es2.last_name as last_name_santa
from employee_salary es1
join employee_salary es2
    on es1.employee_id + 1 = es2.employee_id;

-- joining multiple tables together

select *
from employee_demographics as dem
inner join employee_salary as sal
     on dem.employee_id = sal.employee_id
inner join parks_departments pd 
     on sal.dept_id = pd.department_id;

-- reference for above content
     
select *
from parks_departments;

-- unions

select first_name, last_name
from employee_demographics
union  
select first_name, last_name
from employee_salary;

select first_name, last_name, 'Old Man' as label
from employee_demographics
where age > 40 and gender = 'Male'
union
select first_name, last_name, 'Old Lady' as label
from employee_demographics
where age > 40 and gender = 'Female'
union
select first_name, last_name, 'Highest Paid Employee' as label
from employee_salary
where salary > 70000
order by first_name , last_name;

-- string functions
 
select length('skyfall')

select first_name, length(first_name)
from employee_demographics
order by 2;

select upper('sky');

select lower('sky');

select first_name, upper(first_name)
from employee_demographics;

select rtrim('       sky      ');

select first_name, 
left(first_name, 4),
right(first_name, 4),
substring(first_name,3,2),
birth_date,
substring(birth_date,6,2) as birth_month
from employee_demographics;

select first_name, replace(first_name, 'a', 'z')
from employee_demographics;

select locate('x', 'Alexander');


select first_name, locate('An', first_name)
from employee_demographics;

select first_name, last_name,
concat(first_name, ' ', last_name) as full_name
from employee_demographics;

-- case statement

select 
     first_name,
     last_name,
     age,
case
    when age <= 30 then 'young'
    when age between 31 and 50 then 'Old'
    when age >= 60 then ' on door'
    end as Age_bracket
from employee_demographics;

-- pay increase or bonus
-- <50000 = 5%
-- >50000 = 7%
-- finance = 10% bonus


select first_name, last_name, salary,
 case   
 	 when salary < 50000 then salary + (salary * 0.05)
 	 when salary > 50000 then salary + (salary * 0.07)
 end as new_salary,
 case 
 	when dept_id = 6 then salary * .10
 end as bonus
 from employee_salary;



 -- subqueries
  
 select *
 from employee_demographics
 where employee_id in 
  (select employee_id
   from employee_salary
   where dept_id = 1
 );

 
 select first_name, salary,
 (select avg(salary)
 from employee_salary)
from employee_salary
;


select gender, avg(age), max(age), min(age), count(age)
from employee_demographics
group by gender;


 select  
      avg(max_age)
from 
   (select
         gender,
         avg(age) as avg_age,
         max(age) max_age,
         min(age) min_age,
         count(age) count_age
from employee_demographics
group by gender)
        as Agg_table
;


-- window functions


select 
      dem.first_name,
      dem.last_name,
      gender,
      salary,
      sum(salary)
       over(partition by gender order by dem.employee_id) as rolling_total
from employee_demographics dem
join employee_salary sal 
on dem.employee_id = sal.employee_id;


select 
      dem.employee_id,
      dem.first_name,
      dem.last_name,
      gender,
      salary,
      row_number() over(partition by gender order by salary desc) as row_num,
          rank() over(partition by gender order by salary desc) as rank_num,
          dense_rank() over(partition by gender order by salary desc) as dense_rank_num
from employee_demographics dem
join employee_salary sal 
on dem.employee_id = sal.employee_id;

commit;

-- CTEs


with CTE_Example as 
(
select 
      gender,
      avg(salary) avg_sal,
      max(salary)max_sal,
      min(salary)min_sal,
      count(salary)count_sal
from employee_demographics dem 
join employee_salary sal 
   on dem.employee_id = sal.employee_id
group by gender
)
select *
from CTE_Example 
;   

with CTE_Example as 
(
select 
      gender,
      avg(salary) avg_sal,
      max(salary)max_sal,
      min(salary)min_sal,
      count(salary)count_sal
from employee_demographics dem 
join employee_salary sal 
   on dem.employee_id = sal.employee_id
group by gender
)
select avg(avg_sal)
from CTE_Example 
;   

-- without CTE


select avg_sal
from 
(
select 
      gender,
      avg(salary) avg_sal,
      max(salary)max_sal,
      min(salary)min_sal,
      count(salary)count_sal
from employee_demographics dem 
join employee_salary sal 
   on dem.employee_id = sal.employee_id
group by gender
)
example_subquery
;   


-- It is not permanent. The table made in CTE is limited to query.


with CTE_Example as 
(
select
      employee_id,
      gender,
      birth_date
from employee_demographics dem 
where birth_date > '1985-01-01'
),
CTE_Example2 as 
( 
select employee_id, salary
from employee_salary
where salary >50000 
)
select *
from CTE_Example
join CTE_Example2  
    on CTE_Example.employee_id = CTE_Example2.employee_id
;   


-- temporary tables

create temporary table temp_table
( 
  first_name varchar (50),
  last_name varchar (50),
  favourite_movie varchar(100)
  );

select *
from temp_table;

insert into temp_table
values 
     ( 'Alex',
       'freberg',
       'Lord of the Rings: The Two Towers'
     );


select *
from temp_table;


-- Another way to use Temp Table

select *
from employee_salary;

create temporary table salary_over_50k
select *
from employee_salary
where salary >= 50000;

-- Stored Procedures

select *
from employee_salary
where salary >= 50000
;


delimiter $$
create procedure large_salaries2()
begin 
	 
select *
from employee_salary
where salary >= 50000
;
select *
from employee_salary
where salary >= 10000
;
end $$ 
delimiter ;


call large_salaries2();



delimiter $$
create procedure large_salaries4(huggymuffin int)
begin  
    select *
    from employee_salary
    where employee_id = huggymuffin
    ;
end $$ 
delimiter ;

call large_salaries4(1);

-- Triggers and events

select *
from employee_salary;

select *
from employee_demographics;

delimiter $$
create trigger employee_insert
     after insert on employee_salary
     for each row
begin
	insert into employee_demographics
	          (employee_id, 
	          first_name, 
	          last_name)
	values (
	         new.employee_id,
	         new.first_name,
	         new.last_name);          
	end $$
	delimiter ;

insert into employee_salary
           ( employee_id, 
             first_name,
             last_name,
             occupation,
             salary,
             dept_id)
values 
      ( '14', 'Jean-Raphlo', 'Saperstien', 'Entertainment', '1000000', null);


-- Events

select *
from employee_demographics;

 delimiter $$
 create event delete_retirees
on schedule every 30 second
do
begin 
	delete
    from employee_demographics
    where age >= 60;
	end $$
delimiter ;


show variables like 'event%';

commit; 


