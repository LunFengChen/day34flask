import pymysql
from pymysql.cursors import DictCursor
from dbutils.pooled_db import PooledDB

POOL = PooledDB(
    creator=pymysql,
    maxconnections=20,
    mincached=2,
    blocking=True,
    host="127.0.0.1", port=3306, user="root", password="Zcr1314.", charset="utf8", db="s4big"
)


def fetch_one(sql, params):
    conn = POOL.connection()
    cursor = conn.cursor(cursor=DictCursor)

    cursor.execute(sql, params)
    row_dict = cursor.fetchone()
    cursor.close()
    conn.close()

    return row_dict


def fetch_all(sql, params):
    conn = POOL.connection()
    cursor = conn.cursor(cursor=DictCursor)

    cursor.execute(sql, params)
    data_list = cursor.fetchall()
    cursor.close()
    conn.close()

    return data_list


# 支持update, insert, delete
def commit(sql, params):
    conn = POOL.connection()
    cursor = conn.cursor(cursor=DictCursor)

    cursor.execute(sql, params)
    conn.commit()

    cursor.close()
    conn.close()
