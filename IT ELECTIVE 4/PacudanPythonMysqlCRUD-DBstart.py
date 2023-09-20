import mysql.connector

db = mysql.connector.connect(
    host="localhost",       #host
    user="root",            #user
    passwd="1234",          #password
    #database="cnpetstore"
)
#Run this file first!!!

c = db.cursor(prepared=True)
c.execute("CREATE DATABASE cnpetstore")
#c.execute("USE cnpetstore")
c.execute("CREATE TABLE pets(petid INT NOT NULL PRIMARY KEY AUTO_INCREMENT,petname VARCHAR(50) NOT NULL,petprice INT NOT NULL,petstock INT NOT NULL)")
c.execute("""INSERT INTO pets (petname, petprice, petstock) VALUES
            ('Bulbasaur', 480, 20),
            ('Alligator', 200, 48),
            ('Singing Chipmunks', 500, 3),
            ('John Pork', 69, 69);""")
db.commit()
