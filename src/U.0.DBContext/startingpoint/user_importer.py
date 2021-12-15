from typing import List
from user import User
from db_connection_factory import DBConnectionFactory, DBConnection

connection_string = 'Server=thor01;Database=Contoso;User Id=app;Password=5uper5ecret;'
factory = DBConnectionFactory(connection_string)

def to_sql(u:User):
    return f'INSERT User({u.id}, {u.login},...)'

def import_user(u:User):
    con = factory.get_connection()
    con.open()
    sql = to_sql(u)
    con.execute(sql)
    con.close()

def import_users(users:List[User]):
    for u in users:
        import_user(u)

