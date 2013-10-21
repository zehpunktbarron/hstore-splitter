# -*- coding: utf-8 -*-
#!/usr/bin/python2.7

#description     :This file creates a plot: Calculate the actuality of all points
#author          :Christopher Barron
#date            :19.10.2013
#version         :0.1
#usage           :python pyscript.py
#==============================================================================

import psycopg2
import numpy as np

###
### Connect to database with psycopg2. Add arguments from parser to the connection-string
###

try:
  conn_string="dbname=name user=username host=localhost password=pw"
  print "Connecting to database\n->%s" % (conn_string)
      
  conn = psycopg2.connect(conn_string)
  print "Connection to database was established succesfully"
except:
  print "Connection to database failed"

###
### Execute SQL query
###  
  
# New cursor method for sql
cur = conn.cursor()

# Grab all different Tags. Limit because a shapefile only can have 255 columns
cur.execute(" SELECT skeys(tags), count(skeys(tags)) FROM lines GROUP BY skeys(tags) ORDER BY count DESC LIMIT 245;")

rows = cur.fetchall()


for row in rows:
  print row[0]
  cur.execute(" ALTER TABLE lines ADD column \"" + row[0] + "\" text;") # Add column with every Key in the hstore has
  cur.execute(" UPDATE lines SET \"" + row[0] + "\" = tags -> '" + row[0] + "';") # Insert values for every key the road has
  conn.commit()
