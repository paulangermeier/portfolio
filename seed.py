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
        "image_path": "portfolio/static/test.png",
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
        "image_path": "portfolio/static/test.png",
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
        "image_path": "portfolio/static/test4.png",
        "featured": 1
    }

]

# create connection to the database
con = sqlite3.connect("portfolio.db")

# create a database cursor
cur = con.cursor()

# wipe existing rows to keep this script idempotent
cur.execute("DELETE FROM projects")

# execute SQL Query to INSERT projects with executemany
cur.executemany("""INSERT INTO projects (
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
                )""", projects)

# commit the transaction to save changes
con.commit()

#verify that the rows were inserted by printing rows to the terminal
for row in cur.execute("SELECT * FROM projects ORDER BY id"):
    print(row)

con.close()