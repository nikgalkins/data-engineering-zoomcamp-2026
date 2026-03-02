import duckdb

con = duckdb.connect("dlt_hw.duckdb")

T = '"dlt_hw_ds"."trips"'

# Q1: start/end date 
q1 = f"""
with x as (
  select
    min(trip_pickup_date_time) as min_dt,
    max(trip_pickup_date_time) as max_dt
  from {T}
)
select
  date(min_dt) as min_date,
  date(max_dt) as max_date,
  date_trunc('month', min_dt)::date as month_start,
  (date_trunc('month', min_dt) + interval 1 month)::date as month_end_exclusive
from x;
"""
print("Q1:")
print(con.sql(q1).df())

q2a = f"""
select payment_type, count(*) as cnt
from {T}
group by 1
order by cnt desc;
"""
print("\nPayment types:")
print(con.sql(q2a).df())

# Q2
q2 = f"""
select
  count(*) as total,
  sum(case
        when lower(payment_type) like '%credit%' then 1
        when payment_type = '1' then 1
        else 0
      end) as credit_card_cnt,
  round(
    100.0 * sum(case
        when lower(payment_type) like '%credit%' then 1
        when payment_type = '1' then 1
        else 0
      end) / count(*),
    2
  ) as credit_card_pct
from {T};
"""
print("\nQ2:")
print(con.sql(q2).df())

# Q3: total tips
q3 = f"""
select round(sum(tip_amt), 2) as total_tips
from {T};
"""
print("\nQ3:")
print(con.sql(q3).df())