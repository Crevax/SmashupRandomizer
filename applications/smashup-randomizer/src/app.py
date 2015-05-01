from flask import abort, Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from sqlalchemy.exc import IntegrityError, ProgrammingError
from werkzeug.debug import DebuggedApplication

# configuration - will be refactored and moved later
DEBUG       = True
SECRET_KEY  ='development key'
SQLALCHEMY_DATABASE_URI = 'postgresql://smashup_user:123four@localhost/smashup_randomizer'

app = Flask(__name__)
app.config.from_object(__name__)
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class DeckSet(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True)

  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return '<Set %r>' % self.name

  def __unicode__(self):
    return '%s' % self.name

class Deck(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), unique=True)
  set_id = db.Column(db.Integer, db.ForeignKey('deck_set.id'))
  set = db.relationship('DeckSet',
    backref=db.backref('decks', lazy='dynamic'))

  def __init__(self, name, set):
    self.name = name
    self.set = set

  def __repr__(self):
    return '<Deck %r>' % self.name

  def __unicode__(self):
    return '%s' % self.name

@app.route("/")
def index():
  return render_template('index.html')

@app.route('/sets')
def sets():
  try:
    sets = DeckSet.query.all()
  except ProgrammingError:
    return "Missing database tables. Are you sure you ran migrations?", 500
  return ','.join(set.name for set in sets)

@app.route("/coffee")
def coffee():
  abort(418)

@app.errorhandler(418)
def am_teapot(error):
  return render_template("teapot.html"), 418

@manager.command
def seed_db():
  "Adds initial data to the database"
  try:
    core = DeckSet('Core')
    awe = DeckSet('Awesome Level 9000')
    cthulhu = DeckSet('The Obligatory Cthulhu Set')
    scifi = DeckSet('Science Fiction Double Feature')
    geek = DeckSet('The Big Geeky Box')
    monster = DeckSet('Monster Smash')
    pretty = DeckSet('Pretty Pretty Smash Up')
    db.session.add(core)
    db.session.add(awe)
    db.session.add(cthulhu)
    db.session.add(scifi)
    db.session.add(geek)
    db.session.add(monster)
    db.session.add(pretty)
    db.session.commit()
  except IntegrityError:
    return "Seed data already exists"
  return "We have data now"

if __name__ == "__main__":
  manager.run()
