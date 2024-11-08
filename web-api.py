from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Funzione per connettersi al database
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Animali"
    )

@app.route('/api/visualizza/uccelli', methods=['GET'])
def get_uccelli():
    # Connessione al database
    mydb = connect_to_db()
    mycursor = mydb.cursor(dictionary=True)
    
    # Esecuzione della query per selezionare tutti i dati dalla tabella
    mycursor.execute("SELECT * FROM Uccelli")
    uccelli = mycursor.fetchall()
    
    # Chiusura delle connessioni
    mycursor.close()
    mydb.close()
    
    # Restituisce i dati in formato JSON
    return jsonify(uccelli)


if __name__ == '__main__':
    app.run(debug=True)