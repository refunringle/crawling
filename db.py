import psycopg2

def get_connection(dbname="lyrics"):
    return psycopg2.connect(f"dbname={dbname}")

def add_artist(artist_name):
    conn = get_connection()
    with conn.cursor() as curs:
        curs.execute("INSERT INTO artists(name) VALUES(%s)", (artist_name,))
    conn.commit()
    conn.close()
    