import flask
import psycopg2
from psycopg2 import extras
import os

app = flask.Flask(__name__)

@app.route('/')
def index():
   print('Request for index page received')

   # dummy = [{'ticker':'apple','marketcap':100000}]

   return flask.render_template('index.html', stocks_in_danger = get_sp_500_tickers_in_danger(),
                                 stocks_to_add = get_rising_non_sp_500_tickers())

def get_sp_500_tickers_in_danger():
   sql_query = "select * from tbTickerToMarketcap where SP500mmbr = true and marketcap < 10000000000 order by marketcap"
   data = read_database(sql_query)
   if not data:
      return [{"stock":"bad connection to database","marketcap":0}]
   else: 
      return data

def get_rising_non_sp_500_tickers():
   sql_query = "select * from tbTickerToMarketcap where SP500mmbr = false and marketcap > 14000000000 order by marketcap desc"
   data = read_database(sql_query)
   if not data:
      return [{"stock":"bad connection to database","marketcap":0}]
   else: 
      return data

def read_database(sql_query):
   cursor = None
   conn = None
   db_config = {
   "user": "woody",
    "password": "Thereisasnakeinmyboot1!",
    "host": "indexarb-server.postgres.database.azure.com",
    "database": "dbSPTMI",
    "port": 5432
   }
   try:
      conn = psycopg2.connect(**db_config)
      cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
      cursor.execute(sql_query)

      # Fetch all the rows from the result set as dictionaries
      rows = cursor.fetchall()

      return rows

   except Exception as e:
      print(f"Error: {e}")

   finally:
      if cursor:
         cursor.close()
      if conn:
         conn.close()

if __name__ == '__main__':
   app.run(port=8000)
