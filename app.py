import flask
import psycopg2
from psycopg2 import extras

app = flask.Flask(__name__)

@app.route('/')
def index():
   print('Request for index page received')
   
   return flask.render_template('index.html', 
            stocks_in_danger = get_sp_500_tickers_in_danger(),
            stocks_to_add = get_rising_non_sp_500_tickers(),
            last_updated = "09/26/2023 10:30:05 AM")

def get_sp_500_tickers_in_danger():
   try:
      conn = psycopg2.connect(**db_params)
      cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
      sql_query = "select * from tbTickerToMarketcap where SP500mmbr = true and marketcap < 10000000000 order by marketcap"
      
      cursor.execute(sql_query)

      # Fetch all the rows from the result set as dictionaries
      rows = cursor.fetchall()

      # Process the data (access columns by name)
      return rows # Access 'sp500mmbr' column

   except Exception as e:
      print(f"Error: {e}")

   finally:
      cursor.close()
      conn.close()

def get_rising_non_sp_500_tickers():
   try:
      conn = psycopg2.connect(**db_params)
      cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
      sql_query = "select * from tbTickerToMarketcap where SP500mmbr = false and marketcap > 14000000000 order by marketcap desc"
      
      cursor.execute(sql_query)

      # Fetch all the rows from the result set as dictionaries
      rows = cursor.fetchall()

      return rows

   except Exception as e:
      print(f"Error: {e}")

   finally:
      cursor.close()
      conn.close()

if __name__ == '__main__':
   db_params = {
    "user": "woody",
    "password": "Thereisasnakeinmyboot1!",
    "host": "indexarb-server.postgres.database.azure.com",
    "database": "dbSPTMI",
    "port": 5432
    }
   app.run()