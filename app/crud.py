from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME
from models.models import Users

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

session = Session(bind=engine)


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

# add_user('Илья', 'Томин', 'straxisrule@gmail.com', '12345', 'owner', 'all')


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



# u = 
# print(u.check_password('12345'))

# print(u.check_password('notherightpassword'))

# print(check_user('straxisrule@gmail.com', '123456'))
