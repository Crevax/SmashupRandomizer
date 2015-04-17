from flask import abort, Flask, render_template
from werkzeug.debug import DebuggedApplication
import psycopg2, psycopg2.extras

# configuration - will be refactored and moved later
DEBUG       = True
SECRET_KEY  ='development key'
DB_HOST     = 'localhost'
DB_NAME     = 'smashup_randomizer'
DB_USER     = 'smashup_user'
DB_PASS     = '123four'

app = Flask(__name__)
app.config.from_object(__name__)
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/db_check")
def db_check():
  conn = psycopg2.connect(host=app.config['DB_HOST'], database=app.config['DB_NAME'], user=app.config['DB_USER'], password=app.config['DB_PASS'], connection_factory=psycopg2.extras.RealDictConnection)
  conn.close()
  return "It Works!"

@app.route('/schema')
def create_schema():
  conn = psycopg2.connect(host=app.config['DB_HOST'], database=app.config['DB_NAME'], user=app.config['DB_USER'], password=app.config['DB_PASS'], connection_factory=psycopg2.extras.RealDictConnection)
  cur = conn.cursor()
  with app.open_resource('schema.sql', mode='r') as f:
    cur.execute(f.read())
  conn.commit()
  conn.close()
  return "Nothing broken yet!"

@app.route('/seed')
def seed_db():
  conn = psycopg2.connect(host=app.config['DB_HOST'], database=app.config['DB_NAME'], user=app.config['DB_USER'], password=app.config['DB_PASS'], connection_factory=psycopg2.extras.RealDictConnection)
  cur = conn.cursor()
  with app.open_resource('seed.sql', mode='r') as f:
    cur.execute(f.read())
  conn.commit()
  conn.close()
  return "We're still good!"

@app.route('/drop')
def drop_schema():
  conn = psycopg2.connect(host=app.config['DB_HOST'], database=app.config['DB_NAME'], user=app.config['DB_USER'], password=app.config['DB_PASS'], connection_factory=psycopg2.extras.RealDictConnection)
  cur = conn.cursor()
  with app.open_resource('drop_schema.sql', mode='r') as f:
    cur.execute(f.read())
  conn.commit()
  conn.close()
  return "No more DB Data!"

@app.route('/sets')
def sets():
  conn = psycopg2.connect(host=app.config['DB_HOST'], database=app.config['DB_NAME'], user=app.config['DB_USER'], password=app.config['DB_PASS'], connection_factory=psycopg2.extras.RealDictConnection)
  cur = conn.cursor()
  cur.execute("SELECT * FROM deck_sets")
  sets = cur.fetchall()
  conn.close()
  return str(sets)

@app.route("/coffee")
def coffee():
  abort(418)

@app.errorhandler(418)
def am_teapot(error):
  return render_template("teapot.html"), 418

if __name__ == "__main__":
  app.run()
