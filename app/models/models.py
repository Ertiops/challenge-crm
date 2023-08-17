from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, UUID, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import uuid
import datetime
from werkzeug.security import generate_password_hash, check_password_hash


Base  = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    id  = Column(UUID(as_uuid=True), default=uuid.uuid4(), primary_key=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False)
    password_hash = Column(String(150), nullable=False)
    role =  Column(String(20), nullable=False)
    franchise = Column(String(30), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    
class Reservations(Base):
    __tablename__ = 'reservations'

    reservation_id = Column(Integer, primary_key=True)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)
    name = Column(String(60), nullable=False)
    phone = Column(String(30), nullable=False)
    mail = Column(String(30), nullable=False)
    quest = Column(String(120), nullable=False)
    date = Column(String(30), nullable=False)
    time = Column(String(30), nullable=False)
    guest_number = Column(Integer, nullable=False)
    price = Column(String(30), nullable=False)
    franchise = Column(String(120), nullable=False)











