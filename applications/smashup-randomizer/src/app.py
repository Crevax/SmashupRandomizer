from flask import Flask, render_template
from werkzeug.debug import DebuggedApplication
import psycopg2, psycopg2.extras

app = Flask(__name__)
app.debug = True
app.wsgi_app = DebuggedApplication( app.wsgi_app, True )

@app.route("/")
def index():
  #g.db = psycopg2.connect("dbname=smashup-randomizer user=smashup-user", connection_factory=psycopg2.extras.RealDictConnection)
  foo = "bar"
  return render_template('index.html')

if __name__ == "__main__":
  app.run()
