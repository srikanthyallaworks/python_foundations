from enum import Enum
import random

class DBConnectionStatus(Enum):
  LentOut = 0
  Open = 1
  Closed = 2

class DBConnection:
  status: DBConnectionStatus = DBConnectionStatus.LentOut
  
  def open(self):
    if self.status != DBConnectionStatus.LentOut:
      raise Exception('Can\'t open an open connection!')
    self.status = DBConnectionStatus.Open

  def close(self):
    if  self.status != DBConnectionStatus.Open:
      raise Exception('Can\'t close a closed or new connection!')
    self.status = DBConnectionStatus.Closed

  def execute(self, sql_command:str)->str:
    if self.status != DBConnectionStatus.Open:
      raise Exception('Can\'t execute sql on a closed connection!')

    if random.random() > .8:
      raise Exception('Database returned an error. (String too long or something.)')

    print(f'[[Executing {sql_command}]]')
    return '1 row affected'

