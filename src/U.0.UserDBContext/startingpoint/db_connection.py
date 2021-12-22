from enum import Enum
import random


class DBConnectionStatus(Enum):
    ReadyToUse = 0
    Open = 1
    Closed = 2


class DBConnection:
    """Connection to the database. Use this to execute queries.
    """

    status: DBConnectionStatus = DBConnectionStatus.ReadyToUse

    def open(self):
        """Opens a connection to the database.

        Raises:
            Exception: Only ReadyToUse connections can be opened.
        """
        if self.status != DBConnectionStatus.ReadyToUse:
            raise Exception('Can\'t open an open connection!')
        self.status = DBConnectionStatus.Open

    def close(self):
        """Closes database connection. Releases resources.

        Raises:
            Exception: Only open connections can be closed.
        """
        if self.status != DBConnectionStatus.Open:
            raise Exception('Can\'t close a closed or new connection!')
        self.status = DBConnectionStatus.Closed

    def execute(self, sql_command: str) -> str:
        """Executes arbitrary SQL

        Args:
            sql_command (str): SQL batch

        Raises:
            Exception: Only open connections can execute queries
            Exception: Sometimes the database returns an error.

        Returns:
            str: Message from the database.
        """
        if self.status != DBConnectionStatus.Open:
            raise Exception('Can\'t execute sql on a closed connection!')

        if random.random() > .8:
            # Simulate the occasional error
            raise Exception(
                'Database returned an error. (String too long or something.)')

        print(f'[[Executing {sql_command}]]')
        return '1 row affected'
