"""



"""

from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index() -> 'html':
  return render_template('index.html',current_status = 'Green')

current_status = {
  "status":"green"
}

@app.route('/status', methods=['GET'])
def get_status() -> 'json':
  global current_status
  return current_status

@app.route('/status', methods=['POST'])
def set_status() -> 'json':
  global current_status
  current_status = request.get_json()
  return {"result":"ok"}

app.run()