with psycopg2.connect(
   host = host,
   user = user,
   password = pw,
   dbname = dbname,
   ) as conn:
   cursor = conn.cursor()

   sql_all = """
SELECT * FROM people
"""
   cursor.execute(sql_all)
   for d in cursor.fetchall():
       pass
