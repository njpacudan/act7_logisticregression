import mysql.connector

db = mysql.connector.connect(
    host="localhost",       #host
    user="root",            #user
    passwd="1234",          #password
    database="cnpetstore"   #db
)
c = db.cursor(prepared=True)
loop = True
while loop is True:
    print("---------------------------\nCompletely Normal Pet Store\n---------------------------")
    print("Id | Pet Name | Price | Stock\n---------------------------")
    c.execute("SELECT * FROM pets")
    total = c.fetchall()
    for i in total:
        print(i)
        
    ans = input("---------------------------\nType 1 to Sell\nType 2 to Modify Pet Stock\nType 3 to Add new Pet\nType 4 to Delete Pet\nType 5 to Exit\n :")
    match ans:
        case '1':
            ans1 = int(input("Enter Pet ID: "))
            query = "SELECT * FROM pets WHERE petid = %s"
            query2 = "SELECT petid FROM pets WHERE petid = %s"
            query3 = "SELECT petprice FROM pets WHERE petid = %s"
            query4 = "SELECT petstock FROM pets WHERE petid = %s"
            query5 = "UPDATE pets SET petstock = %s WHERE petid = %s"
            tuple1 = (ans1,)
            c.execute(query,tuple1)
            showfetch = c.fetchall()
            c.execute(query2,tuple1)
            compare = c.fetchone()
            if compare is None:
                print("The ID you entered doesn't exist!")
            else:
                print("\nId | Pet Name | Price | Stock")
                print(showfetch)
                c.execute(query3,tuple1)
                pricetot = c.fetchone()
                calcash = int(pricetot[0])
                ans2 = int(input("Enter cash: "))
                if ans2 > calcash:
                    total = ans2 - calcash
                    print("---------------------\nThis is the receipt\n---------------------\nId | Pet Name | Price | Stock\n")
                    print(showfetch)
                    print("\nPrice: ",calcash," Php\nCash: ",ans2," Php\nChange: "+str(total)+" Php\n---------------------\n")
                    c.execute(query4,tuple1)
                    cstock = c.fetchone()
                    cstock1 = cstock[0]
                    minstock = int(cstock1) - 1
                    tuple2 = (minstock, ans1)
                    c.execute(query5, tuple2)
                    db.commit()
                else:
                    print("Insufficient cash!")

        case '2':
            ans1 = int(input("Enter pet ID: "))
            query = "SELECT * FROM pets WHERE petid = %s"
            query2 = "SELECT petid FROM pets WHERE petid = %s"
            query3 = "UPDATE pets SET petstock = %s WHERE petid = %s;"
            tuple1 = (ans1,)
            c.execute(query,tuple1)
            showfetch = c.fetchall()
            c.execute(query2,tuple1)
            compare = c.fetchone()
            if compare is None:
                print("The ID you entered doesn't exist!")
            else:
                print("\nId | Pet Name | Price | Stock")
                print(showfetch)
                ans2 = input("Enter new Pet stock quantity: ")
                tuple3 = (ans2, ans1)
                c.execute(query3,tuple3)
                ds = c.fetchall()
                db.commit()
                print(ds)
                print("New Pet stock quantity recorded.")
        case '3':
            query = "INSERT INTO pets (petname, petprice, petstock) VALUES (%s,%s,%s)"
            ans1 = input("Enter new Pet Name: ")
            ans2 = input("Enter new Pet Price: ")
            ans3 = input("Enter new Pet Stock: ")
            tans = (ans1,ans2,ans3)
            c.execute(query,tans)
            db.commit()
            print("New Pet recorded.")
        case '4':
            ans1 = int(input("Enter Pet ID to DELETE: "))
            query = "SELECT * FROM pets WHERE petid = %s"
            query2 = "SELECT petid FROM pets WHERE petid = %s"
            query3 = "DELETE FROM pets WHERE petid = %s"
            tuple1 = (ans1,)
            c.execute(query,tuple1)
            showfetch = c.fetchall()
            c.execute(query2,tuple1)
            compare = c.fetchone()
            if compare is None:
                print("The ID you entered doesn't exist!")
            else:
                c.execute(query3, tuple1)
                db.commit()
                print("Pet deleted.")
        case '5':
            print("Exiting....")
            loop = False
    

