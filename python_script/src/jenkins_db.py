#!/usr/bin/python
import sys
import sqlite3 as lite

class Jenkins_Job:

    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __unicode__(self):
        return "{0} , {1}".format(name, status)

class Jenkins_Jobs:

    def __init__(self, db_name):
        self.db_con = lite.connect(db_name)

        try:
            with self.db_con:
                db_con.cursor().execute(
                        "CREATE TABLE jenkins_jobs(name TEXT primary key, status TEXT, last_update DEFAULT current_timestamp)") 
        except:
            pass

    def store_job(self, job):
        try:
            with self.db_con:
                db_con.cursor().execute(
                        "INSERT INTO jenkins_jobs(name,status) VALUES('?','?')",
                        (job.name, job.status) )
        except:
            with self.db_con:
                db_con.cursor().execute(
                        "UPDATE jenkins_jobs SET status = '?' WHERE name = '?'",
                        (job.status, job.name) )

    def __unicode__(self):
        ret_str = ""
        
        with self.db_con:
            for row in db_con.cursor().execute("SELECT").fetchall()
                ret_str = ret_str + row

        return ret_str
