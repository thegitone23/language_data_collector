from app import app

@app.route("/")
def index():
  return "Hello World From Flask"
