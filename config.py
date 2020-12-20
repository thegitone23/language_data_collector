import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  SECRET_KEY = os.environ.get("SECRET_KEY") or "its_a_secret_hmmm"
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABSE_URL") or "sqlite:///" + os.path.join(basedir, "app.db")
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  ADMIN_NAME = os.environ.get("ADMIN_NAME") or "mynk_11"
  