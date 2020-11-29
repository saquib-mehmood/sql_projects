#  Write a basic `select` query that will return all of the values from the `recent_grads` table, and **store this query as a string named query**.
# - use the `Cursor` method `execute()` to run the query against our database.
# - Return the full results set and store it as results.
# - Print the first three tuples in the list results.

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

# SQL Query as a string
query = "select * from recent_grads;"
# Execute the query, convert the results to tuples, and store as a local variable
cursor.execute(query)
# Fetch the full results set as a list of tuples
results = cursor.fetchall()
# Display the first three results
print(results[0:3])