root = './SimpleDB'
structureNewDatabase = 'tables/'

def create_database(nameNewDatabase):
    import os    
    os.makedirs(f'{root}/database/{nameNewDatabase}/{structureNewDatabase}')  
          
def create_table(use, nameNewTable, table=dict()):
    import json
    with open(f'{root}/database/{use}/tables/{nameNewTable}.json', 'w', encoding='utf-8') as tableFile:
        json.dump(table, tableFile, indent=4)
        	
def insert_in_to(use, tableName, id, insert):
    import json

    with open(f'{root}/database/{use}/tables/{tableName}.json', 'r', encoding='utf-8') as tableFile:
        data = json.load(tableFile)
        data[id] = insert
    
    with open(f'{root}/database/{use}/tables/{tableName}.json', 'w', encoding='utf-8') as tableFile:
        json.dump(data, tableFile, indent=4)

def drop_database(name):
    import shutil, os
    
    os.rmtree(f'{root}/database/{name}')

def drop_table(use, name):
    import shutil, os

    os.rmtree(f'{root}/database/{use}/tables/{name}')

def drop_column(use, tableName, id):
    import json

    with open(f'{root}/database/{use}/tables/{tableName}.json', 'r', encoding='utf-8') as tableFile:
        data = json.load(tableFile)
        data.pop(id)
    
    with open(f'{root}/database/{use}/tables/{tableName}.json', 'w', encoding='utf-8') as tableFile:
        json.dump(data, tableFile, indent=4)

