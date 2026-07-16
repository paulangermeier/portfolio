import sqlite3

projects = [
    {
        "slug": "portfolio",
        "title": "Portfolio Website",
        "year": 2026,
        "short_description": "Datenbankgetriebene Portfolio-Plattform, gebaut, um meine Software-Projekte zu präsentieren und mit ihnen zu wachsen. Entstanden als CS50-Abschlussprojekt.",
        "long_description": """Diese Website ist mein Abschlussprojekt für Harvards 
        <a href="https://cs50.harvard.edu/x/" class="link-underline" target="_blank" rel="noopener">CS50</a> und zugleich die Plattform, 
        auf der meine künftigen Software-Projekte präsentiert werden sollen. Sie ist vollständig selbst entwickelt: 
        <a href="https://flask.palletsprojects.com/en/stable/" class="link-underline" target="_blank" rel="noopener">Flask</a> und 
        <a href="https://sqlite.org/" class="link-underline" target="_blank" rel="noopener">SQLite</a> im Backend, 
        <a href="https://jinja.palletsprojects.com/en/stable/" class="link-underline" target="_blank" rel="noopener">Jinja2</a>-Templates, handgeschriebenes 
        CSS und HTML im Frontend. Alle Inhalte kommen aus der Datenbank, sodass die Seite mit jedem neuen Projekt wächst, ohne dass sich an der Struktur etwas ändert.""",
        "tech_stack": "Python, Flask, SQLite, Jinja2, HTML, CSS",
        "github_url": "https://github.com/paulangermeier/portfolio",
        "image_path": "images/portfolio-screenshot.webp",
        "featured": 1
    }
]

contents = [
    {
        "slug": "portfolio",
        "position": 1,
        "heading": "Motivation",
        "content": """Diese Website ist als Abschlussprojekt des Harvard-Kurses CS50 „Introduction to Computer Science" entstanden und markiert den Startpunkt meiner Reise als Software-Entwickler.  
        Der Wunsch, in die Software-Entwicklung einzusteigen, begleitet mich schon seit meiner Studienzeit und so war CS50 der erste und entscheidende Schritt. 
        Schnell war klar, dass ich einen Ort brauche, an dem ich meine Projekte öffentlich zeigen und erklären kann: sei es zur Akquise weiterer Projekte oder um bei Recruitern Aufmerksamkeit zu wecken. 
        Das langfristige Ziel ist ein eigenes, gebootstrapptes Software-Produkt — und diese Seite dokumentiert den Weg dorthin.""",
        "image_path": None
    },
    {
        "slug": "portfolio",
        "position": 2,
        "heading": "Architektur & Tech Stack",
        "content": """<p>Das Backend basiert auf Flask. 
        Ich habe bewusst ein Micro-Framework statt eines Full-Stack-Frameworks wie Django gewählt, um jede Schicht selbst aufzubauen und zu verstehen: Routing, Datenbankzugriff, Templating. 
        Ein Framework, das diese Arbeit versteckt, hätte dem Lernziel widersprochen.</p>
        <p>Als Datenbank kommt SQLite zum Einsatz, angebunden über Pythons natives sqlite3-Modul. 
        Für eine Portfolio-Seite mit reinem Lese-Traffic ist eine dateibasierte Datenbank die passende Wahl. 
        Kein Server, keine Konfiguration, keine Abhängigkeiten. Alle Queries sind parameterisiert, um SQL-Injection strukturell auszuschließen.</p>
        <p>Das Datenmodell besteht aus zwei Tabellen (wie aus der untenstehenden Abbildung ersichtlich ist): projects hält die einheitlichen Metadaten jedes Projekts, sections die frei strukturierbaren Inhalte der Detailseiten. 
        Die beiden Tabellen sind durch eine 1:n-Beziehung verknüpft. 
        Ein Projekt kann damit beliebig viele Abschnitte haben oder gar keine. 
        Neue Projekte und neue Inhalte entstehen so allein durch neue Datenbankeinträge, ohne dass sich an Templates oder Struktur etwas ändert.</p>""",
        "image_path": "images/er-diagram.svg"
    },
    {
        "slug": "portfolio",
        "position": 3,
        "heading": "Designsystem",
        "content": """<p>Das Design folgt einem einfachen Prinzip: Der Inhalt steht im Vordergrund, alles andere tritt zurück. 
        Eine monochromatische Palette auf dunklem Grund, großzügiger Whitespace, und eine klare visuelle Hierarchie ersetzen dekorative Elemente. 
        Jedes Gestaltungsmittel muss eine Funktion erfüllen und was keine hat, fliegt raus.</p>
        <p>Technisch ist das Designsystem über CSS Custom Properties aufgebaut: Farben, Schriften und Abstände sind als zentrale Tokens definiert, auf die alle Komponenten zugreifen. 
        Eine Änderung an einer Stelle wirkt konsistent auf der gesamten Seite, was demselben Prinzip wie beim Datenmodell entspricht, nur auf Gestaltungsebene.</p>
        <p>Bei der Typografie kombiniere ich IBM Plex Sans für Fließtext und IBM Plex Mono für Überschriften und technische Elemente. 
        Beide Schriften sind aus Datenschutzgründen und für volle Kontrolle über das Ladeverhalten self-hosted eingebunden. 
        Interaktive Elemente geben dezentes Feedback durch unterstreichende Hover-Effekte, die nicht ablenken.</p>""",
        "image_path": None
    },
    {
        "slug": "portfolio",
        "position": 4,
        "heading": "Ausblick",
        "content": """<p>Diese Seite ist bewusst als Anfang gebaut, nicht als Abschluss. 
        Das Datenmodell ist darauf ausgelegt, mit jedem neuen Projekt zu wachsen, und genau das ist der Plan: Jedes Software-Projekt auf dem Weg zum eigenen Produkt wird hier dokumentiert.</p>
        <p>Konkret geplant sind für diese Website als nächste Schritte ein geschützter Admin-Bereich, über den ich Inhalte direkt pflegen kann statt über Seed-Skripte, sowie kleinere Verbesserungen bei Barrierefreiheit und Bildverwaltung.</p>
        <p>Größere Ideen und nächste Projekte lasse ich zum jetzigen Zeitpunkt bewusst offen.</p>
        <p>Das Ziel dahinter bleibt dasselbe wie am Anfang beschrieben. Ein eigenes, gebootstrapptes Software-Produkt. Diese Seite wird zeigen, wie weit der Weg dorthin schon ist.</p>""",
        "image_path": None  
    }
]

# create connection to the database
con = sqlite3.connect("portfolio.db")

# activate foreign key enforcement since SQLite has it siabled by default
con.execute("PRAGMA foreign_keys = ON")

# create schema for db
with open("schema.sql") as f:
    schema = f.read()

con.executescript(schema)

# create a database cursor
cur = con.cursor()

# create dict to store ids from DB with slug from project to correctly map contents
slug_id = {}

# execute SQL Query to INSERT projects while storing ids of projects from DB with slugs from projects
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
                content,
                image_path
                )
                VALUES (
                ?,
                ?,
                ?,
                ?,
                ?
                )""",
                (slug_id[section["slug"]],
                section["position"],
                section["heading"],
                section["content"],
                section["image_path"])
                )

# commit the transaction to save changes
con.commit()

# verify that the rows were inserted by printing rows to the terminal
for row in cur.execute("SELECT * FROM projects INNER JOIN sections ON projects.id=sections.project_id ORDER BY projects.id"):
    print(row)

con.close()