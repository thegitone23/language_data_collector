from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
  return render_template("index.html", announcements = ["Work Under Progress"] )

@app.route("/login", methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    flash("User {} with remember me={} .. Loging In".format(form.username.data, form.remember_me.data))
    return redirect(url_for("index"))
  return render_template("login.html", form=form)