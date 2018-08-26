CREATE DATABASE homework6;
USE sakila;
	#1.a
select first_name,last_name from actor;

	#1.b
SELECT UPPER(concat(first_name,", ",last_name)) AS "Actor Name" FROM actor;

	#2.a
select actor_id, first_name,last_name from actor where first_name="Joe";

	#2.b
select actor_id, first_name, last_name from actor where upper(last_name) like "%GEN%";

	#2.c
select actor_id, first_name, last_name from actor where upper(last_name) like "%LI%" order by last_name,first_name;

	#2.d 
select country_id,country from country where country in ("Afghanistan", "Bangladesh", "China");

	#3.a
ALTER TABLE actor ADD COLUMN description blob;

	#3.b
ALTER TABLE actor DROP COLUMN description;

	#4.a
SELECT last_name, COUNT(last_name)as"number of last name" from actor group by last_name;

	#4.b
SELECT last_name, COUNT(last_name)as"number of last name" from actor group by last_name HAVING COUNT(last_name) > 1;

	#4.c
#Select actor_id,first_name,last_name from actor where (first_name="GROUCHO" AND last_name="WILLIAMS");
UPDATE actor SET first_name="HARPO", last_name="WILLIAMS" where (first_name="GROUCHO" AND last_name="WILLIAMS");
#Select actor_id,first_name,last_name from actor where (first_name="HARPO" AND last_name="WILLIAMS");

	#4.d
UPDATE actor SET first_name="GROUCHO", last_name="WILLIAMS" where (first_name="HARPO" AND last_name="WILLIAMS");

	#5.a
#show create table address;
CREATE TABLE `address` (
   `address_id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
   `address` varchar(50) NOT NULL,
   `address2` varchar(50) DEFAULT NULL,
   `district` varchar(20) NOT NULL,
   `city_id` smallint(5) unsigned NOT NULL,
   `postal_code` varchar(10) DEFAULT NULL,
   `phone` varchar(20) NOT NULL,
   `location` geometry NOT NULL,
   `last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
   PRIMARY KEY (`address_id`),
   KEY `idx_fk_city_id` (`city_id`),
   SPATIAL KEY `idx_location` (`location`),
   CONSTRAINT `fk_address_city` FOREIGN KEY (`city_id`) REFERENCES `city` (`city_id`) ON UPDATE CASCADE
 ) ENGINE=InnoDB AUTO_INCREMENT=606 DEFAULT CHARSET=utf8

	#6.a
SELECT s.first_name, s.last_name, a.address from staff s join address a on (s.address_id=a.address_id);
    #6.b
SELECT s.first_name, s.last_name, SUM(p.amount) from staff s join payment p 
on (s.staff_id=p.staff_id) where p.payment_date like "2005-08-%"
group by s.first_name; 
#Select * from staff;	
#Select * from payment;
    
    #6.c
Select f.film_id,a.actor_id as"actor #" from film_actor f
Inner join actor a
on a.actor_id=f.actor_id
where f.actor_id in (a.actor_id)
 group by film_id ;
 
select * from actor limit 10;
select * from film_actor limit 10;

	#6.d
select count(*)as"number of Hunchback Impossible" from inventory where film_id 
in (
select film_id from film where title = "Hunchback Impossible"
);

select * from inventory limit 10;
select * from film where title = "Hunchback Impossible";
	
    #6.e
select c.last_name, SUM(p.amount) from customer c inner join payment p
on c.customer_id=p.customer_id group by c.last_name;
    
    #7.a
select title from film where title like "k%"or title like "q%";

	#7.b
select last_name, first_name from actor where actor_id in (
select actor_id from film_actor where film_id in(
select film_id from film where title ="Alone Trip"));
	
    #7.c
select c.last_name, c.first_name, c.email from customer c
inner join address a on c.address_id=a.address_id 
inner join city ci on a.city_id=ci.city_id
inner join country cy on ci.country_id=cy.country_id where cy.country="Canada";

	#7.d
select * from film where film_id in(
select film_id from film_category where category_id in(
select category_id from category where name="Family")
);

	#7.e
select film.title, count(film.title) as "rent rate" from film join inventory on film.film_id=inventory.film_id
join rental on inventory.inventory_id=rental.inventory_id group by title order by count(*) desc;
	
    #7.f
select s.store_id, count(p.amount) as "total amount" from store s 
join customer c on s.store_id=c.store_id
join payment p on p.customer_id=c.customer_id group by s.store_id;

	#7.g
select s.store_id,c.city, cy.country from store s 
join address a on s.address_id=a.address_id 
join city c on a.city_id=c.city_id
join country cy on c.country_id=cy.country_id;

	#7.h
select c.category_id,c.name,count(p.amount) as "Gorss revenue" from category c
join film_category fc on c.category_id=fc.category_id
join inventory i on fc.film_id=i.film_id
join rental r on r.inventory_id=i.inventory_id
join payment p on p.customer_id=r.customer_id group by category_id order by count(*) desc; 

	#8.a
create view top_five as
select c.category_id,c.name,count(p.amount) as "Gorss revenue" from category c
join film_category fc on c.category_id=fc.category_id
join inventory i on fc.film_id=i.film_id
join rental r on r.inventory_id=i.inventory_id
join payment p on p.customer_id=r.customer_id group by category_id order by count(*) asc; 

	#8.b
select * from top_five;
	# 8.c
drop view top_five;





