from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

class Team(Base):
    __tablename__ = 'team'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'id'           : self.id,
       }
 
class MenuPlayer(Base):
    __tablename__ = 'menu_player'


    name =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    Nationality = Column(String(250))
    number = Column(String(8))
    position = Column(String(250))
    team_id = Column(Integer,ForeignKey('team.id'))
    team = relationship(Team)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'Nationality'         : self.Nationality,
           'id'         : self.id,
           'number'         : self.number,
           'position'         : self.position,
       }



engine = create_engine('sqlite:///teammenuwithusers.db')
 

Base.metadata.create_all(engine)
