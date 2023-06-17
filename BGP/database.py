import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

def persons(db, cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS persons (
                        idP INTEGER PRIMARY KEY,
                        fName TEXT NOT NULL,
                        sName TEXT NOT NULL,
                        age INT NOT NULL );""")
    person = [
        ('Jan', 'Nowak', 2),
        ('Karol', 'Kowalski', 21),
        ('Stas', 'Kaminski', 44),
        ('Stefan', 'Zielski', 60),
        ('Grzes', 'Wozniak', 40)
    ]

    cursor.executemany("REPLACE INTO persons (fName, sName, age) VALUES (?,?,?)", person)
    conn.commit()


def moves(db, cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS moves (
                        idM INTEGER PRIMARY KEY,
                        idP INTEGER NOT NULL, 
                        name TEXT NOT NULL,
                        link TEXT NOT NULL );""")
    moves = [
        (2, 'Luis Fonsi - Despacito ft. Daddy Yankee', 'https://www.youtube.com/watch?v=kJQP7kiw5Fk&t=1s'),
        (3, 'Baby Shark Dance | #babyshark Most Viewed Video | Animal Songs | PINKFONG Songs for Children0', 'https://www.youtube.com/watch?v=XqZsoesa55w&t=13s'),
        (1, 'Ed Sheeran - Shape of You (Official Music Video)', 'https://www.youtube.com/watch?v=JGwWNGJdvx8'),
        (1, 'Wiz Khalifa - See You Again ft. Charlie Puth [Official Video] Furious 7 Soundtrack', 'https://www.youtube.com/watch?v=RgKAFK5djSk'),
        (4, 'Mark Ronson - Uptown Funk (Official Video) ft. Bruno Mars', 'https://www.youtube.com/watch?v=OPf0YbXqDm0')
    ]

    cursor.executemany("REPLACE INTO moves (idP, name, link) VALUES (?,?,?)", moves)
    conn.commit()

def combined_table(db, cursor):
    cursor.execute(""" CREATE TABLE IF NOT EXISTS combined_table AS SELECT * FROM persons JOIN moves WHERE persons.idP = moves.idP; """)
    conn.commit()


def dodatek(db, cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS ene (
                        idP INTEGER PRIMARY KEY,
                        fName TEXT,
                        sName TEXT   );""")
    dodateks = [
        ('Jan', 'Nowak'),
        ('Karol', 'Kowalski'),
        ('Stas', 'Kaminski'),
        ('Stefan', 'Zielski'),
        ('Grzes', 'Wozniak')
    ]

    cursor.execute("REPLACE INTO dodatek (fName, sName) VALUES (?,?)", dodateks)
    conn.commit()
