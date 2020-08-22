import pymysql

def conecta():
    try:
        print("conectando...")
        return pymysql.connect(
            host="172.21.0.2",
            user="root",
            password="example",
            db="classicmodels"
        )
    except Exception as e:
        print(str(e))
        return False

conecta()