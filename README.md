# Mantic-data

Repository to stock and share my code to create a database containing all the current maires in france, 
with details that include their firstname, surname, political party etc. 

This Repository also contains the different methods used to determine each maire's political party.

To create the table, run the "creation_table_maire.py" file.

To fill the table with 3 web pages about each maire, run the "fill_table.py" file. !!! THIS FILE TAKES HOURS AND HOURS TO RUN  !!!

Another option is to first fill the table with the political parties of maires that have it on wikipedia, and then run the scrapping for the other maires only. To do this, first run "wiki_parties.py" and then "wiki_scrapping.py" after having created the table. This methode still bugs and the two files are not yet compatible.


