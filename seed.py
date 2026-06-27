import sqlite3

projects = [
    {
        "slug": "project-xy",
        "title": "Projekt XY",
        "year": 2026,
        "short_description": "Das ist ein Test-Text für das Projekt XY für die short Description Zelle zum Testen meines seed.py Skripts.",
        "long_description": "Das ist ein Test-Text für das Projekt XY für die long Description Zelle der etwas länger ist als die short Description Zelle meines seed.py Skripts.",
        "tech_stack": "Python, Flask, Jinja, SQL, HTML, CSS",
        "github_url": "www.github.de/projekt-xy",
        "image_path": "images/test.png",
        "featured": 1
    },
    {
        "slug": "project-z",
        "title": "Projekt Z",
        "year": 2025,
        "short_description": "Das ist ein Test-Text für das Projekt Z für die short Description Zelle zum Testen meines seed.py Skripts.",
        "long_description": "Das ist ein Test-Text für das Projekt Z für die long Description Zelle der etwas länger ist als die short Description Zelle meines seed.py Skripts.",
        "tech_stack": "Python, Flask, Jinja, SQL, HTML, CSS",
        "github_url": "www.github.de/projekt-z",
        "image_path": "images/test.png",
        "featured": 0
    },
    {
        "slug": "project-a",
        "title": "Projekt A",
        "year": 2024,
        "short_description": "Das ist ein Test-Text für das Projekt A für die short Description Zelle zum Testen meines seed.py Skripts.",
        "long_description": "Das ist ein Test-Text für das Projekt A für die long Description Zelle der etwas länger ist als die short Description Zelle meines seed.py Skripts.",
        "tech_stack": "Python, Flask, Jinja, SQL, HTML, CSS",
        "github_url": "www.github.de/projekt-A",
        "image_path": "images/test4.png",
        "featured": 1
    }
]

contents = [
    {
        "slug": "project-xy",
        "position": 1,
        "heading": "Test-Überschrift",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    },
    {
        "slug": "project-xy",
        "position": 2,
        "heading": "Test-Überschrift 2",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    },
    {
        "slug": "project-xy",
        "position": 3,
        "heading": "Test-Überschrift 3",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    },
    {
        "slug": "project-z",
        "position": 1,
        "heading": "Überschrift-Test",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    },
    {
        "slug": "project-z",
        "position": 2,
        "heading": "Überschrift-Test 2",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    },
    {
        "slug": "project-z",
        "position": 3,
        "heading": "Überschrift-Test 3",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    },
    {
        "slug": "project-a",
        "position": 1,
        "heading": "Überschrift 1",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    },
    {
        "slug": "project-a",
        "position": 2,
        "heading": "Überschrift 2",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    },
    {
        "slug": "project-a",
        "position": 3,
        "heading": "Überschrift 2",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    },
]

# create connection to the database
con = sqlite3.connect("portfolio.db")

# create a database cursor
cur = con.cursor()

# wipe existing rows to keep this script idempotent
cur.execute("DELETE FROM sections")
cur.execute("DELETE FROM projects")

# create dict to store ids from DB with slug from project to correctly map contents
slug_id = {}

#execute SQL Query to INSERT projects while storing ids of projects from DB with slugs from projects
for project in projects:
    cur.execute("""INSERT INTO projects (
                slug, 
                title,
                year,
                short_description,
                long_description,
                tech_stack,
                github_url,
                image_path,
                featured
                )
                VALUES (
                :slug, 
                :title, 
                :year, 
                :short_description,
                :long_description,
                :tech_stack,
                :github_url,
                :image_path,
                :featured
                )""", project)
    project_id = cur.lastrowid
    slug_id[project["slug"]] = project_id

# execute SQL Query to INSERT contents with slug_id dict
for section in contents:
    cur.execute("""INSERT INTO sections (
                project_id,
                position,
                heading,
                content
                )
                VALUES (
                ?,
                ?,
                ?,
                ?
                )""",
                (slug_id[section["slug"]],
                section["position"],
                section["heading"],
                section["content"])
                )

# commit the transaction to save changes
con.commit()

#verify that the rows were inserted by printing rows to the terminal
for row in cur.execute("SELECT * FROM projects INNER JOIN sections ON projects.id=sections.project_id ORDER BY projects.id"):
    print(row)

con.close()