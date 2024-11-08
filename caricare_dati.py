import mysql.connector

# Funzione per connettersi al database
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Animali"
    )

# Dati degli animali da inserire
uccelli = [
    ("Passero", "Passeridae", 14, "Urbano", "Semi, Insetti"),
    ("Merlo", "Turdidae", 34, "Boschi", "Insetti, Frutti"),
    ("Civetta", "Strigidae", 65, "Boschi", "Piccoli mammiferi"),
    ("Picchio", "Picidae", 40, "Boschi", "Insetti"),
    ("Gabbiano", "Laridae", 120, "Coste", "Pesce"),
    ("Rondine", "Hirundinidae", 35, "Aree aperte", "Insetti"),
    ("Cuculo", "Cuculidae", 34, "Boschi", "Insetti, Uova di altri uccelli"),
    ("Gufo", "Strigidae", 90, "Boschi", "Piccoli mammiferi"),
    ("Cigno", "Anatidae", 240, "Laghi", "Piante acquatiche")
]

# Connessione al database e inserimento degli animali
mydb = connect_to_db()
mycursor = mydb.cursor()

sql = "INSERT INTO Uccelli (Nome_Comune, famiglia, Apertura_Alare, Habitat, Alimentazione) VALUES (%s, %s, %s, %s,%s)"
mycursor.executemany(sql, uccelli)
mydb.commit()