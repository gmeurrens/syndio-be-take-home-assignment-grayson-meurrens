import sqlite3
from flask import jsonify

def db_connect():
    conn = sqlite3.connect('employees.db')
    conn.row_factory = sqlite3.Row
    return conn

def calculate_pvalue():
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(id) FROM employees')
    result = cursor.fetchone()
    conn.close()
    
    return result[0]