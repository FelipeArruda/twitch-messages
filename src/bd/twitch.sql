CREATE DATABASE twitch;

CREATE TABLE IF NOT EXISTS twitch.event_message(
   id int auto_increment PRIMARY KEY,
   user varchar(500) not null ,
   channel varchar(500) not null ,
   message varchar(500) not null ,
   date datetime
);

alter table event_message
    add created_at datetime not null;

select * from twitch.event_message where channel = 'ale_apoka' and user = 'sudo4root' order by date desc;
select count(*) from twitch.event_message;
select channel, count(*) from twitch.event_message group by channel order by 2 desc;