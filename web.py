from crawler import song_lyrics
from flask import Flask ,url_for
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
    artists=Artists.query.all()
    formatted =[]
    for i in artists:
        target = url_for("artist",artist_id=i.id)
        link =f'<a href ="{target}">{i.name}</a>'
        formatted.append(f"<li>{link}</li>")
    return "<ul>"+"".join(formatted)+ "</ul>"

@app.route("/artist/<int:artist_id>")
def artist(artist_id):
    artist = Artists.query.filter_by(id = artist_id).first()
    #select id, name from artists where id = artist_id
    formatted = []
    for song in artist.songs:
        target = url_for("song", song_id=song.id)
        link = f'<a href="{target}">{song.name}</a>'
        formatted.append(f"<li>{link}</li>")
    songs_list = "".join(formatted)
    return f"""Songs by <em>{artist.name}</em><ol>{songs_list}</ol>"""

@app.route("/song/<int:song_id>")
def song(song_id):
        lyrics = Songs.query.filter_by(id = song_id).all()
        for i in lyrics:
            lyric = i.lyrics
        return f"{lyric}" 