/* @bruin

name: staging.trips
type: duckdb.sql

depends:
  - ingestion.trips
  - ingestion.payment_lookup

materialization:
  type: table

@bruin */

with base as (
  select
    try_cast(tpep_pickup_datetime as timestamp) as pickup_datetime,
    try_cast(tpep_dropoff_datetime as timestamp) as dropoff_datetime,
    cast(pulocationid as integer) as pickup_location_id,
    cast(dolocationid as integer) as dropoff_location_id,
    cast(passenger_count as integer) as passenger_count,
    cast(trip_distance as double) as trip_distance,
    cast(fare_amount as double) as fare_amount,
    cast(total_amount as double) as total_amount,
    cast(payment_type as integer) as payment_type,
    taxi_type
  from ingestion.trips
),
dedup as (
  select *
  from (
    select
      *,
      row_number() over (
        partition by
          pickup_datetime,
          dropoff_datetime,
          pickup_location_id,
          dropoff_location_id,
          fare_amount,
          total_amount,
          taxi_type
        order by pickup_datetime
      ) as rn
    from base
    where pickup_datetime is not null
  )
  where rn = 1
)
select
  d.*,
  p.payment_type_desc
from dedup d
left join ingestion.payment_lookup p
  on d.payment_type = p.payment_type;