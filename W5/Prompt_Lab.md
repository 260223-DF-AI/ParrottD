Challenge1.1

In a BigQuery sql query Find the top departments in average salary and show the top 5.
Select only the department name, average salary, and employee count.
Only where the department has more than 10 employees in it. And order the list desc in average salary in the department

SELECT 
    department_name, 
    AVG(salary) AS average_salary, 
    COUNT(*) AS employee_count
FROM 
    `your_project.your_dataset.employees`
GROUP BY 
    department_name
HAVING 
    employee_count > 10
ORDER BY 
    average_salary DESC
LIMIT 5;

output quality: 5
what I learned: making a zero-shot prompt can be hard for more complex or harder to word problems.


Challenge1.2
Give an explanation for this error and how to fix it:
google.api_core.exceptions.BadRequest: 400 Syntax error: 
Expected end of input but got keyword SELECT at [3:1]

This error typically pops up when you are working with Google BigQuery (via the Python client library).
It essentially means you’ve sent a "broken" SQL script where one statement ended abruptly or 
didn't follow the proper structure before the next one began.

What the Error Means

The message Expected end of input but got keyword SELECT at [3:1] tells you exactly where the parser got confused:

[3:1]: Line 3, Column 1.

The Conflict: BigQuery finished reading what it thought was a complete command on Line 2, but then it saw a new SELECT 
on Line 3 and didn't know how to connect


Common Causes & Fixes

1. Missing Semicolons between Queries

If you are trying to run two queries in the same execution call, BigQuery requires a semicolon ; to separate them. Without it, the engine thinks the second SELECT is part of the first one.

The Wrong Way:

SQL
SELECT name FROM `project.dataset.table1`
SELECT name FROM `project.dataset.table2` -- Error happens here
The Fix:

SQL
SELECT name FROM `project.dataset.table1`;
SELECT name FROM `project.dataset.table2`;

2. Dangling Commas or Missing Keywords

Often, this happens because you forgot a comma in a list of columns, or you didn't finish a FROM clause.

The Wrong Way:

SQL
SELECT 
  col1
  col2 -- Missing comma here!
FROM `table`
In this case, the engine might think col2 is an alias, but if it hits another keyword unexpectedly, it fails.

3. Trailing Characters in Python Strings

If you are building your query string in Python, ensure you don't have accidental characters or improper concatenation.

The Wrong Way:

Python
query = "SELECT * FROM table" + "SELECT * FROM table2" 
# Results in: SELECT * FROM tableSELECT * FROM table2


output quality: 5
what i learned: gemini is got for giving an explanation for an error

Challenge 1.3
give me a data dictionary entry for a column called 'customer_lifetime_value' in a 'dim_customer' table
where the entry includes the data type, description, business definition, calculation method with some example
values for the entry

Here is a comprehensive data dictionary entry for the customer_lifetime_value column.

Data Dictionary: dim_customer
Column Name: customer_lifetime_value

Attribute	Details
Data Type	DECIMAL(18, 2)
Description	The total net profit attributed to the entire future relationship with a customer.
Business Definition	A prediction of the total revenue a customer will generate for the company throughout their entire lifespan as a client. This metric helps the Marketing and Success teams identify high-value segments and determine appropriate customer acquisition cost (CAC) thresholds.
Calculation Method

This value is typically calculated using a predictive model or a historical aggregate. For this table, it represents the Historical CLV, calculated as:

CLV=∑(Transaction Revenue−Transaction Cost)
Formula logic:

Sum the total gross revenue from all completed orders.

Subtract the total cost of goods sold (COGS) and returns.

Exclude pending or cancelled transactions.

Example Values

1250.50: A long-term loyal customer with frequent repeat purchases.

45.00: A new customer who has only made one small initial purchase.

0.00: A lead or registered user who has not yet converted into a paying customer.

-15.25: A customer whose returns and service costs have exceeded their total purchase value (potential churn risk or "unprofitable" segment).

Note: This field is updated via the nightly ETL batch process. If the customer is part of a "Guest" checkout, the CLV may be underrepresented as it cannot be tied to a persistent customer_id.

This would be useful for a new team member
additional context I would use would be whether I wanted the data dictionary entry in something like a readme
or code.

output quality: 5
what I learned: AI can be useful for giving explanations of what you are doing or a structure to
someone new.

Challenge2.1
Given this example transforming these names into snake case:
`CustomerFirstName` -> `customer_first_name`
`order-total-amount` -> `order_total_amount`
`PRODUCT ID` -> `product_id`

can you convert this 4 names into snake case the same way:
`ShippingAddress Line1`
`total_Revenue_YTD`
`customerEmailAddress`
`ORDER__STATUS__CODE`

Following the pattern of your examples, here are the four names converted into snake case:

ShippingAddress Line1 → shipping_address_line1

total_Revenue_YTD → total_revenue_ytd

customerEmailAddress → customer_email_address

ORDER__STATUS__CODE → order_status_code

yes it followed the pattern correctly and it didn't struggle with any of the 4

output quality: 5
what I learned: the ai will try to follow the structure of your example even outside just getting the answer

Challenge 2.2
Given this input query which turns into given output documentation:
Input:
```sql
SELECT customer_id, COUNT(*) as order_count 
FROM orders GROUP BY customer_id
```

Output:

```
Query: Customer Order Count
Purpose: Counts the total number of orders per customer
Tables Used: orders
Output Columns: customer_id, order_count
Aggregation: COUNT grouped by customer_id
```
can you write the output for this query:
```
SELECT p.category, 
       DATE_TRUNC(o.order_date, MONTH) as month,
       SUM(o.quantity * p.unit_price) as revenue,
       COUNT(DISTINCT o.customer_id) as unique_customers
FROM orders o
JOIN products p ON o.product_id = p.product_id
WHERE o.order_date >= '2024-01-01'
GROUP BY 1, 2
ORDER BY 1, 2
```

Query Documentation
Query: Monthly Category Revenue and Customer Reach
Purpose: Calculates monthly revenue and the number of unique customers for each product category, specifically for data from the year 2024 onwards.
Tables Used: * orders (aliased as o)

products (aliased as p)

Output Columns: * category: The classification of the product.

month: The order date truncated to the first of the month.

revenue: Total sales value (

∑(quantity×unit_price)
).

unique_customers: Count of distinct customer IDs.

Aggregation: * SUM of calculated line-item totals.

COUNT(DISTINCT) of customer IDs.

Grouped by category (1) and month (2).

output quality: 4
what I learned: It can give bigger explanation than you expect

Challenge3.1
Given this scenario can you estimate the BigQuery costs:
You have a table with 500 million rows, each row is approximately 500 bytes
- You run a query that scans 3 columns (out of 20 total columns)
- The query runs 4 times per day
- BigQuery charges $6.25 per TB scanned
- Assume columnar storage distributes data evenly across columns

Think through this step by step

To estimate the BigQuery costs for this scenario, we need to calculate the total amount of data scanned per query and then apply the pricing rate.

BigQuery's on-demand pricing is based on the amount of data processed by each query. For billing purposes, Google defines 1 TB as 10 
12
  bytes (decimal).

1. Calculate Total Table Size

First, we find the total size of the table in bytes:

Total Size=Rows×Row Size
Total Size=500,000,000 rows×500 bytes/row
Total Size=250,000,000,000 bytes (or 250 GB)
2. Calculate Size Per Column

BigQuery uses a columnar storage format. Since the data is distributed evenly across 20 columns:

Size per Column= 
20 columns
250 GB
​	
 
Size per Column=12.5 GB per column
3. Calculate Data Scanned per Query

The query scans 3 specific columns. Because BigQuery only charges for the columns actually read:

Data Scanned=3 columns×12.5 GB
Data Scanned=37.5 GB per query
4. Calculate Daily and Monthly Costs

Now we calculate the total data scanned over time and apply the cost of $6.25 per TB.

Daily Data Scanned: 37.5 GB×4 times/day=150 GB/day

Daily Cost: (150 GB/1,000 GB/TB)×$6.25=$0.9375

Monthly Data Scanned (30 days): 150 GB/day×30 days=4,500 GB (4.5 TB)

Monthly Cost: 4.5 TB×$6.25=$28.125

Final Cost Summary

Cost per Query: ≈$0.23

Daily Cost: $0.94

Monthly Cost: $28.13

the final answer seems reasonable and the answer comes after the work so it could make the
response more likely to be correct.

output quality: 5
what I learned: AI can help with business analytics given a scenario


Challenge3.2
Given this scenario diagnose this pipeline issue:
An ETL pipeline extracts data from a REST API, transforms it with Python, and loads it into BigQuery. 
The pipeline ran successfully for 30 days, then suddenly started failing with this error:

```
google.api_core.exceptions.Forbidden: 403 Access Denied: 
BigQuery BigQuery: Permission bigquery.tables.create denied
```

Nothing in the pipeline code changed. The GCP project and service account are the same.

Think through this step by step

This is a classic "it worked yesterday" scenario in GCP. Since the code and the Service Account (SA) haven't changed, the issue almost certainly lies in the IAM environment, resource state, or project-level constraints.

Here is a step-by-step diagnostic path to identify the root cause:

1. Check for "Policy Inheritance" Breaks

Permissions in GCP are often inherited from the Project or Folder level.

The Issue: If the pipeline creates a new table every day (e.g., a sharded table like logs_20260323), it requires bigquery.tables.create on the Dataset.

The Fix: Check if someone manually changed the permissions on the specific BigQuery Dataset where the pipeline writes. If the SA was granted "BigQuery Data Editor" at the dataset level and that role was removed, the pipeline will fail even if the SA still has project-level roles.

2. Service Account Key Expiration

If you are using a JSON key file for authentication:

The Issue: Service account keys can be created with an expiration date. If the key reached its 30-day (or 1-year) limit, the API will reject the request.

The Fix: Check the "Keys" tab of the Service Account in the IAM console. If the key is expired, you'll need to rotate it (generate a new one and update your pipeline's environment variables).

3. Resource Quotas and "Exceeded" Limits

While the error says "Permission Denied," GCP sometimes throws a 403 when a Quota is hit that prevents the creation of new resources.

The Issue: BigQuery has a limit on the number of table partitions or the number of tables within a dataset. If your Python script creates a new table for every run, you might have hit a limit (e.g., the 1,000-partition limit per table or project-wide table limits).

The Fix: Check the Quotas & System Limits page in the GCP Console for BigQuery.

4. Organization-Level Policy Changes

If you are in a corporate environment, a Cloud Admin may have pushed a new Organization Policy.

The Issue: A new policy might have been enacted that restricts resource creation to specific regions or requires specific labels. Even if your SA has the "Role," the "Policy" can override it.

The Fix: Check for "Deny" policies in the IAM & Admin > Organization Policies section.

5. The "Custom Role" Drift

Are you using a Custom IAM Role instead of a predefined one like BigQuery Data Editor?

The Issue: If your admin modified the definition of a Custom Role to remove bigquery.tables.create, every Service Account assigned that role loses the permission simultaneously.

The Fix: Verify the permissions inside the specific role assigned to the SA.


The steps where logical and it thinks the most likely issues are with someone changing permissions and
potentially the json key expiring. I would check the expiring first but there are reasons to check permissions first

output quality: 5
what I learned: chain of thought prompting is good.

For each challenge, document:

1. Your prompt (original and refined versions)
2. The LLM's output
3. Your evaluation of the output quality (1-5 scale)
4. What you learned about prompting from that challenge