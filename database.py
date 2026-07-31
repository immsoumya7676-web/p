import sqlite3
from datetime import datetime

DB_NAME = "packsecure.db"


def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inspections(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        date TEXT,

        product TEXT,

        mfg TEXT,

        exp TEXT,

        batch TEXT,

        mrp TEXT,

        confidence REAL,

        risk INTEGER,

        status TEXT,

        reason TEXT

    )
    """)

    conn.commit()
    conn.close()


def insert_record(data):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO inspections(

        date,
        product,
        mfg,
        exp,
        batch,
        mrp,
        confidence,
        risk,
        status,
        reason

    )

    VALUES(?,?,?,?,?,?,?,?,?,?)

    """,

    (

    datetime.now().strftime("%d-%m-%Y %H:%M"),

    data.get("product","Unknown"),

    data.get("Manufacturing Date","-"),

    data.get("Expiry Date","-"),

    data.get("Batch Number","-"),

    data.get("MRP","-"),

    data.get("Confidence",0),

    data.get("risk",0),

    data.get("status","Unknown"),

    data.get("reason","-")

    )

    )

    conn.commit()

    conn.close()


def get_all_records():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""

    SELECT * FROM inspections

    ORDER BY id DESC

    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def delete_all_records():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("DELETE FROM inspections")

    conn.commit()

    conn.close()
