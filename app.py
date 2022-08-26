from pydoc import render_doc
from crawler import song_lyrics
from flask import Flask ,url_for,render_template
from flask_sqlalchemy import SQLAlchemy

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
    return render_template("song.html",songs=artist,nartist = no_songs)

@app.route("/artist/song/<int:song_id>")
def song(song_id):
        artist = Songs.query.all()
        song = Songs.query.filter_by(id = song_id).first()
        lyric =song.lyrics.replace("\n","<br>")     
        return render_template("song.html",lyrics=lyric,song_name=song.name,songs=artist ,songs_=song)
        