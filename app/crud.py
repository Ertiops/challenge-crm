from sqlalchemy import create_engine, select, and_, or_, func, case, cast, Integer
from sqlalchemy.orm import Session
from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME
from models.models import Owners, Users, Franchises
from models.models import Reservations

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
session = Session(bind=engine)

class OwnersCRUD:

    def add_owner(first_name: str, last_name: str, patronymic: str, email: str, phone: int,  password: str, role: str):
        """creates an owner in table Owners"""
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
        session.close() 

    def check_owner(email: str, password: str):
        """checks if owner exists in table Owners by email"""
        query = session.query(Owners).filter_by(email=email).first()
        if query != None:
            result = query.check_password(password)
            return result
        else:
            return None
        
    def get_owner(email: str):
        """query an owner by email"""
        query = session.query(Owners).filter_by(email=email).first()
        return query 

    def get_owner_by_id(id: str):
        """gets owner's id"""
        query = session.get(Owners, str(id)) 
        return query


class FranchisesCRUD:

    def add_franchise(id: str, city: str):
        """creates a franchise in table Franchises"""
        franchise = Franchises(
            id=id,
            city=city
        )
        session.add(franchise)
        session.commit()
        session.close() 

    # def get_franchises_and_franchiser():
    #     query = session.query(Franchises, Users).join(Users, Franchises.id == Users.franchise_id).filter(Users.role == "франчайзер").order_by(Franchises.created_at).all()
    #     return query

    # def get_franchise_and_franchiser_by_id(franchise_id: str):
    #     query = session.query(Franchises, Users).join(Users, Franchises.id == Users.franchise_id).filter(Franchises.id == franchise_id).filter(Users.role == "франчайзер").first()
    #     return query

    def get_franchises():
        """query all franchises of table Franchises"""
        query = session.query(Franchises).order_by(Franchises.created_at).all()
        return query

    def get_franchises_and_counted_employees():
        """query the count of different types of employees grouped by franchises"""
        user_subquery = (
            session.query(
                Users.franchise_id,
                func.count().filter(Users.role == "актёр").label("actor_count"),
                func.count().filter(Users.role == "оператор").label("operator_count"),
                func.count().filter(Users.role == "администратор").label("admin_count"),
            )
            .filter(Users.role.in_(["актёр", "оператор", "администратор"]))
            .group_by(Users.franchise_id)
            .subquery()
        )
        supervisor_subquery = (
            session.query(
                Users.franchise_id,
                func.count().filter(Users.role.in_(["директор", "франчайзер"])).label("supervisor_count")
            )
            .filter(Users.role.in_(["директор", "франчайзер"]))
            .group_by(Users.franchise_id)
            .subquery()
        )
        query = (
            session.query(
                Franchises.id,
                Franchises.city,
                user_subquery.c.actor_count,
                user_subquery.c.operator_count,
                user_subquery.c.admin_count,
                supervisor_subquery.c.supervisor_count
            )
            .outerjoin(user_subquery, Franchises.id == user_subquery.c.franchise_id)
            .outerjoin(supervisor_subquery, Franchises.id == supervisor_subquery.c.franchise_id)
            .group_by(
                Franchises.id,
                Franchises.city,
                user_subquery.c.actor_count,
                user_subquery.c.operator_count,
                user_subquery.c.admin_count,
                supervisor_subquery.c.supervisor_count
            )
            .order_by(Franchises.created_at) 
            .all()
        )
        return query

    def update_franchise(id: str, city: str):
        """updates data for franchise in Franchises table"""
        query = session.query(Franchises).filter_by(id=id).first()
        if query:
            query.city = city
            session.commit()
            session.close()
            return True
        else:
            return False

    def delete_franchise(id: str):
        """"deletes a franchise by it's id"""
        franchise = session.query(Franchises).filter_by(id=id).first()
        session.delete(franchise)
        session.commit()
        session.close()

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
            .order_by(Franchises.created_at)
            .all())
        return query 

    def is_city_unique_except_current(id: str, city: str):
        """checks if city in table Franchises unique and excepts row of franchise's id"""         
        query = session.query(Franchises).filter(and_(Franchises.city == city, Franchises.id != id)).first()
        if query:
            return False
        else:
            return True
        
    def is_city_unique(city: str):
        """returns False if city is in database, otherwise returns True"""
        query = session.query(Franchises).filter_by(city=city).first()   
        if query:
            return False
        else:
            return True    


class EmployeesCRUD:

    def add_user(id: str, first_name: str, last_name: str, patronymic: str, email: str, phone: int, password: str, role: str, franchise_id: str):
        """creates a user for table Users in db"""
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
        session.close()

    def check_user(email: str, password: str):
        """returns True or False whether email in db and returns None otherwise"""
        query = session.query(Users).filter_by(email=email).first()
        if query != None:
            result = query.check_password(password)
            return result
        else:
            return None
        
    def get_user(email: str):
        """returns query row from Users table by email"""
        query = session.query(Users).filter_by(email=email).first()
        return query 

    def update_user(id: str, first_name: str, last_name: str, patronymic: str, email: str, old_email: str, phone: int, role: str):
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
            session.close()
            return True
        else:
            return False

    def get_employees(franchise_id: str, role: str):
        """makes a query of employees data from particular franchise and role of table Users"""
        query = session.query(Users).filter_by(franchise_id=franchise_id).filter_by(role=role).order_by(Users.created_at).all()
        return query

    def get_bosses(franchise_id: str):
        """makes a query of directors and franchisers data from particular franchise of table Users"""        
        query = session.query(Users).filter_by(franchise_id=franchise_id).filter(or_(Users.role == "директор", Users.role == "франчайзер")).order_by(Users.role).order_by(Users.created_at).all()
        return query   

    def delete_user(email: str):
        """deletes a particular user from table Users by email"""
        user = session.query(Users).filter_by(email=email).first()
        session.delete(user)
        session.commit()
        session.close()

    def is_email_unique_except_current(id: str, email: str):
        """checks if email in table Users and excepts row of user's id"""
        query = session.query(Users).filter(and_(Users.email == email, Users.id != id)).first()
        if query:
            return False
        else:
            return True
        
    def is_phone_unique_except_current(id: str, phone: int):
        """checks if phone in table Users and excepts row of user's id"""        
        query = session.query(Users).filter(and_(Users.phone == phone, Users.id != id)).first()
        if query:
            return False
        else:
            return True

    def is_email_unique(email: str):
        """checks if email is unique"""
        query = session.query(Users).filter_by(email=email).first()   
        if query != None:
            return False
        else:
            return True
        
    def is_phone_unique(phone: int):
        """checks if phone is unique"""
        query = session.query(Users).filter_by(phone=phone).first()   
        if query != None:
            return False
        else:
            return True
        
    def get_employee_by_id(id: str):
        """gets employee row from Users table"""
        query = session.get(Users, str(id)) 
        return query

class ReservationsCRUD:

    def add_reservation(name: str, phone: int, mail: str, quest: str, date: str, time: str, guest_number: int, price: float, franchise: str):
        """creates a reservation of a quest in Reservations table"""
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
        session.close()


