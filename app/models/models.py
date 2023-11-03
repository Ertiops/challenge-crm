from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, UUID, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime
import pytz
from werkzeug.security import generate_password_hash, check_password_hash



Base  = declarative_base()


class Owners(Base, UserMixin):
    __tablename__ = 'owners'
    id = Column(UUID(as_uuid=True), default=uuid.uuid4(), primary_key=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    patronymic = Column(String(30))
    email = Column(String(30), nullable=False)
    phone = Column(String(11), nullable=False)
    password_hash = Column(String(150), nullable=False)
    role =  Column(String(20), nullable=False)
     
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Franchises(Base):
    __tablename__ = 'franchises'
    id  = Column(UUID(as_uuid=True), primary_key=True)
    city = Column(String(50), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now(pytz.timezone('Europe/Moscow')))





class Users(Base, UserMixin):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    patronymic = Column(String(30))
    email = Column(String(30), nullable=False, unique=True)
    phone = Column(String(11), nullable=False, unique=True)
    password_hash = Column(String(150), nullable=False)
    role = Column(String(20), nullable=False)
    franchise_id = Column(UUID(as_uuid=True), ForeignKey("franchises.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now(pytz.timezone('Europe/Moscow')))
    verified = Column(Boolean, default=False)

    franchises=relationship('Franchises')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    







class Reservations(Base):
    __tablename__ = 'reservations'

    reservation_id = Column(Integer, primary_key=True)
    date_created = Column(DateTime, default=datetime.now(pytz.timezone('Europe/Moscow')))
    name = Column(String(60), nullable=False)
    phone = Column(String(30), nullable=False)
    mail = Column(String(30), nullable=False)
    quest = Column(String(120), nullable=False)
    date = Column(String(30), nullable=False)
    time = Column(String(30), nullable=False)
    guest_number = Column(Integer, nullable=False)
    price = Column(String(30), nullable=False)
    franchise = Column(String(120), nullable=False)














