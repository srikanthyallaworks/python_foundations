#!/usr/bin/env python
from flask import Flask, render_template,request, jsonify
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
    return jsonify({'status':state.status.value})

  @app.route('/status', methods=['POST'])
  def set_status() -> 'json':
    value = request.get_json()['status']
    state.status = Status(value)
    return jsonify({"result":"ok"})

  app.run(port=settings.port,host='0.0.0.0')



def main():
  state = State(Status.Green)
  settings=get_settings()
  serve(state, settings)

  
if __name__ == '__main__':
  main()


