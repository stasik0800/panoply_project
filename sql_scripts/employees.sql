insert into dwh_employees
select
        a.emp_id,
        a.first_name,
        a.last_name,
        a.email,
        a.salery,
        a.store_id,
        GETDATE() as etl_updated
from employees a
left join dwh_employees b on a.emp_id = b.emp_id
where b.emp_id is null;


update dwh_employees
   set emp_id = b.emp_id,
       first_name = b.first_name,
       last_name = b.last_name,
       email = b.email,
       salery = b.salery,
       store_id = b.store_id,
       etl_updated = GETDATE()
from  employees b
where dwh_employees.emp_id = b.emp_id;
-- option add md5 on several columns to know which records to update