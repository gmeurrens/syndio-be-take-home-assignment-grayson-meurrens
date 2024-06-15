import sqlite3
from flask import jsonify
import pandas as pd
from stats.ols_regression import protected_class_pvalue

def db_connect():
    conn = sqlite3.connect('employees.db')
    conn.row_factory = sqlite3.Row
    return conn

def calculate_pvalue():
    conn = db_connect()
    query = 'SELECT protected_class, tenure, performance, compensation FROM employees'
    df = pd.read_sql_query(query, conn)
    conn.close()

    pvalue = protected_class_pvalue(df)
    
    return pvalue