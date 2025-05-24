from flask import Flask 
app = Flask(__name__) 
@app.route('/') 
def home(): 
  return "TP4 : Bonjour depuis Render !  l'app Flask est bien en ligne..." 
if __name__ == '__main__': 
  app.run()
