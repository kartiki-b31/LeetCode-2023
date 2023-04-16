# Write your MySQL query statement below
UPDATE SALARY
SET SEX=CASE SEX
WHEN 'm' then 'f'
else 'm' end;