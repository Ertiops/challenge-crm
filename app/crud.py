from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME
from models.models import Users
from models.models import Reservations

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

session = Session(bind=engine)

"""USER TABLE CRUD OPERATIONS"""

def add_user(first_name, last_name, email, password, role, franchise):
    user = Users(
        first_name=first_name,
        last_name=last_name,
        email=email,
        role=role,
        franchise=franchise
    )
    user.set_password(password)
    session.add(user)
    session.commit()

def check_user(email, password):
    # returns True or False
    query = session.query(Users).filter_by(email=email).first()
    if query != None:
        result = query.check_password(password)
        return result
    else:
        return None
    
def get_user(email):
    query = session.query(Users).filter_by(email=email).first()
    return query    

# add_user('Илья', 'Томин', 'straxisrule@gmail.com', '12345', 'owner', 'all')

# print(u.check_password('12345'))

# print(u.check_password('notherightpassword '))

# print(check_user('straxisrule@gmail.com', '123456'))


"""RESERVATIONS TABLE CRUD OPERATIONS"""

def add_reservation(name, phone, mail, quest, date, time, guest_number, price, franchise):
    reservations = Reservations(
        name = name,
        phone = phone,
        mail = mail,
        quest = quest,
        date = date,
        time = time,
        guest_number = guest_number,
        price = price,
        franchise = franchise
        )
    session.add(reservations)
    session.commit()






"""FRANCHISES TABLE CRUD OPERATIONS"""





