-- stg created by pandas


-- dwh
create table dwh_stores  (like stores);
create table dwh_company  (like company);
create table dwh_employees  (like employees);

alter table dwh_stores add column etl_updated datetime;
alter table dwh_company add column etl_updated datetime;
alter table dwh_employees add column etl_updated datetime;