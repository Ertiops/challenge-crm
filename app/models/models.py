from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import uuid
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
    











