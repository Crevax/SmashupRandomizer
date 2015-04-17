from flask import Flask, render_template
from werkzeug.debug import DebuggedApplication
import psycopg2, psycopg2.extras

app = Flask(__name__)
app.debug = True
app.wsgi_app = DebuggedApplication( app.wsgi_app, True )

@app.route("/")
def index():
  conn = psycopg2.connect("host=localhost dbname=smashup_randomizer user=smashup_user password=123four", connection_factory=psycopg2.extras.RealDictConnection)
  conn.close()
  return render_template('index.html', info=conn)

if __name__ == "__main__":
  app.run()
