from flask import Flask ,url_for,render_template ,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_accept import accept

import time

app = Flask('lyrics')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///lyrics'
db= SQLAlchemy(app)


class Artists(db.Model):
    __tablename__ = "artists"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    songs = db.relationship("Songs", back_populates="artist")

    def __repr__(self) -> str:
        return f"Artists('{self.name}')"

class Songs(db.Model):
    __tablename__ = "songs"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    lyrics = db.Column(db.String)
    artist_id = db.Column(db.Integer, db.ForeignKey("artists.id"), nullable=False)
    artist = db.relationship("Artists", back_populates="songs")

    def __repr__(self) -> str:
        return f"Songs('{self.name}')"

@app.route("/")
def index():
    artists = Artists.query.all()
    nartist= len(artists)
    # formatted =[]
    # for i in artists:
    #     target = url_for("artist",artist_id=i.id)
    #     link =f'<a href ="{target}">{i.name}</a>'
    #     formatted.append(f"<li>{link}</li>")
    #return "<ul>"+"".join(formatted)+ "</ul>"
    return render_template("index.html",artists=artists,no_artist=nartist)


@app.route("/artist/<int:artist_id>")
def artist(artist_id):
    artist = Songs.query.filter_by(artist_id = artist_id).all()
    no_songs=len(artist)
    #select id, name from artists where id = artist_id
    # formatted = []
    # for song in artist.songs:
    #     target = url_for("song", song_id=song.id)
    #     link = f'<a href="{target}">{song.name}</a>'
    #     formatted.append(f"<li>{link}</li>")
    # songs_list = "".join(formatted)
    time.sleep(2)

    return render_template("song.html",songs=artist,nartist = no_songs)

@app.route("/song/<int:song_id>")
@accept("text/html")
def song(song_id):
        song = Songs.query.filter_by(id = song_id).first()
        lyric =song.lyrics.replace("\n","<br>")     
        time.sleep(2)
        return render_template("songs.html",lyrics=lyric,songs_=song)

@song.support("application/json")
def song_json(song_id):
        print("am returning json!....")
        song = Songs.query.filter_by(id = song_id).first()
        lyric =song.lyrics
        ret = dict(song= dict(name=song.name,
                            lyrics = song.lyrics,
                            id=song.id,
                            artist= dict(name=song.artist.name,id=song.artist.id)))
        return jsonify(ret)




# @app.route("/lyrics/<int:song_id>")
# def lyrics(song_id):
#     song = Songs.query.filter_by(id = song_id).first()
#     time.sleep(2)
#     return render_template("lyrics.html", 
#                            song = song) 