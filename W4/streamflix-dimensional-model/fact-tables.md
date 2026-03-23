- Table name
- Grain statement (one specific sentence)
- List of foreign keys to dimensions
- List of measures with type (additive/semi-additive/non-additive)
- Fact table type (transaction/periodic snapshot/accumulating)


Show Metrics
Shows all relevant data for each show in streaming service
- Foreign Keys (Creator_key, show_id INT64, date_key DATETIME) --Non-Additive
- average_watch_time_min DECIMAL -Non-Additive
- number_views -Additive
- average_drop_off_time - Non-Additive
- average_episode_length - Non-additive
- completion_rate - Non-Additive
- rating - Non-Additive

Subscriber Data
Shows all relevent information with users
- Foreign Keys (user_id INT64, plan_type STRING) -- Non-Additive
- age_of_account
- current_sub_duration
- number_of_cancellations
- current_date_subscribed
- show_date