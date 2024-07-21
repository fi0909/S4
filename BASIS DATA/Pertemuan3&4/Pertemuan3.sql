select *  from customer ;
SELECT * from customer ORDER BY CustomerID DESC;
select * from customer where Country like '%France%';
select distinct Country from customer;
select * from customer where Country = ANY(select Country from customer where Country like '%France%' or Country like '%Germany%');
select * from customer where Country = ANY(select Country from customer where City in ('Paris ','Berlin '));
select CustomerID,CustomerName,Address,PostalCode,
	case when PostalCode is not null then 'right'
		else 'Nothing here' end as num
from customer;
select @rowid:=@rowid+1 as rowid
from customer, (select @rowid:=0) as init
order by Address;
select Price,unit,count(Unit) as banyak_unit,sum(Price) as total_harga from products GROUP BY Unit,Price;
select * from products ORDER BY price asc limit 10;


