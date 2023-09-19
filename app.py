import requests
import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
   print('Request for index page received')
   return flask.render_template('index.html')


if __name__ == '__main__':
   app.run()