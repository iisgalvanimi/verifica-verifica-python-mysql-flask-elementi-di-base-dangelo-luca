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


@app.route('/api/aggiungi/uccelli', methods=['POST'])
def add_uccelli():
    data = request.get_json()  # Recupera i dati JSON inviati dal client

    if not all(key in data for key in ('Nome_Comune', 'famiglia', 'Apertura_Alare', 'Habitat', 'Alimentazione')):
        return jsonify({"error": "Dati mancanti"}), 400

    nome = data['Nome_Comune']
    famiglia = data['famiglia']
    apertura_alare = data['Apertura_Alare']
    habitat = data['Habitat']
    alimentazione = data['Alimentazione']

    try:
        
        mydb = connect_to_db()
        mycursor = mydb.cursor()

        
        sql = "INSERT INTO Uccelli (Nome_Comune, famiglia, Apertura_Alare, Habitat, Alimentazione) VALUES (%s, %s, %s, %s, %s)"
        values = (nome, famiglia, apertura_alare, habitat, alimentazione)
        
        
        mycursor.execute(sql, values)
        mydb.commit()

        mycursor.close()
        mydb.close()

        return jsonify({"message": "Animale inserito con successo!"}), 201
    
    except mysql.connector.Error as err:
        return jsonify({"error": f"Errore nel database: {err}"}), 500



@app.route('/api/delete/uccelli/<int:id>', methods=['DELETE'])
def delete_ucelli(id):
    mydb = connect_to_db()
    mycursor = mydb.cursor()

    # Verifica se l'animale con questo id esiste
    mycursor.execute("SELECT * FROM Uccelli WHERE Id = %s", (id,))
    if not mycursor.fetchone():
        mycursor.close()
        mydb.close()
        return jsonify({"message": "Animale non trovato"}), 404

    # Esegue l'operazione di DELETE
    sql = "DELETE FROM Uccelli WHERE Id = %s"
    mycursor.execute(sql, (id,))
    mydb.commit()

    mycursor.close()
    mydb.close()

    return jsonify({"message": "Animale eliminato con successo!"}), 200

@app.route('/api/update/uccelli/<int:id>', methods=['PUT'])
def update_uccelli(id):
    data = request.get_json()

    # Verifica che tutti i campi necessari siano presenti
    if not all(key in data for key in ('Nome_Comune', 'famiglia', 'Apertura_Alare', 'Habitat','Alimentazione')):
        return jsonify({"error": "Dati mancanti"}), 400

    nome = data['Nome_Comune']
    famiglia = data['famiglia']
    apertura_alare = data['Apertura_Alare']
    habitat = data['Habitat']
    alimentazione = data['Alimentazione']

    # Connessione al database e aggiornamento dei dati
    mydb = connect_to_db()
    mycursor = mydb.cursor()

    sql = "UPDATE Uccelli SET Nome_Comune = %s, famiglia = %s, Apertura_Alare = %s, Habitat = %s, Alimentazione = %s WHERE Id = %s"
    values = (nome, famiglia, apertura_alare, habitat,alimentazione, id)
    mycursor.execute(sql, values)
    mydb.commit()

    mycursor.close()
    mydb.close()

    # Controlla se l'update ha modificato delle righe
    if mycursor.rowcount == 0:
        return jsonify({"message": "Animale non trovato"}), 404

    return jsonify({"message": "Animale aggiornato con successo!"}), 200


if __name__ == '__main__':
    app.run(debug=True)