"""



"""

from flask import Flask, render_template,request
import unicornhathd
import time


unicornhathd.brightness(1)
unicornhathd.set_all(255,0,0)
unicornhathd.show()
time.sleep(.25)
unicornhathd.show()


class State():
  def __init__(self):
    self._current = { "status":"green"}    

  def get(self):
    return self._current

  def set(self,new_status):
    self._current=new_status
    r=0
    g=0
    b=0
    if new_status["status"]=='green':
      g=255
    elif new_status["status"]=='red':
      r=255
    else:
      b=255
    print(r,g,b)
    unicornhathd.set_all(r,g,b)
    unicornhathd.show()

def serve(state):

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

  app.run()



def main():
  state = State()
  


  serve(state)

  



if __name__ == '__main__':
  main()





# def main():



# if __name__ == '__main__':
#   main()

