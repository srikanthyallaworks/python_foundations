from typing import List
from user import User
from db_connection_factory import DBConnectionFactory, DBConnection


def to_sql(u: User) -> str:
    """Builds an insert statement for the specified user.

    Args:
        u (User): User that gets added to the database.

    Returns:
        str: SQL query 
    """
    return f'INSERT User({u.id}, {u.login},...)'


class UserImporter:
    """Tool for importing users into a database. 
    """

    factory: DBConnectionFactory

    def __init__(self, connection_string: str) -> None:
        self.factory = DBConnectionFactory(connection_string)

    def import_user(self, u: User):
        """Imports a single user into the database.

        Args:
            u (User): [description]
        """
        con = self.factory.get_connection()
        con.open()
        sql = to_sql(u)
        con.execute(sql)
        con.close()

    def import_users(self, users: List[User]):
        """Imports a batch of users.

        Args:
            users (List[User]): Users to import.
        """
        for u in users:
            try:
                self.import_user(u)
            except Exception as e:
                # TODO: Log this to a file so we can add the user manually
                print(f'Error: [{e}] on user: [{u}]')
