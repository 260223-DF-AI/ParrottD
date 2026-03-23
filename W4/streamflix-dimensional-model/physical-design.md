Partitioning strategy for each fact table
- Clustering columns for each table
- Estimated table sizes and growth rates
- Recommended load frequency


Subscriber Data
- Partition by month
- clustering with user_key, plan_key, current_sub_duration
- Table size to be in the millions and growth rate around 8-10%
- load frequency around a month
Show Metrics
- clustering with show_id, average_watch_time, rating
- Partition by week
- Tablesize around ~1000s shows and growth rate ~5%
- load frequency- every week