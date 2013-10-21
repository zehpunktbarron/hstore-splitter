hstore-splitter
==========

This straigth forward script splits a postgres table-column with tags in the hstore format into single columns. You may use it if you want have OSM date stored in a postgres database and want to export the data to a shapefile. Shapes do not support hstore and require a column for each indivudal OSM key
. As shapes are limited in the amount of columns only the 245 most common keys are taken into account.

Database connection parameters need to be adjusted manually within the code in line 12.

Run the script from your linux terminal as follows:
python split_hstore.py
