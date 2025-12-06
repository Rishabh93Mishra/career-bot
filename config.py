import mysql.connector

def get_db():
    return mysql.connector.connect(
        host="bdz27lkwu8ik0qoikfal-mysql.services.clever-cloud.com",
        user="uvubwzynwacmo0ji",
        password="Ee8SNwtphk1RZGlxVySW",
        database="bdz27lkwu8ik0qoikfal",
        port=3306
    )
