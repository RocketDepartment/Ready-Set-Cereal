CREATE TABLE pending_orders
(
order_id int NOT NULL AUTO_INCREMENT,
time_ordered DATETIME NOT NULL,
c1 int,
c2 int,
c3 int,
milk int,
spoon int,
status varchar(80),
PRIMARY KEY (order_id)
);

CREATE TABLE completed_orders
(
order_id int NOT NULL,
time_ordered DATETIME NOT NULL,
time_served DATETIME NOT NULL,
c1 int,
c2 int,
c3 int,
milk int,
spoon int,
PRIMARY KEY (order_id)
);

CREATE TABLE current_status
(
status varchar(80),
order_id int,
milk_temp varchar(80),
clear varchar(80)
);

CREATE TABLE social_media
(
order_id int NOT NULL,
twitter varchar(80),
facebook varchar(80),
instagram varchar(80)
);