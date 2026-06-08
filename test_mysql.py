from app.database.mysql import engine

try:
    # Membuka koneksi ke MySQL
    connection = engine.connect()

    print("MySQL Connected!")

    # Menutup koneksi
    connection.close()

except Exception as e:
    print("Connection Failed")
    print(e)