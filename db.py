import psycopg2

def get_connection(dbname="lyrics"):
    return psycopg2.connect(f"dbname={dbname}")


def add_artist(artist_name):
    conn = get_connection()
    with conn.cursor() as curs:
        curs.execute("INSERT INTO artists(name) VALUES(%s)", (artist_name,))
        curs.execute("SELECT id FROM artists ORDER BY id DESC")
        id = curs.fetchone()[0]
    conn.commit()
    conn.close()
    return id

def add_song(song_name, artist_id, lyrics):
    conn = get_connection()
    with conn.cursor() as curs:
        curs.execute("INSERT INTO songs(name, artist_id, lyrics) VALUES(%s,%s, %s)",
         (song_name, artist_id, lyrics))
    conn.commit()
    conn.close()


# import sys

# import psycopg2
# import models


# def get_all_artists():
#     sess = models.get_session("postgresql:///lyrics")
#     artists = sess.query(models.Artist).all()
#     return [x.name for x in artists]

#     # conn = get_connection("lyrics")
#     # cur = conn.cursor()
#     # cur.execute("SELECT name FROM artist")
#     # results = [x[0] for x in cur.fetchall()]
#     # return results

# def get_songs_for(artist):
#     sess = models.get_session("postgresql:///lyrics")
#     artist = sess.query(models.Artist).filter(models.Artist.name == artist).first()
#     return [(x.name, x.lyrics) for x in artist.songs]

#     # conn = get_connection("lyrics")
#     # cur = conn.cursor()
#     # cur.execute("SELECT s.name,s.lyrics from artist a, song s where a.name = %s and a.id = s.artist", (artist,))
#     # results = cur.fetchall()
#     # return results

# def main():
#     if len(sys.argv) == 1:
#         for i in get_all_artists():
#             print (i)
#     else:
#         for name, lyrics in get_songs_for(sys.argv[1]):
#             print (name)
#             print (lyrics)
#             print ("-"*30)

# if __name__ == "__main__":
#     main()
# # ["Megha", "Afreedi", "Shamil", "Shahina", "Sooraj", "Sreejith", "Waleed"]
