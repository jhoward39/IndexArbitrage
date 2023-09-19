import requests
import flask
import pandas
import yfinance as yf

app = flask.Flask(__name__)

@app.route('/')
def index():
   print('Request for index page received')
   stock = get_ticker('AAPL')
   return flask.render_template('index.html', name = 'AAPL', data = stock.to_html())

def get_ticker(ticker):
   ticker = [ticker]
   # start = datetime.datetime(2020, 1, 1)
   # end = datetime.datetime(2022, 1, 1)
   data = yf.download(ticker)
   return data


if __name__ == '__main__':
   app.run()