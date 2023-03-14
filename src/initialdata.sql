use mydb;

drop table if exists user;
create table user(user_id int(10) auto_increment, name varchar(50), address varchar(250), primary key (user_id));

drop table if exists bse_bulkdeals;
create table bse_bulkdeals(deal_id int(10) auto_increment, deal_date varchar(10), security_code varchar(10), security_name varchar(100), client_name varchar(100), deal_type enum('B', 'S'), quantity varchar(30), price varchar(30), primary key (deal_id));