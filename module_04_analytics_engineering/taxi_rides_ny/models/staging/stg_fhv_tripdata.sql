with source as (
    select * from {{ source('raw', 'fhv_tripdata') }}
),
renamed as (
    select
        dispatching_base_num,
        pickup_datetime,
        dropoff_datetime,
        cast(pulocationid as int64) as pickup_location_id,
        cast(dolocationid as int64) as dropoff_location_id,
        cast(sr_flag as int64) as sr_flag,
        affiliated_base_number
    from source
    where dispatching_base_num is not null
)
select * from renamed
