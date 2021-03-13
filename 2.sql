

select count(*) from (select count(*) from event_log as el where el.event_timestamp
between UNIX_TIMESTAMP("2020-09-01") and UNIX_TIMESTAMP("2020-09-30")
group by el.user_id
having count(user_id)>=1000 and count(user_id)<2000) childSelect;
