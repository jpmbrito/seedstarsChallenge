#!/usr/bin/python
import sys
import sqlite3 as lite
import traceback

class Jenkins_Job:

    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __str__(self):
        return "{0} , {1}".format(self.name, self.status)

class Jenkins_Jobs:

    def __init__(self, db_name):
        self.db_con = lite.connect(db_name)

    def table_create(self):
        try:
            with self.db_con:
                self.db_con.cursor().execute(
                        """CREATE TABLE Jenkins_Jobs(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT UNIQUE NOT NULL,
                        status TEXT,
                        last_update DATETIME DEFAULT(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW')))""")
        except:
            pass
    
    def table_delete(self):
        with self.db_con:
            self.db_con.cursor().execute(
                    "DROP TABLE IF EXISTS Jenkins_Jobs")

    def store_job(self, job):
        if self.create_job(job) is False:
            self.update_job(job)

    def create_job(self, job):
        try:
            with self.db_con:
                self.db_con.cursor().execute(
                        """INSERT INTO jenkins_jobs(name,status)
                        VALUES(?,?)""",
                        (job.name, job.status,) )
        except:
            return False;

        return True;

    def update_job(self, job):
        try:
            with self.db_con:
                self.db_con.cursor().execute(
                        """UPDATE jenkins_jobs
                        SET status = ? ,
                        last_update = STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW')
                        WHERE name = ?""",
                        (job.status, job.name,) )
        except:
            return False;
        
        return True;

    def __str__(self):
        ret_str = ""
        
        with self.db_con:
            
            for row in self.db_con.cursor().execute("""
                    SELECT * FROM jenkins_jobs""").fetchall():
                        ret_str = "{0}\n{1}".format(ret_str,row)

        return ret_str
