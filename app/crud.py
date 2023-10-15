from sqlalchemy import create_engine, select, and_, or_, func
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
    query = session.query(Franchises, Users).join(Users, Franchises.id == Users.franchise_id).filter(Users.role == "франчайзер").order_by(Franchises.created_at).all()
    return query

def get_franchise_and_franchiser_by_id(franchise_id):
    query = session.query(Franchises, Users).join(Users, Franchises.id == Users.franchise_id).filter(Franchises.id == franchise_id).filter(Users.role == "франчайзер").first()
    return query

def get_franchises():
    query = session.query(Franchises).order_by(Franchises.created_at).all()
    return query


# print(get_franchise_and_franchiser_by_id("db2da6b8-c2db-4d2f-98bc-3bc12582d795"))   

def update_franchise(id, city):
    """updates data for franchise in Franchises table"""
    query = session.query(Franchises).filter_by(id=id).first()
    if query:
        query.city = city
        session.commit()
        return True
    else:
        return False

def delete_franchise(id):
    franchise = session.query(Franchises).filter_by(id=id).first()
    session.delete(franchise)
    session.commit()

def get_franchises_and_employees_count():
    """selects franchises, cities and joins franchise employees count"""
    user_count_subquery = (
        session.query(Users.franchise_id, func.count(Users.id).label('user_count'))
        .group_by(Users.franchise_id)
        .subquery())

    # Create the main query to select id, city, and user count
    query = (
        session.query(Franchises.id, Franchises.city, user_count_subquery.c.user_count)
        .outerjoin(user_count_subquery, Franchises.id == user_count_subquery.c.franchise_id)
        .all())
    return query 




"""USER TABLE CRUD OPERATIONS"""

def add_user(id, first_name, last_name, patronymic, email, phone, password, role, franchise_id):
    user = Users(
        id=id,
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
    """returns True or False whether email in db and returns None otherwise"""
    query = session.query(Users).filter_by(email=email).first()
    if query != None:
        result = query.check_password(password)
        return result
    else:
        return None
    
def get_user(email):
    """returns query row from Users table by email"""
    query = session.query(Users).filter_by(email=email).first()
    return query 

def update_user(id, first_name, last_name, patronymic, email, old_email, phone, role):
    """updates data for franchiser in Users table"""
    query = session.query(Users).filter_by(email=old_email).first()
    if query:
        query.first_name = first_name
        query.last_name = last_name
        query.patronymic = patronymic
        query.email = email
        query.phone = phone
        query.role = role
        session.commit()
        return True
    else:
        return False

def get_employees(franchise_id, role):
    query = session.query(Users).filter_by(franchise_id=franchise_id).filter_by(role=role).order_by(Users.created_at).all()
    return query

def get_bosses(franchise_id):
    query = session.query(Users).filter_by(franchise_id=franchise_id).filter(or_(Users.role == "директор", Users.role == "франчайзер")).order_by(Users.role).order_by(Users.created_at).all()
    return query   

def delete_user(email):
    user = session.query(Franchises).filter_by(email=email).first()
    session.delete(user)
    session.commit()


def is_email_unique_except_current(id, email):
    query = session.query(Users).filter(and_(Users.email == email, Users.id != id)).first()
    if query:
        return False
    else:
        return True
    

def is_phone_unique_except_current(id, phone):
    query = session.query(Users).filter(and_(Users.phone == phone, Users.id != id)).first()
    if query:
        return False
    else:
        return True


def is_email_unique(email):
    """returns False if email is in database, otherwise returns True"""
    query = session.query(Users).filter_by(email=email).first()   
    if query != None:
        return False
    else:
        return True
    
def is_phone_unique(phone):
    """returns False if phone is in database, otherwise returns True"""
    query = session.query(Users).filter_by(phone=phone).first()   
    if query != None:
        return False
    else:
        return True

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












