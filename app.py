import requests
import flask
import pandas
import yfinance as yf

app = flask.Flask(__name__)

@app.route('/')
def index():
   print('Request for index page received')
   return flask.render_template('index.html', 
            stocks_in_danger = ['AAPL'],
            stocks_to_add = ['NOK'],
            last_updated = "10/25/2000")

def get_ticker(ticker):
   ticker = [ticker]
   # start = datetime.datetime(2020, 1, 1)
   # end = datetime.datetime(2022, 1, 1)
   data = yf.download(ticker)
   return data


if __name__ == '__main__':
   app.run(port=8000)