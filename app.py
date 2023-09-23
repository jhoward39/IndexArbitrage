import flask
import yfinance as yf

app = flask.Flask(__name__)

@app.route('/')
def index():
   print('Request for index page received')
   return flask.render_template('index.html', 
            stocks_in_danger = ['AAPL'],
            stocks_to_add = ['NOK'],
            last_updated = "10/25/2000")

if __name__ == '__main__':
   app.run()