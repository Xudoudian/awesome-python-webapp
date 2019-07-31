-- busdatabase.sql

drop database if exists busdatabase;

create database busdatabase;

use busdatabase;

alter user on busdatabase to 'bus'@'localhost' identified by 'buspassword';

create table users(
    `id` varchar(50) not null,
    `telephone` varchar(50) not null unique,
    `passwd`  varchar(50) not null,
    `name` varchar(50) not null,
    `usertype` varchar(50) not null,
    `image` varchar(500) not null,
    `evaluation` varchar(200) not null,
    `vip` bool not null, 
    `created_at` real not null,
    key `idx_created_at` (`created_at`),
    primary key (`id`)
)engine=innodb default charset=utf8;

create table orders(
    `id` varchar(50) not null,
    `user_id` varchar(50) not null,
    `user_name`  varchar(50) not null,
    `car_id` varchar(50) not null,
    `order_from` varchar(200) not null,
    `order_to` varchar(200) not null,
    `order_acid` varchar(50) not null,
    `price` varchar(200) not null,
    `created_at` real not null,
    key `idx_created_at` (`created_at`),
    primary key (`id`)
)engine=innodb default charset=utf8;

create table cars(
    `id` varchar(50) not null,
    `user_id` varchar(50) not null,
    `user_name` varchar(50) not null,
    `seat`  varchar(50) not null,
    `car_acid` varchar(50) not null,
    `image` varchar(500) not null,
    `content` mediumtext not null,
    `evaluation` varchar(200) not null,
    `location` varchar(50) not null,
    `created_at` real not null,
    key `idx_created_at` (`created_at`),
    primary key (`id`)
)engine=innodb default charset=utf8;