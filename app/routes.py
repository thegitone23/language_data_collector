from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm, SubmitReplyForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Sentence, Reply


@app.route("/")
@app.route("/index")
def index():
  return render_template("index.html", user=current_user )

@app.route("/login", methods=["GET", "POST"])
def login():
  if current_user.is_authenticated:
    return redirect(url_for("index"))

  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username.data).first()
    if user is None or not user.check_password(form.password.data):
      flash("Invalid Credentials")
      return redirect(url_for("login"))
    login_user(user, remember=form.remember_me.data) 
    return redirect(url_for("index"))

  return render_template("login.html", form=form, user=current_user)

@app.route("/register", methods=["GET", "POST"])
def register():
  if current_user.is_authenticated:
    return redirect(url_for("index"))
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(username=form.username.data, email=form.email.data)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
    flash("Congratulations, you are now a registered user!")
    return redirect(url_for("login"))
  return render_template("register.html", title="Register", form=form, user=current_user)

@app.route("/logout")
def logout():
  logout_user()
  return redirect(url_for("index"))

@app.route("/sentences")
@login_required
def sentences():
  sentence_list = Sentence.query.all()
  return render_template("sentences.html", sentence_list=sentence_list, user=current_user)

@app.route("/reply_to/<sentence_id>", methods=["GET", "POST"])
@login_required
def reply_to(sentence_id):
  form = SubmitReplyForm()
  sentence = Sentence.query.get_or_404(sentence_id)
  previous_reply = Reply.query.filter_by(sentence_id=sentence_id).filter_by(user_id=current_user.id).first()
  previous_reply_text=""

  if previous_reply:
    previous_reply_text = previous_reply.text

  if form.validate_on_submit():
    txt = form.text.data
    if previous_reply:
      previous_reply.text = txt
      db.session.commit()
    else:
      reply = Reply(text=txt, sentence_id=sentence_id, user_id=current_user.id)
      sentence.reply_count += 1
      db.session.add(reply)
      db.session.commit()

    flash("Thanks For The Reply .. Keep Up The Good Work..")
    return redirect(url_for("index"))
  return render_template("submit_reply.html", sentence=sentence.text, previous_reply=previous_reply_text, form=form, user=current_user)