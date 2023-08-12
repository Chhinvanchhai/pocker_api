
import datetime
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from api import app
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey,  String, Column, DateTime, Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
# import pymysql
from sqlalchemy import create_engine


# create the app
# configure the SQLite database, relative to the app instance folder

# ========
# userpass = 'mysql+pymysql://root:@'
# basedir  = '127.0.0.1'
# dbname   = '/pocker'
# socket   = '?unix_socket=/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock'
# dbname   = dbname + socket
# app.config['SQLALCHEMY_DATABASE_URI'] = userpass + basedir + dbname
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# ========

# for postgre
db_url = "postgresql://postgres:123456@localhost:5432/poker"
# db_url = "postgresql://postgres:123456@db:5432/poker"
app.config['SQLALCHEMY_DATABASE_URI'] = db_url

engine = create_engine(db_url, echo=True)
db =  Session(engine)


# ====---sqlite---=====
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# db.init_app(app)

class Base(DeclarativeBase):
     pass

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(225), unique=True, nullable=False)
#     password = db.Column(db.String(225), nullable=False)
#     email = db.Column(db.String(225))
#     lastName = db.Column(db.String(225))
#     firstName = db.Column(db.String(225))
#     status = db.Column(db.String(225))
#     createdAt = db.Column(db.DateTime, default=datetime.date.today())
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable= True, unique=True,)
    password: Mapped[str] = mapped_column(String(128), nullable= False)
    lastName: Mapped[str] = mapped_column(String(100), nullable= True)
    firstName: Mapped[str] = mapped_column(String(100), nullable= True)
    status: Mapped[int] = mapped_column( default= 0)
    createdAt = Column(DateTime, default=datetime.datetime.utcnow)
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    # def __repr__(self) -> str:
    #     return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
     __tablename__ = "address"

     id: Mapped[int] = mapped_column(primary_key=True)
     email_address: Mapped[str]
     user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

     user: Mapped["User"] = relationship(back_populates="addresses")

    #  def __repr__(self) -> str:
    #      return f"Address(id={self.id!r}, email_address={self.email_address!r})"



Base.metadata.create_all(engine)
