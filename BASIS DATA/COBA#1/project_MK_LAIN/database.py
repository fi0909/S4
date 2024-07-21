import mysql.connector
from mysql.connector import Error
from datetime import datetime

class Database:
    # Static variables to store database details
    host = 'localhost'
    database = 'project_lol'
    user = 'root'
    password = 'luthfiku12345'

    @staticmethod
    def check_credentials(username, password):
        try:
            connection = mysql.connector.connect(host=Database.host,
                                                 database=Database.database,
                                                 user=Database.user,
                                                 password=Database.password)
            if connection.is_connected():
                cursor = connection.cursor(dictionary=True)
                query = "SELECT * FROM users WHERE username = %s AND password = %s"
                cursor.execute(query, (username, password))
                user = cursor.fetchone()
                cursor.close()
                connection.close()
                if user:
                    return True
                else:
                    return False
        except Error as e:
            print("Error while connecting to MySQL", e)
            return False

    @staticmethod
    def register(username, password):
        try:
            connection = mysql.connector.connect(host=Database.host,
                                                 database=Database.database,
                                                 user=Database.user,
                                                 password=Database.password)
            if connection.is_connected():
                cursor = connection.cursor()
                # Check if username already exists
                cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
                existing_user = cursor.fetchone()
                if existing_user:
                    return False
                else:
                    # If username does not exist, perform registration
                    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
                    cursor.execute(query, (username, password))
                    connection.commit()
                    cursor.close()
                    connection.close()
                    return True
        except Error as e:
            print("Error while connecting to MySQL", e)
            return False
        
    @staticmethod
    def get_laptops():
        try:
            connection = mysql.connector.connect(host=Database.host,
                                                 database=Database.database,
                                                 user=Database.user,
                                                 password=Database.password)
            if connection.is_connected():
                cursor = connection.cursor()
                query = "SELECT * FROM list_laptop"
                cursor.execute(query)
                data = cursor.fetchall()
                cursor.close()
                connection.close()
                return data
        except mysql.connector.Error as e:
            print("Error while connecting to MySQL", e)
            return None
        
    @staticmethod
    def add_laptop(kode_laptop, jenis_laptop, harga_sewa):
        # Tambahkan laptop ke database
        try:
            connection = mysql.connector.connect(host=Database.host,
                                                 database=Database.database,
                                                 user=Database.user,
                                                 password=Database.password)
            if connection.is_connected():
                cursor = connection.cursor()
                query = "INSERT INTO list_laptop (kode_laptop, jenis_laptop, harga_sewa) VALUES (%s, %s, %s)"
                cursor.execute(query, (kode_laptop, jenis_laptop, harga_sewa))
                connection.commit()
                cursor.close()
                connection.close()
                return True
        except mysql.connector.Error as e:
            print("Error while connecting to MySQL", e)
            return False
    
    @staticmethod
    def delete_laptop(kode_laptop):
        # Hapus laptop dari database
        try:
            connection = mysql.connector.connect(host=Database.host,
                                                 database=Database.database,
                                                 user=Database.user,
                                                 password=Database.password)
            if connection.is_connected():
                cursor = connection.cursor()
                query = "DELETE FROM list_laptop WHERE kode_laptop = %s"
                cursor.execute(query, (kode_laptop,))
                connection.commit()
                cursor.close()
                connection.close()
                return True
        except mysql.connector.Error as e:
            print("Error while connecting to MySQL", e)
            return False
        
    @staticmethod
    def get_kode():
        try:
            connection = mysql.connector.connect(host=Database.host,
                                                 database=Database.database,
                                                 user=Database.user,
                                                 password=Database.password)
            if connection.is_connected():
                cursor = connection.cursor()
                query = "SELECT kode_laptop FROM list_laptop"
                cursor.execute(query)
                data = cursor.fetchall()
                cursor.close()
                connection.close()
                return data
        except mysql.connector.Error as e:
            print("Error while connecting to MySQL", e)
            return None
        
    @staticmethod
    def get_jenis(selected_kode):
        try:
            connection = mysql.connector.connect(host=Database.host,
                                                database=Database.database,
                                                user=Database.user,
                                                password=Database.password)
            if connection.is_connected():
                cursor = connection.cursor()
                # Construct SQL query to select laptop type based on selected code
                query = "SELECT jenis_laptop FROM list_laptop WHERE kode_laptop = %s"
                cursor.execute(query, (selected_kode,))
                laptop_type = cursor.fetchone()[0]  # Fetch the first row and extract laptop type
                cursor.close()
                connection.close()
                return laptop_type
        except mysql.connector.Error as e:
            print("Error while connecting to MySQL", e)
            return None
        
    @staticmethod
    def get_harga(selected_kode):
        try:
            connection = mysql.connector.connect(host=Database.host,
                                                database=Database.database,
                                                user=Database.user,
                                                password=Database.password)
            if connection.is_connected():
                cursor = connection.cursor()
                # Construct SQL query to select laptop type based on selected code
                query = "SELECT harga_sewa FROM list_laptop WHERE kode_laptop = %s"
                cursor.execute(query, (selected_kode,))
                harga_sewa = cursor.fetchone()[0]  # Fetch the first row and extract laptop type
                cursor.close()
                connection.close()
                return harga_sewa
        except mysql.connector.Error as e:
            print("Error while connecting to MySQL", e)
            return None
    
    @staticmethod
    def get_list():
        try:
            connection = mysql.connector.connect(host=Database.host,
                                                database=Database.database,
                                                user=Database.user,
                                                password=Database.password)
            if connection.is_connected():
                cursor = connection.cursor()
                # Construct SQL query to select laptop type based on selected code
                query = "SELECT id_sewa, kode_laptop, jenis_laptop, harga_sewa, jam_mulai, created_at FROM sewa_laptop WHERE jam_akhir is null"
                cursor.execute(query)
                data = cursor.fetchall()  # Fetch the first row and extract laptop type
                cursor.close()
                connection.close()
                return data
        except mysql.connector.Error as e:
            print("Error while connecting to MySQL", e)
            return None
    
    @staticmethod
    def sewa_laptop(kode_laptop, jenis_laptop, harga_sewa):
        now = datetime.now()
        time = now.strftime("%H:%M:%S") 
        try:
            connection = mysql.connector.connect(host=Database.host,
                                                database=Database.database,
                                                user=Database.user,
                                                password=Database.password)
            if connection.is_connected():
                cursor = connection.cursor()
                query = "INSERT INTO sewa_laptop(kode_laptop, jenis_laptop, harga_sewa, jam_mulai) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (kode_laptop, jenis_laptop, harga_sewa, time))
                connection.commit()
                cursor.close()
                connection.close()
                return True
        except mysql.connector.Error as e:
            print("Error while connecting to MySQL", e)
            return False

    @staticmethod
    def akhiri_sewa(kode_laptop):
        try:
            connection = mysql.connector.connect(host=Database.host,
                                                database=Database.database,
                                                user=Database.user,
                                                password=Database.password)
            if connection.is_connected():
                cursor = connection.cursor()
                # Ambil waktu mulai sewa
                query = "SELECT created_at FROM sewa_laptop WHERE kode_laptop = %s AND jam_akhir IS NULL"
                cursor.execute(query, (kode_laptop,))
                jam_mulai = cursor.fetchone()[0]
                
                # Perbarui jam akhir sewa
                query = "UPDATE sewa_laptop SET jam_akhir = NOW() WHERE kode_laptop = %s AND jam_akhir IS NULL"
                cursor.execute(query, (kode_laptop,))
                connection.commit()
                cursor.close()
                connection.close()
                
                return jam_mulai  # Kembalikan waktu mulai sewa
        except mysql.connector.Error as e:
            print("Error while connecting to MySQL", e)
            return None