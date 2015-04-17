from flask import abort, Flask, render_template
from werkzeug.debug import DebuggedApplication
import psycopg2, psycopg2.extras

app = Flask(__name__)
app.debug = True
app.wsgi_app = DebuggedApplication( app.wsgi_app, True )

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/db_check")
def db_check():
  conn = psycopg2.connect("host=localhost dbname=smashup_randomizer user=smashup_user password=123four", connection_factory=psycopg2.extras.RealDictConnection)
  conn.close()
  return "It Works!"

@app.route("/coffee")
def coffee():
  abort(418)

@app.errorhandler(418)
def am_teapot(error):
  return render_template("teapot.html"), 418

if __name__ == "__main__":
  app.run()
