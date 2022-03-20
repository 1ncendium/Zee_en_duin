import sqlite3
Gebruikersnaam = input("Gebruikersnaam: ")
Wachtwoord = input("Wachtwoord: ")
db = sqlite3.connect("bungelow.db")
cursor = db.cursor()
statement = f"Select gebruikersnaam FROM gast WHERE gebruikersnaam=? and wachtwoord=?;"
cursor.execute(statement, [Gebruikersnaam, Wachtwoord])
if not cursor.fetchone():
    print("Login failed")
else:
    print(f"Welcome {Gebruikersnaam}")