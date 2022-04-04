CREATE DATABASE twitch;
-- drop table twitch.event_message;
CREATE TABLE IF NOT EXISTS twitch.event_message(
   id int auto_increment PRIMARY KEY,
   user varchar(500) not null ,
   channel varchar(500) not null ,
   message varchar(500) not null ,
   date datetime
);

alter table event_message
    add created_at datetime not null;

select * from twitch.event_message where channel = 'mch_agg' and user ='sudo4root'  order by date desc;
select count(*) from twitch.event_message;
select channel, count(*) from twitch.event_message group by channel order by 2 desc;

select * from twitch.event_message order by  created_at desc;

select user, channel, count(id) from twitch.event_message group by user,channel order by count(id) desc;

delete from twitch.event_message where channel in ('kamet0', 'xqcow', 'mizkif', 'hasanabi', 'rubius', 'elspreen', 'summit1g', 'yoda');