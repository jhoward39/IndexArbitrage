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
   
def get_dummy_pricing_data():
   ticker_to_history = {}
   ticker_to_history["OGN"] = [{ 'date': '1997-11-01', 'price': 3.32 }, { 'date': '1997-12-01', 'price': 3.54 }, { 'date': '1998-01-01', 'price': 3.63 }, { 'date': '1998-02-01', 'price': 3.61 }, { 'date': '1998-03-01', 'price': 4.12 }, { 'date': '1998-04-01', 'price': 3.64 }, { 'date': '1998-05-01', 'price': 3.68 }, { 'date': '1998-06-01', 'price': 3.95 }, { 'date': '1998-07-01', 'price': 3.93 }, { 'date': '1998-08-01', 'price': 3.19 }, { 'date': '1998-09-01', 'price': 3.21 }, { 'date': '1998-10-01', 'price': 3.55 }, { 'date': '1998-11-01', 'price': 3.61 }, { 'date': '1998-12-01', 'price': 4.15 }, { 'date': '1999-01-01', 'price': 4.39 }, { 'date': '1999-02-01', 'price': 4.21 }, { 'date': '1999-03-01', 'price': 4.08 }, { 'date': '1999-04-01', 'price': 4.81 }, { 'date': '1999-05-01', 'price': 5.2 }, { 'date': '1999-06-01', 'price': 5.91 }, { 'date': '1999-07-01', 'price': 5.7 }, { 'date': '1999-08-01', 'price': 5.08 }, { 'date': '1999-09-01', 'price': 5.43 }, { 'date': '1999-10-01', 'price': 5.46 }, { 'date': '1999-11-01', 'price': 5.63 }, { 'date': '1999-12-01', 'price': 6.42 }, { 'date': '2000-01-01', 'price': 6.59 }, { 'date': '2000-02-01', 'price': 8.25 }, { 'date': '2000-03-01', 'price': 6.03 }, { 'date': '2000-04-01', 'price': 8.11 }, { 'date': '2000-05-01', 'price': 7.28 }, { 'date': '2000-06-01', 'price': 8.02 }, { 'date': '2000-07-01', 'price': 10.36 }, { 'date': '2000-08-01', 'price': 9.61 }, { 'date': '2000-09-01', 'price': 9.15 }, { 'date': '2000-10-01', 'price': 8.89 }, { 'date': '2000-11-01', 'price': 9.21 }, { 'date': '2000-12-01', 'price': 10.22 }, { 'date': '2001-01-01', 'price': 9.75 }, { 'date': '2001-02-01', 'price': 9.73 }, { 'date': '2001-03-01', 'price': 8.92 }, { 'date': '2001-04-01', 'price': 8.83 }, { 'date': '2001-05-01', 'price': 9.74 }, { 'date': '2001-06-01', 'price': 9.1 }, { 'date': '2001-07-01', 'price': 10.05 }, { 'date': '2001-08-01', 'price': 10.16 }, { 'date': '2001-09-01', 'price': 9.47 }, { 'date': '2001-10-01', 'price': 8.76 }, { 'date': '2001-11-01', 'price': 9.1 }, { 'date': '2001-12-01', 'price': 9.47 }, { 'date': '2002-01-01', 'price': 10.18 }, { 'date': '2002-02-01', 'price': 9.55 }, { 'date': '2002-03-01', 'price': 11.02 }, { 'date': '2002-04-01', 'price': 10.35 }, { 'date': '2002-05-01', 'price': 11.14 }, { 'date': '2002-06-01', 'price': 11.02 }, { 'date': '2002-07-01', 'price': 9.88 }, { 'date': '2002-08-01', 'price': 9.09 }, { 'date': '2002-09-01', 'price': 8.9 }, { 'date': '2002-10-01', 'price': 9.76 }, { 'date': '2002-11-01', 'price': 10.09 }, { 'date': '2002-12-01', 'price': 10.3 }, { 'date': '2003-01-01', 'price': 9.27 }, { 'date': '2003-02-01', 'price': 10.16 }, { 'date': '2003-03-01', 'price': 10.82 }, { 'date': '2003-04-01', 'price': 12.21 }, { 'date': '2003-05-01', 'price': 12.36 }, { 'date': '2003-06-01', 'price': 11.76 }, { 'date': '2003-07-01', 'price': 12.28 }, { 'date': '2003-08-01', 'price': 12.61 }, { 'date': '2003-09-01', 'price': 12.39 }, { 'date': '2003-10-01', 'price': 13.11 }, { 'date': '2003-11-01', 'price': 13.12 }, { 'date': '2003-12-01', 'price': 12.63 }, { 'date': '2004-01-01', 'price': 12.67 }, { 'date': '2004-02-01', 'price': 13.24 }, { 'date': '2004-03-01', 'price': 13.87 }, { 'date': '2004-04-01', 'price': 13.76 }, { 'date': '2004-05-01', 'price': 13.94 }, { 'date': '2004-06-01', 'price': 15.37 }, { 'date': '2004-07-01', 'price': 14.7 }]
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
