-- Solving Questions  (Only answers appearing here)

 use solving_interview_questions;
 
 
 create table icc_world_cup
 ( 
 team_1 varchar(20), 
 team_2 varchar(20),
 winner varchar(20)
 );
 
 insert into icc_world_cup values ('INDIA', 'SL', 'INDIA');
  insert into icc_world_cup values ('SL', 'AUS', 'AUS'); 
   insert into icc_world_cup values ('SA', 'ENG', 'ENG'); 
    insert into icc_world_cup values ('ENG', 'NZ', 'NZ'); 
     insert into icc_world_cup values ('AUS', 'INDIA', 'INDIA');
 
 
 SELECT *
 FROM icc_world_cup;  
 

 select team_name, count(1) as no_of_matches_played,
 sum(win_flag) as no_of_matches_won, 
 count(1) - sum(win_flag) as no_of_losses
 from ( 
 select team_1 as team_name,
               case
	               when team_1 = winner
	                  then 1
	                  else 0 
	                  end as win_flag
 from icc_world_cup 
 union all
  select team_2 as team_name,
                case 
	                when team_2 = winner 
                      then 1
                      else 0
                      end as win_flag
 from icc_world_cup) a
 group by team_name
  order by no_of_matches_won desc;
 
 
 ----------------------------------------------------------------------------------------------------------------------------------
 
 
 -- 2nd 
 
 create table customer_orders
 ( 
 order_id integer,
 customer_id integer,
 order_date date,
 order_amount integer
 );
 
 select *
 from customer_orders
 
 insert into customer_orders
 values(1,100, cast('2022-01-01'as date),2000),
        (2,200, cast('2022-01-01'as date),2500),
        (3,300, cast('2022-01-01'as date),2100),
        (4,100, cast('2022-01-02'as date),2000),
        (5,400, cast('2022-01-02'as date),2200),
        (6,500, cast('2022-01-02'as date),2700),
        (7,100, cast('2022-01-03'as date),3000),
        (8,400, cast('2022-01-03'as date),1000),
        (9,600, cast('2022-01-03'as date),3000)
        ;
 
 
 with first_visit as ( 
 select 
      customer_id,
      min(order_date) as first_visit_date
 from customer_orders
 group by customer_id
), 
visit_flag as (
select 
      co.*,
      fv.first_visit_date,
         case 
	         when co.order_date = fv.first_visit_date 
	               then 1 
	               else 0 
	               end as first_visit_flag, 
         case 
	         when co.order_date != fv.first_visit_date 
	               then 1 
	               else 0 
	               end as repeat_visit_flag
         from customer_orders co
         inner join first_visit fv 
                   on co.customer_id = fv.customer_id
         order by order_id
  ) 
  select
         order_date,
         sum(first_visit_flag) as no_of_new_customers,
         sum(repeat_visit_flag) as no_of_repeat_customers
  from visit_flag
  group by order_date
;


---------------------------------------------------------------------------------------------------------

-- order amount by new customers and repeat customers

 with first_visit as ( 
 select 
      customer_id,
      min(order_date) as first_visit_date
 from customer_orders
 group by customer_id
)
select co.customer_id,
         sum(case 
	         when co.order_date = fv.first_visit_date 
	               then co.order_amount
	               else 0 
	               end) as revenue_new_customers, 
         sum(case 
	         when co.order_date > fv.first_visit_date 
	               then co.order_amount
	               else 0 
	               end) as revenue_repeat_customers
         from customer_orders co
         inner join first_visit fv 
                   on co.customer_id = fv.customer_id
      group by co.customer_id   
 order by co.customer_id
 ;
 
 
 ---------------------------------------------------------------------------------------------------------

 with customer_revenue as ( 
      -- Step 1 : Calculate first visit vs repeat revenue for every customer
 select 
      co.customer_id,
     sum(case 
	         when co.order_date = fv.first_order_date 
	               then co.order_amount
	               else 0 
	               end) as first_revenue, 
         sum(case 
	         when co.order_date > fv.first_order_date 
	               then co.order_amount
	               else 0 
	               end) as repeat_revenue, 
	      -- Check if they ever came back
	    (max(co.order_date) > min(co.order_date) )as has_repeated          
         from customer_orders co
         inner join ( 
                select customer_id, min(order_date) as first_order_date
                from customer_orders
      group by customer_id   
 ) fv on co.customer_id = fv.customer_id 
 group by co.customer_id 
 ),
 new_customers_list as ( 
        -- Step 2 : Filter fo customers who only visited once (never repeated)
       select 
            customer_id as new_customer_id,
            first_revenue as new_customer_revenue, 
            row_number() over(order by customer_id) as rn 
            from customer_revenue
            where has_repeated = false or repeat_revenue = 0 
 ), 
 repeat_customers_list as (  
       -- Step 3 : Filter for customers who have returned at least once
       select 
            customer_id as repeat_customer_id, 
            (first_revenue + repeat_revenue) as repeat_customer_revenue,
            row_number() over(order by customer_id) as rn 
        from customer_revenue
        where has_repeated = true and repeat_revenue > 0 
 )  
   -- Step 4 : Emulate FULL OUTER JOIN using LEFT JOIN + UNION + RIGHT JOIN
 select 
      n.new_customer_id,
      n.new_customer_revenue,
      r.repeat_customer_id,
      r.repeat_customer_revenue
 from new_customers_list n 
 left join repeat_customers_list r 
                on n.rn = r.rn
  union              
 select 
      n.new_customer_id,
      n.new_customer_revenue,
      r.repeat_customer_id,
      r.repeat_customer_revenue
 from new_customers_list n 
 right join repeat_customers_list r 
                on n.rn = r.rn;               
 
 
 -------------------------------------------------------------------------------------------------------------
 
 
 create table entries (  
 name varchar(20),
 address varchar(20),
 email varchar(20),
 floor int,
 resources varchar(20)
 );
 
 insert into entries
 values ('A','BANGALORE','A@gmail.com','1','CPU'),
        ('A','BANGALORE','A1@gmail.com','1','CPU'),
        ('A','BANGALORE','A2@gmail.com','2','DESKTOP'),
        ('B','BANGALORE','B@gmail.com','2','DESKTOP'),
        ('B','BANGALORE','B1@gmail.com','2','DESKTOP'),
        ('B','BANGALORE','B2@gmail.com','1','MONITOR');
 
 
 select *
 from entries;
 
 -- name of each person, how many times they visited the floor
 -- also which floor they visited most, resources used by them during their visit
 
 
 -- This query is a trial and error and it is not correct.
 with with rankedcounts as ( 
      select 
            name,
            floor,
            count(*) as times_visited,
            group_concat(resources separator ', ') as resources_used
            from entries
            group by name, floor
            ),
            rankedfloors as ( 
               select 
                     name, 
                     floor,
                     row_number() over(partition by name order by count(*)  desc, floor asc ) as floor_rank
                from entries
                group by name, floor
            )
            select
                  f.name,
                  f.times_visited,
                  r.floor as most_visited_floor,
                  f.resources_used
             from rankedcounts f
            inner join rankedfloors r on f.name = r.name and r.floor_rank = 1
 group by f.name, most_visited_floor
 
 
 
 -- this one is totally coreect and easy and efficient query
 with total_visits as 
 (   
 select 
       name,
      count(1) as total_visits,
      group_concat(distinct resources separator ', ') as resources_used
from entries
group by name 
),
 floor_visit as 
 (  
 select 
      name,
      floor,
      count(1) as no_of_floor_visit,
 rank() over(partition by name order by count(1) desc) as rn      
from entries
group by name, floor ) 
select 
      fv.name,
      fv.floor as most_visited_floor,
      tv.total_visits,
      tv.resources_used
from floor_visit fv 
inner join total_visits tv on fv.name = tv.name
where rn = 1;

----------------------------------------------------------------------------------------------------------

-- Write a Query to provide the date for nth occurrence of Sunday in future from given date
-- datepart
-- sunday 1
-- monday 2
-- friday 6
-- saturday 7


set @today_date ='2022-01-01'; -- saturday
set @n = 3;

select date_add( 
     @today_date,
     interval (8 - dayofweek(@today_date)) +(@n - 1) * 7 day
     ) as nth_sunday;

---------------------------------------------------------------------------------------------------------

/* The Parato principle states that for many outcomes, roughly 80% of consequences come from 20% of causes, eg:
 * 1- 80% of productivity come from 20% of the employees */


select sum(sales) * 0.8 
from orders

with productsales as (
      select      
            product_id, 
            sum(sales) as product_sales, 
 from orders
 group by product_id 
),
cumulativesales as (  
select 
        product_id,
        product_sales,
sum(product_sales) 
	         over (order by product_sales desc
	         rows between unbounded preceding and current row) as running_total
	  from productsales
)
select *
from cumulativesales
where running_total <= 1837760
order by product_sales desc; 

 
-- There is a little but differnce between these two similar looking queries.
-- The first one contains manual calculation while second  is more specific.


with productsales as (
      select      
            product_id, 
            sum(sales) as product_sales, 
 from orders
 group by product_id 
),
cumulativesales as (  
select 
        product_id,
        product_sales,
sum(product_sales) 
	         over (order by product_sales desc
	         rows between unbounded preceding and current row) as running_total,
	         0.8*sum(product_sales) over() as total_sales
	  from productsales
)
select *
from cumulativesales
where running_total <= total_sales
order by product_sales desc; 

