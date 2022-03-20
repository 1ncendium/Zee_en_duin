import sqlite3

# <!------- Begin login function --------!>

def login(gebruikersnaam, wachtwoord):
    Gebruikersnaam = gebruikersnaam
    Wachtwoord = wachtwoord
    db = sqlite3.connect("bungelow.db")
    cursor = db.cursor()
    statement = f"Select gebruikersnaam FROM gast WHERE gebruikersnaam=? and wachtwoord=?;"
    cursor.execute(statement, [Gebruikersnaam, Wachtwoord])
    if not cursor.fetchone():
        return True
    else:
        return False

# <!------- End login function --------!>