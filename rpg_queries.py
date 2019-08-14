import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

query = """SELECT * 
FROM charactercreator_character 
INNER JOIN charactercreator_mage 
ON character_id = character_ptr_id;"""

curs.execute(query)
results = curs.fetchone()
remaining_results = curs.fetchall()

print(results)
print(remaining_results)

'''
How many total characters?
There are 302 characters
'''

query = """SELECT COUNT(character_id) FROM charactercreator_character;"""
curs.execute(query)
curs.fetchall()

'''
How many of each specific Subclass
'''

#Cleric
query = """SELECT COUNT(character_ptr_id) 
FROM charactercreator_cleric;"""
curs.execute(query)
curs.fetchall()

#Fighter
query = """SELECT COUNT(character_ptr_id) 
FROM charactercreator_fighter;"""
curs.execute(query)
curs.fetchall()

#Mage
query = """SELECT COUNT(character_ptr_id) 
FROM charactercreator_mage;"""
curs.execute(query)
curs.fetchall()

#Necromancer
query = """SELECT COUNT(mage_ptr_id) 
FROM charactercreator_necromancer;"""
curs.execute(query)
curs.fetchall()

#Thief
query = """SELECT COUNT(character_ptr_id) 
FROM charactercreator_thief;"""
curs.execute(query)
curs.fetchall()

'''
How many total Items?
'''

query = """SELECT COUNT(item_id)
FROM armory_item"""
curs.execute(query)
curs.fetchall()

'''
How many of the Items are weapons? How many are not?
'''

query1 = """SELECT COUNT(item_id)
FROM armory_item"""
curs.execute(query1)
curs.fetchall()

query2 = """SELECT COUNT(item_ptr_id)
FROM armory_weapon"""
curs.execute(query2)
curs.fetchall()

'''
How many Items does each character have? (Return first 20 rows)
How many weapons does each character have? (Return first 20 rows)
'''

# *****************************************************************
query = """SELECT COUNT(item_id)
FROM charactercreator_character 
INNER JOIN armory_item 
ON character_id = item_id LIMIT 20;"""
curs.execute(query)
curs.fetchall()

# ******************************************************************
query = """SELECT COUNT(item_id)
FROM charactercreator_character 
INNER JOIN armory_weapon 
ON character_id = item_id LIMIT 20;"""
curs.execute(query)
curs.fetchall()

'''
On average, how many Items does each Character have?
On average, how many weapons does each Character have?
'''

query = """SELECT AVG(item_id)
FROM armory_item"""
curs.execute(query)
curs.fetchall()

query = """SELECT AVG(item_ptr_id)
FROM armory_weapon"""
curs.execute(query)
curs.fetchall()

# Buddymove Dataset; Assignment 2

import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('buddymove_holidayiq.csv')
df.shape

# make buddymove_holidayiq.sqlite3 db
df.head()

# Create in memory SQLite db
engine = create_engine('sqlite://', echo=False)

df.to_sql('buddymove_holidayiq', con=engine)
engine.execute("SELECT * FROM buddymove_holidayiq").fetchall()