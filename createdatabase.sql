#
# createdatabase.sql
#
# Create a MySql database, database user, table and permissions to store user information
#
# Run from command line (will prompt for mysql root password):
#
# mysql -h <host> -u root -p < createdatabase.sql

drop database if exists holextdb;
drop user if exists 'holextusr'@'localhost';

create database holextdb;

use holextdb;

create table userinfo ( `userid`   integer unsigned auto_increment primary key,
                        `email`    varchar(50) not null unique,
                        `forename` varchar(25) not null,
                        `surname`  varchar(35) not null,
                        `created`  datetime not null)
                        character set 'utf8'
                        collate 'utf8_general_ci'
                        engine InnoDB;

create user 'holextusr'@'localhost' identified by 'somepassword';

grant select, insert, update, delete on holextdb.userinfo to 'holextusr'@'localhost'