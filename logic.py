import sqlite3
from config import DATABASE

class DB_Manager:

    def __init__(self, database):
        self.database = database

    def create_tables(self):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS status (
                    status_id INTEGER PRIMARY KEY,
                    status_name TEXT
                )
            """)

            conn.execute("""
                CREATE TABLE IF NOT EXISTS skills (
                    skill_id INTEGER PRIMARY KEY,
                    skill_name TEXT
                )
            """)

            conn.execute("""
                CREATE TABLE IF NOT EXISTS projects (
                    project_id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    project_name TEXT,
                    description TEXT,
                    url TEXT,
                    status_id INTEGER,

                    FOREIGN KEY (status_id)
                        REFERENCES status(status_id)
                )
            """)

            conn.execute("""
                CREATE TABLE IF NOT EXISTS project_skills (
                    project_id INTEGER,
                    skill_id INTEGER,

                    PRIMARY KEY (project_id, skill_id),

                    FOREIGN KEY (project_id)
                        REFERENCES projects(project_id),

                    FOREIGN KEY (skill_id)
                        REFERENCES skills(skill_id)
                )
            """)

        conn.close()

if __name__ == "__main__":
    db_manager = DB_Manager(DATABASE)
    db_manager.create_tables()
