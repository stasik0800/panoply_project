insert into dwh_stores
select
        a.store_id,
        a.store_name,
        a.number_of_employees,
        a._id,
        GETDATE() as etl_updated
from stores a
left join dwh_stores b on a.store_id = b.store_id
where b.store_id is null;



update dwh_stores
   set store_id = b.store_id,
       store_name = b.store_name,
       number_of_employees = b.number_of_employees,
       _id = b._id,
       etl_updated = GETDATE()
from  stores b
where dwh_stores.store_id = b.store_id;