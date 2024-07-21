import random as rd
import string
import mysql.connector as sql
import datetime

def random_generate(size=6, chars=string.ascii_uppercase + string.digits+string.ascii_lowercase):
    return ''.join(rd.choice(chars) for _ in range(size))

def connect():
    conn = sql.connect(
        host="localhost",
        username="root",
        password = "luthfiku12345",
        database = "project_db"
    )
    return conn
def inserting(query):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

def generate_id(table):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("select count(*) from {}".format(table))
    id_count = cursor.fetchone()[0]
    id_count += 1
    id_len = len(str(id_count))
    txt = "T0"
    id_gen = (txt[:1] + str(id_count))
    return id_gen
def get_user_id():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("select id_user from user")
    data = cursor.fetchall()
    return data


def tugas_ins():
    date = datetime.datetime.now() 
    data = get_user_id()
    f = open("tugas_crud.txt","w")
    for i in range(0,100):
        id_user= rd.choice(data)
        id_tugas = generate_id(table="tugas")
        nama_tugas= random_generate()
        deskripsi = random_generate()
        kategori = random_generate()
        prioritas = rd.choice(["high","mid","low"])
        date += datetime.timedelta(days=1)
        query = "call sp_tambah_tugas('{}','{}','{}','{}','{}','{}','{}')".format(id_tugas,nama_tugas,deskripsi,kategori,prioritas,date,id_user[0])
        #inserting(query)
        print(query+";")
        f.write(query+";\n")
    f.close()

def goal_ins():
    date = datetime.datetime.now() 
    data = get_user_id()
    for i in range(0,100):
        id_user= rd.choice(data)
        id_tugas = generate_id(table="tugas")
        nama_tugas= random_generate()
        deskripsi = random_generate()
        kategori = random_generate()
        prioritas = rd.choice(["high","mid","low"])
        date += datetime.timedelta(days=1)
        query = "call sp_tambah_tugas('{}','{}','{}','{}','{}','{}','{}')".format(id_tugas,nama_tugas,deskripsi,kategori,prioritas,date,id_user)
        #inserting(query)
        print(query+";")
    pass

tugas_ins()
