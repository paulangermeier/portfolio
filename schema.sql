DROP TABLE IF EXISTS sections;
DROP TABLE IF EXISTS projects;

CREATE TABLE projects (
    id INTEGER PRIMARY KEY,
    slug TEXT NOT NULL UNIQUE,
    title TEXT NOT NULL,
    year INTEGER NOT NULL,
    short_description TEXT NOT NULL,
    long_description TEXT,
    tech_stack TEXT,
    github_url TEXT,
    image_path TEXT,
    featured INTEGER DEFAULT 0
);

CREATE TABLE sections (
	id INTEGER PRIMARY KEY,
	project_id INTEGER NOT NULL,
	position INTEGER NOT NULL,
	heading TEXT,
	content TEXT,
	image_path TEXT,
	FOREIGN KEY (project_id)
	REFERENCES projects(id)
);