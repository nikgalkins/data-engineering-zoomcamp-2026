/* @bruin

name: reports.trips_report
type: duckdb.sql

depends:
  - staging.trips

materialization:
  type: table

@bruin */

select
  cast(date_trunc('day', pickup_datetime) as date) as trip_date,
  taxi_type,
  coalesce(payment_type_desc, 'Unknown') as payment_type_desc,
  count(*) as trips,
  round(avg(total_amount), 2) as avg_total_amount
from staging.trips
group by 1,2,3;