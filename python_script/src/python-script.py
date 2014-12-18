#!/usr/bin/python
from jenkinsapi.jenkins import Jenkins
from jenkins_db import *
import time
import argparse

def main(args):
    jsrv = Jenkins(args.srv, args.usr , args.pwd )
    jjobs = Jenkins_Jobs(args.db)
    jjobs.table_create()

    while true:
        #Store all jenkins jobs in local database
        for j in jsrv.get_jobs():
            job_instance = server.get_job(j[0])
            jjobs.store_job( 
                    Jenkins_Job( job_instance.name , job_instance.is_running() )
                    )
        print(jjobs)
        time.sleep( pool_period )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Seedstars Challenge - Python app")
    parser.add_argument("-srv", metavar='--server', type=str,
            help="Jenkins server address")
    parser.add_argument("-usr", metavar='--user', type=str,
            help="Jenkins server Authentication Username")
    parser.add_argument("-pwd", metavar='--password', type=str,
            help="Jenkins server Authentication Password")
    parser.add_argument("-db", metavar='--database', type=str,
            help="Database location", default="jenkins_db.db")
    parser.add_argument("-pp", metavar='--poolingperiod', type=int,
            help="Pooling period in seconds", default=5)

    args = parser.parse_args()
    print("""Program arguments:
            \tServer Address = {0}
            \tServer Username = {1}
            \tServer Password = {2}
            \tDatabase Location = {3}
            \tPooling period = {4}""".format(
                args.srv,
                args.usr,
                args.pwd,
                args.db,
                args.pp)
            )
    main(args)
