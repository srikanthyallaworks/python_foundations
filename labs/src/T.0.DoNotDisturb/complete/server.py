#!/usr/bin/env python
from flask import Flask, render_template,request
from dataclasses import dataclass

try:
  from .settings import get_settings
  from .status import Status
except:
  from settings import get_settings
  from status import Status

@dataclass
class State():
  status:Status

def serve(state:State,settings):

  app = Flask(__name__)

  @app.route('/')
  def index() -> 'html':
    return render_template('index.html')

  @app.route('/status', methods=['GET'])
  def get_status() -> 'json':
    return {'status':state.status}

  @app.route('/status', methods=['POST'])
  def set_status() -> 'json':
    state.status = request.get_json()['status']
    return {"result":"ok"}

  app.run(port=settings.port)



def main():
  state = State("green")
  settings=get_settings()
  serve(state, settings)

  
if __name__ == '__main__':
  main()


