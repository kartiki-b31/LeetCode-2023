# Write your MySQL query statement below

SELECT P.firstName, P.lastName,A.city, A.state 
FROM Address A RIGHT OUTER JOIN PERSON P
ON P.personId=A.personId;

