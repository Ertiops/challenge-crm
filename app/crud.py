from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME
from models.models import Owners, Users, Franchises
from models.models import Reservations

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

session = Session(bind=engine)

"""OWNER TABLE CRUD OPERATIONS"""

def add_owner(first_name, last_name, patronymic, email, phone,  password, role):
    owner = Owners(
        first_name=first_name,
        last_name=last_name,
        patronymic=patronymic,        
        email=email,
        phone=phone,
        role=role
    )
    owner.set_password(password)
    session.add(owner)
    session.commit()

def check_owner(email, password):
    # returns True or False
    query = session.query(Owners).filter_by(email=email).first()
    if query != None:
        result = query.check_password(password)
        return result
    else:
        return None
    
def get_owner(email):
    query = session.query(Owners).filter_by(email=email).first()
    return query  

# add_owner('Илья', 'Томин', 'Сергеевич', 'straxisrule@gmail.com', '89534087334', '12345', 'owner')

"""FRANCHISES TABLE CRUD OPERATIONS"""

def add_franchise(id, city):
    franchise = Franchises(
        id=id,
        city=city
    )
    session.add(franchise)
    session.commit()

# add_franchise("Набережные Челны")

def get_franchises_and_franchiser():
    query = session.query(Franchises, Users).join(Users, Franchises.id == Users.franchise_id).filter(Users.role == "франчайзер").all()
    return query

def get_franchise_and_franchiser_by_id(franchise_id):
    query = session.query(Franchises, Users).join(Users, Franchises.id == Users.franchise_id).filter(Franchises.id == franchise_id).filter(Users.role == "франчайзер").first()
    return query

# print(get_franchise_and_franchiser_by_id("db2da6b8-c2db-4d2f-98bc-3bc12582d795"))   

def delete_franchise(id):
    franchise = session.query(Franchises).filter_by(id=id).first()
    session.delete(franchise)
    session.commit()

# delete_franchise("")



"""USER TABLE CRUD OPERATIONS"""

def add_user(first_name, last_name, patronymic, email, phone, password, role, franchise_id):
    user = Users(
        first_name=first_name,
        last_name=last_name,
        patronymic=patronymic,
        email=email,
        phone=phone,
        role=role,
        franchise_id=franchise_id
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

# add_user('Илья', 'Томин', 'Сергеевич', 'straxisrule@gmail.com', '89534087334', '12345', 'franchiser', '161aa0f3-acb9-4311-b4d8-7e5a4998cc94')

# print(u.check_password('12345'))

# print(u.check_password('notherightpassword '))

# print(check_user('straxisrule@gmail.com', '123456'))
   
# print(check_user_and_owner('straxisrule@gmail.com', '12345'))





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












