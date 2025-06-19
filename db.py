import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="card_storage",
        password="card_storage",
        database="card_storage"
    )
