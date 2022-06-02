{{ config(materialized='table') }}

select avg(nav) from "FINALWEEK"."PUBLIC"."NAV" group by month(nav_date)
