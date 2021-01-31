insert into dwh_company
select
        a._id,
        a.company_name ,
        a.market_cap,
        a.number_of_employees,
        a.counntry ,
        GETDATE() as etl_updated
from company a
left join dwh_company b on a._id = b._id
where b._id is null;


update dwh_company
   set  _id= a._id,
        company_name= a.company_name ,
        market_cap= a.market_cap,
        number_of_employees= a.number_of_employees,
        counntry= a.counntry ,
        etl_updated= GETDATE()
from  company a
where dwh_company._id = a._id ;
-- option add md5 on several columns to know which records to update