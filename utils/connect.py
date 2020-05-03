def db_connect(us: str, passw: str):
    try:
        conn = mysql.connector.connect(user=us, password=passw, host='127.0.0. 1',
                                       database='school')
    except:
        conn = None
    return conn
