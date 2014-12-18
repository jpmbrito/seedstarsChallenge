#!/usr/bin/python
import unittest
from jenkins_db import *

class Jenkins_Jobs_test(unittest.TestCase):

    def setUp(self):
        self.jj = Jenkins_Jobs("jenkins_jobs_test.db")
        self.jj.table_delete()
        self.jj.table_create()

    def test_store_job_create(self):
        self.jj.store_job( Jenkins_Job("JOB1", "BLOCK") )
        self.jj.store_job( Jenkins_Job("JOB2", "BLOCK") )
        print self.jj
        self.jj.store_job( Jenkins_Job("JOB1", "ACTIVE") )
        self.jj.store_job( Jenkins_Job("JOB2", "ACTIVE") )
        print self.jj #TODO - ASSERT processing
       
    def tearDown(self):
        self.jj.table_delete()
        self.jj.table_create()

if __name__ == '__main__':
    unittest.main()
