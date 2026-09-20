-- Exploratory Data Analysis

use world_layoffs;

select *
from layoffs_staging2;



update layoffs_staging2
set total_laid_off = null 
where  total_laid_off = ''
or total_laid_off = 'null' 
or  total_laid_off is null 


update layoffs_staging2
set percentage_laid_off = null 
where  percentage_laid_off = ''
or percentage_laid_off = 'null' 
or percentage_laid_off is null 

update layoffs_staging2
set funds_raised_millions= null 
where  funds_raised_millions = ''
or funds_raised_millions= 'null' 
or funds_raised_millions is null 

alter table  layoffs_staging2
modify column total_laid_off int null;

alter table  layoffs_staging2
modify column percentage_laid_off float null; 

alter table  layoffs_staging2
modify column funds_raised_millions  int null;

select max(total_laid_off), max(percentage_laid_off)
from layoffs_staging2;

select *
from layoffs_staging2
where percentage_laid_off = 1
order by total_laid_off desc;


select *
from layoffs_staging2
where percentage_laid_off = 1
order by funds_raised_millions desc;


select company, sum(total_laid_off)
from layoffs_staging2
group by company
order by 2 desc;


select min(date), max(date)
from layoffs_staging2;

select industry, sum(total_laid_off)
from layoffs_staging2
group by industry
order by 2 desc;

select country, sum(total_laid_off)
from layoffs_staging2
group by country
order by 2 desc;

select year(date), sum(total_laid_off)
from layoffs_staging2
group by year(date)
order by 1 desc;


select stage, sum(total_laid_off)
from layoffs_staging2
group by stage
order by 2 desc;

select *
from layoffs_staging2
where stage like 'Post%';

select company, avg(percentage_laid_off)
from layoffs_staging2
group by company
order by 2 desc;


select substring(date, 1,7) as  month, sum(total_laid_off)
from layoffs_staging2
where substring(date, 1,7) is not null
group by month
order by 1 asc;


with rolling_total as 
(
select substring(date, 1,7) as  month, sum(total_laid_off) as total_off
from layoffs_staging2
where substring(date, 1,7) is not null
group by month
order by 1 asc
) 
select month, total_off,
sum (total_off) over(order by month) as rolling_total 
from rolling_total;




select company, sum(total_laid_off)
from layoffs_staging2
group by company
order by 2 desc;


select company, year(date), sum(total_laid_off)
from layoffs_staging2
group by company, year(date)
order by 3 desc;


with company_year (company, years, total_laid_off) as  
( 
select company, year(date), sum(total_laid_off)
from layoffs_staging2
group by company, year(date)
), company_year_rank as
(select *,
          dense_rank()
               over (partition by years order by total_laid_off desc) 
                                                                 as Ranking
from company_year
where years is not null 
) 
select *
from company_year_rank
where ranking <= 5
;