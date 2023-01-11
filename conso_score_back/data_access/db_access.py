from flask import g
import psycopg2


def get_db():
    if 'db' not in g:
        #print("creating connection" + DATA_URL)
        g.db = psycopg2.connect(
            host="localhost",
            port=15432,
            database="postgres", #consoscore ne marche pas
            user="conso_score_user",
            password="conso_score_user_pwd"
        )
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def fetch_into_db(request_string):
	cursor = get_db().cursor()
	cursor.execute(request_string)
	return cursor
