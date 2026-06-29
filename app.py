from datetime import datetime
from flask import Flask, render_template, g, abort
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

    # transform rel_projects row objects into a list of dicts each with a split tech_list
    # tech_stack is stored as comma separated string in the DB
    projects = []
    for project in rel_projects:
        # row object is read only, convert to dict so tech_list can be added
        p = dict(project)
        # list comprehension that creates a new key-value pair in p with separated tech_stack values
        p["tech_list"] = [t.strip() for t in p["tech_stack"].split(",")]
        # append the dict stored in p to projects to create a list of dicts
        projects.append(p)

    return render_template("index.html", current_year=current_year, projects=projects)

@app.route("/projects/<slug>")
def project_details(slug):
    
    # create db cursor
    cur = get_db().cursor()

    # query to get data for project from DB
    project = cur.execute(
        "SELECT * FROM projects WHERE slug = ?", (slug,)
        ).fetchone()

    # if project is empty send error message
    if project is None:
        abort(404)

    # query to get data for content from DB
    content = cur.execute(
        "SELECT * FROM sections WHERE project_id = ? ORDER BY position", (project["id"],)
    ).fetchall()

    return render_template("project_detail.html", project=project, content=content)

@app.route("/projects")
def projects():
    return render_template("projects.html")