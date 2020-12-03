#!/usr/bin/env python

"""



"""

from flask import Flask, render_template,request
from settings import get_settings

class State():
  def __init__(self):
    self._current = { "status":"green"}    

  def get(self):
    return self._current

  def set(self,new_status):
    self._current=new_status


def serve(state,settings):

  app = Flask(__name__)

  @app.route('/')
  def index() -> 'html':
    return render_template('index.html')

  @app.route('/status', methods=['GET'])
  def get_status() -> 'json':
    return state.get()

  @app.route('/status', methods=['POST'])
  def set_status() -> 'json':
    new_status = request.get_json()
    state.set(new_status)
    return {"result":"ok"}

  app.run(port=settings.port)



def main():
  state = State()
  settings=get_settings()
  serve(state, settings)

  
if __name__ == '__main__':
  main()


