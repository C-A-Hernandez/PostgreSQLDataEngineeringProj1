# PostgreSQLDataEngineeringProj1
The purpose of the Postgres database in the context of the startup (Sparkify) and the analytical goals
of the startup is to optimize queries based on song play analysis.

The database schema involves a star schema with a fact table named songplays, and four dimension tables 
named users, songs, artists, and time.  The star schema is selected as the type of schema due to its 
simplicity and facilitating query simplification rather than complex joins that occur with other types of schemas.

The extract transform and load (ETL) pipeline involves first importing the following (os, glob, psychopg2, and 
pandas as pd from sql_queries). Second, defining the process_song_file by opening the song file and inserting 
records into the song table; then inserting records into the artist table.  Third, defining the process_log_file 
by opening the log file, filtering by NextSong action, converting timestamp column to datetime, inserting time data 
records into time table, loading user table, inserting user records, inserting songplay records, getting songid and 
artist id from song and artist tables, and inserting songplay records into the songplay table.  Fourth, the processing 
of the data was defined in order to get all files matching extension from directory, to print total number of files found, 
and to iterate over files and process.  

The foregoing ETL pipeline was used to transfer data from log_data and song_data files that were in .json format in two 
local directories into the tables that are in the star schema in Postgres using Python and SQL.

