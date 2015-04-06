from flask import Flask, render_template
from werkzeug.debug import DebuggedApplication

app = Flask(__name__)
app.debug = True
app.wsgi_app = DebuggedApplication( app.wsgi_app, True )

@app.route("/")
def index():
	return render_template('index.html')

if __name__ == "__main__":
  app.run()
