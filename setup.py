from sqlite3 import connect
from json import load

with open("db_credentials") as f:
    jsondata=load(f)
    con=connect(jsondata.get("dbname"))
    cor=con.cursor()
    with open("schema.sql" ) as f1:
        cor.executescript(f1.read())
    print "Data bases initialized"
    con.commit()

    cor.close()
    con.close()
