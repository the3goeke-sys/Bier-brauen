import sqlite3
import pandas as pd

conn = sqlite3.connect("database/brauerei.db")

df = pd.read_sql_query("""
SELECT *
FROM messungen
ORDER BY id DESC
LIMIT 5
""", conn)

conn.close()

print("Letzte 5 Messungen:")
print(df)
