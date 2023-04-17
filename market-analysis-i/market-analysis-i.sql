# Write your MySQL query statement below

SELECT U.user_id AS buyer_id, U.join_date,COUNT(order_id) AS orders_in_2019
FROM USERS U LEFT JOIN Orders O
ON U.USER_ID=O.BUYER_ID
AND O.order_date>='2019-01-01' AND O.order_date<'2020-01-01'
GROUP BY USER_ID;
