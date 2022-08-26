from os import name
from typing_extensions import Self
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,relationship 
from sqlalchemy import Column , ForeignKey 
from sqlalchemy import Integer , String
from sqlalchemy.orm import session 
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql:///rought',echo=True,future=True)

#session =  sessionmaker(bind=engine)
#session = session()


base = declarative_base()

class Artists(base):
    __tablename__ = "artist"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    songs = relationship("Songs", back_populates="artist")

class Songs(base):
    __tablename__ = "songs"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    lyrics = Column(String)
    artist_id = Column(Integer, ForeignKey("artist.id"), nullable=False)
    artist = relationship("Artists", back_populates="songs")


def get_session():

    engine = create_engine('postgresql:///rought',echo=True)
    base.metadata.create_all(engine)
    Session = sessionmaker(bind = engine)
    session = Session()
    return session

#artist1= artists(id=1,name='raj',song='asa')
#session.add(artist1)
#session.commit()

def drop_table():
    base.metadata.drop_all(engine)
    base.metadata.create_all(engine)
