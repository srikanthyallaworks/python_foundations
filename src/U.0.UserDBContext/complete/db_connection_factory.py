from typing import List, Optional
from db_connection import DBConnection, DBConnectionStatus


class DBConnectionFactory:
    """Builds database connections. Keeps them in a pool for performance.

    Raises:
        Exception: Throws when the pool is full.
    """
    _connection_string: str
    _max_connections = 5
    _pool: List[DBConnection] = []

    def __init__(self, connection_string: str) -> None:
        self._connection_string = connection_string

    def get_connection(self) -> DBConnection:
        """Gets a usable database connection.

        Raises:
            Exception: Throws when out of connections.

        Returns:
            DBConnection: Usable connection.
        """
        con: Optional[DBConnection] = None
        if len(self._pool) <= self._max_connections:
            con = DBConnection()
            self._pool.append(con)
        else:
            recyclable = [c for c in self._pool
                          if c.status == DBConnectionStatus.Closed]
            if len(recyclable) == 0:
                raise Exception('Out of database connections!')
            con = recyclable[0]

        con.status = DBConnectionStatus.ReadyToUse
        return con
