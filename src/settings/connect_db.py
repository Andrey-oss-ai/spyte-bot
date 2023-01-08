from sqlalchemy import Boolean, Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base

from src.settings import DB_FOLDER, BD_NAME

Base = declarative_base()
DB_FOLDER.mkdir(exist_ok=True)
engine = create_engine(f'sqlite:///db/{BD_NAME}.db')


class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    link = Column(String(200), unique=True)
    image = Column(String(200))
    text = Column(String(200))
    send = Column(Boolean, default=False)


class Reminders(Base):
    __tablename__ = 'reminder'
    id = Column(Integer, primary_key=True)
    date = Column(String(200))
    description = Column(String(200))
    repeat = Column(Boolean, default=False)


Base.metadata.create_all(engine)


def db_connect():
    session = Session(engine)
    return session
