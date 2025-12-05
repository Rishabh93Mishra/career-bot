import mysql.connector

def get_db():
    return mysql.connector.connect(
        host="bd27lkuu8i4kogikfal-mysql.services.clever-cloud.com",
        user="uvwbazynwmacmo0ji",
        password="Ee8SNwtphk1RZGlxVySW",
        database="bd27lkuu8i4kogikfal",
        port=3306
    )
