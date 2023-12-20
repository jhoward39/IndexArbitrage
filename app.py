import flask
import psycopg2
from psycopg2 import extras
import os
import json

app = flask.Flask(__name__)

@app.route('/')
def index():
   print('Request for index page received')

   return flask.render_template('index.html', stocks_in_danger = get_sp_500_tickers_in_danger(),
                                 stocks_to_add = get_rising_non_sp_500_tickers(), ticker_to_history = json.dumps(get_pricing_data()))

def get_sp_500_tickers_in_danger():
   sql_query = "select Ticker, CompanyName, DateAdded, MarketCap from tbTickers where isSP500member = true and marketcap < 10000000000 order by marketcap"
   data = read_database(sql_query)
   if not data:
      return [{"stock":"bad connection to database","marketcap":0}]
   else: 
      return data

def get_rising_non_sp_500_tickers():
   sql_query = "select Ticker, CompanyName, DateAdded, MarketCap from tbTickers where isSP500member = false and marketcap > 20000000000 order by marketcap desc"
   data = read_database(sql_query)
   if not data:
      return [{"stock":"bad connection to database","marketcap":0}]
   else: 
      return data

def get_pricing_data():
   sql_query = "select Ticker, Date, ClosingPriceAtDate from tbPriceData"
   data = read_database(sql_query)
   tickers = []
   ticker_to_history = {}
   for row in data:
      ticker = row["ticker"].strip()
      if ticker in tickers:
         ticker_to_history[ticker].append({"date": row["date"].strftime("%Y-%m-%d"), "price": float(row["closingpriceatdate"])})
      else: 
         tickers.append(ticker)
         ticker_to_history[ticker] = [{"date": row["date"].strftime("%Y-%m-%d"), "price": float(row["closingpriceatdate"])}]

   return ticker_to_history
   
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
   app.run()
