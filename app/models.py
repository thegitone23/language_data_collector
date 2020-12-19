from app import db, login, Config
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user
from flask_admin.contrib.sqla import ModelView

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)
  email = db.Column(db.String(120), index=True, unique=True)
  password_hash = db.Column(db.String(128))
  replies = db.relationship('Reply', backref='author', lazy='dynamic')

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

  def __repr__(self):
    return "<User {}>".format(self.username)

class Sentence(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  text = db.Column(db.Unicode(192))
  reply_count = db.Column(db.Integer,default=0, index=True)
  replies = db.relationship('Reply', backref='sentence', lazy='dynamic')  

  def __repr__(self):
    return "<Sentence : {}>".format(self.text)

class Reply(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  text = db.Column(db.Unicode(192))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  sentence_id = db.Column(db.Integer, db.ForeignKey('sentence.id'))   

  def __repr__(self):
    return "<Reply : {}>".format(self.text)

@login.user_loader
def load_user(id):
  return User.query.get(int(id))

class MyModelView(ModelView):
  def is_accessible(self):
    return current_user.is_authenticated and current_user.username == Config.ADMIN_NAME