-- SQL Project - Data Cleaning

-- https://www.kaggle.com/datasets/swaptr/layoffs-2022






SELECT * 
FROM world_layoffs.layoffs;



-- first thing we want to do is create a staging table. This is the one we will work in and clean the data. We want a table with the raw data in case something happens
CREATE TABLE world_layoffs.layoffs_staging 
LIKE world_layoffs.layoffs;

INSERT layoffs_staging 
SELECT * FROM world_layoffs.layoffs;


-- now when we are data cleaning we usually follow a few steps
-- 1. check for duplicates and remove any
-- 2. standardize data and fix errors
-- 3. Look at null values and see what 
-- 4. remove any columns and rows that are not necessary - few ways



-- 1. Remove Duplicates

# First let's check for duplicates



SELECT *
FROM world_layoffs.layoffs_staging
;

SELECT company, industry, total_laid_off,`date`,
		ROW_NUMBER() OVER (
			PARTITION BY company, industry, total_laid_off,`date`) AS row_num
	FROM 
		world_layoffs.layoffs_staging;



SELECT *
FROM (
	SELECT company, industry, total_laid_off,`date`,
		ROW_NUMBER() OVER (
			PARTITION BY company, industry, total_laid_off,`date`
			) AS row_num
	FROM 
		world_layoffs.layoffs_staging
) duplicates
WHERE 
	row_num > 1;
    
-- let's just look at oda to confirm
SELECT *
FROM world_layoffs.layoffs_staging
WHERE company = 'Oda'
;
-- it looks like these are all legitimate entries and shouldn't be deleted. We need to really look at every single row to be accurate

-- these are our real duplicates 
SELECT *
FROM (
	SELECT company, location, industry, total_laid_off,percentage_laid_off,`date`, stage, country, funds_raised_millions,
		ROW_NUMBER() OVER (
			PARTITION BY company, location, industry, total_laid_off,percentage_laid_off,`date`, stage, country, funds_raised_millions
			) AS row_num
	FROM 
		world_layoffs.layoffs_staging
) duplicates
WHERE 
	row_num > 1;

-- these are the ones we want to delete where the row number is > 1 or 2or greater essentially

-- now you may want to write it like this:
WITH DELETE_CTE AS 
(
SELECT *
FROM (
	SELECT company, location, industry, total_laid_off,percentage_laid_off,`date`, stage, country, funds_raised_millions,
		ROW_NUMBER() OVER (
			PARTITION BY company, location, industry, total_laid_off,percentage_laid_off,`date`, stage, country, funds_raised_millions
			) AS row_num
	FROM 
		world_layoffs.layoffs_staging
) duplicates
WHERE 
	row_num > 1
)
DELETE
FROM DELETE_CTE
;


WITH DELETE_CTE AS (
	SELECT company, location, industry, total_laid_off, percentage_laid_off, `date`, stage, country, funds_raised_millions, 
    ROW_NUMBER() OVER (PARTITION BY company, location, industry, total_laid_off, percentage_laid_off, `date`, stage, country, funds_raised_millions) AS row_num
	FROM world_layoffs.layoffs_staging
)
DELETE FROM world_layoffs.layoffs_staging
WHERE (company, location, industry, total_laid_off, percentage_laid_off, `date`, stage, country, funds_raised_millions, row_num) IN (
	SELECT company, location, industry, total_laid_off, percentage_laid_off, `date`, stage, country, funds_raised_millions, row_num
	FROM DELETE_CTE
) AND row_num > 1;

-- one solution, which I think is a good one. Is to create a new column and add those row numbers in. Then delete where row numbers are over 2, then delete that column
-- so let's do it!!

ALTER TABLE world_layoffs.layoffs_staging ADD row_num INT;


SELECT *
FROM world_layoffs.layoffs_staging
;

CREATE TABLE `world_layoffs`.`layoffs_staging2` (
`company` text,
`location`text,
`industry`text,
`total_laid_off` INT,
`percentage_laid_off` text,
`date` text,
`stage`text,
`country` text,
`funds_raised_millions` int,
row_num INT
);

INSERT INTO `world_layoffs`.`layoffs_staging2`
(`company`,
`location`,
`industry`,
`total_laid_off`,
`percentage_laid_off`,
`date`,
`stage`,
`country`,
`funds_raised_millions`,
`row_num`)
SELECT `company`,
`location`,
`industry`,
`total_laid_off`,
`percentage_laid_off`,
`date`,
`stage`,
`country`,
`funds_raised_millions`,
		ROW_NUMBER() OVER (
			PARTITION BY company, location, industry, total_laid_off,percentage_laid_off,`date`, stage, country, funds_raised_millions
			) AS row_num
	FROM 
		world_layoffs.layoffs_staging;

-- now that we have this we can delete rows were row_num is greater than 2

DELETE FROM world_layoffs.layoffs_staging2
WHERE row_num >= 2;







-- 2. Standardize Data

use world_layoffs;

select company, trim(company)
from layoffs_staging2;

update layoffs_staging2
set company = trim(company);


select distinct industry
from layoffs_staging2
order by 1;


select distinct industry
from layoffs_staging2
where industry like 'crypto%';

update layoffs_staging2
set industry = 'crypto'
where industry like 'crypto%';


select distinct country
from layoffs_staging2
order by 1;


select *
from layoffs_staging2
where country like 'United States%'
order by 1;



select distinct country, trim(trailing '.' from country)
from layoffs_staging2
order by 1;

update layoffs_staging2
set country = trim(trailing '.' from country)
where country like 'United States%';

select date,
str_to_date(date, '%m/%d/%y')
from layoffs_staging2;

update layoffs_staging2
set date = str_to_date(date, '%m/%d/%Y')

select DATE 
from layoffs_staging2
where str_to_date(date, '%m%/d%/Y') is null    
   and date is not null 
   and date != '';

update layoffs_staging2 
set date = case 
	  when date like '%/%/%/' then str_to_date(date, '%m/%d/%Y')
	   when date like '%-%-%' then str_to_date(date, '%m-%d-%Y')
          else date 
          end;



update layoffs_staging2
set date = str_to_date(date, '%m/%d/%Y') 
where date like '%/%/%';

select *
from layoffs_staging2;


update layoffs_staging2
set `date` = null 
where `date` = '' or `date` = 'null';


alter table layoffs_staging2
modify column `date` DATE;



select *
from layoffs_staging2
where total_laid_off = 'null' 
and percentage_laid_off = 'null';


select distinct industry
from layoffs_staging2;

update layoffs_staging2
set industry = null 
where industry = '';

select *
from layoffs_staging2
where industry = 'null' 
or industry = '';



select *
from layoffs_staging2
where company = 'Airbnb';


select *
from layoffs_staging2 st1
join layoffs_staging2 st2
     on st1.company = st2.company
     and st1.location = st2.location 
  where (st1.industry is null or st1.industry = '')
   and st2.industry is not null
   
   update layoffs_staging2 st1
join layoffs_staging2 st2
     on st1.company = st2.company
set st1.industry = st2.industry
where st1.industry is null 
   and st2.industry is not null
     
   
select *
from layoffs_staging2
where company like 'Bally%';


delete
from layoffs_staging2
where total_laid_off = 'null' 
and percentage_laid_off = 'null';

alter table layoffs_staging2
drop column row_num;