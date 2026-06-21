from datetime import datetime
from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)

DATABASE = 'portfolio.db'

# function for creating a db connection
def get_db():
    # checking if a connection to the db is already there
    db = getattr(g, '_database', None)
    if db is None:
        # if no connection is there create db connection
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

# route/ function to close the db connection
@app.teardown_appcontext
def close_connection(exception):
    # checking if a connection to the db is there
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    # importing current year for copyright
    current_year = datetime.now().year

    # create a db cursor 
    cur = get_db().cursor()

    # Querying DB to store the relevant projects for index.html as a list of row objects (dicts)
    rel_projects = cur.execute(
        "SELECT * FROM projects WHERE featured = 1"
    ).fetchall()

    print(rel_projects[0]["title"])

    return render_template("index.html", current_year=current_year, rel_projects=rel_projects)