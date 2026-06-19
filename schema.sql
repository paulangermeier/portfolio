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