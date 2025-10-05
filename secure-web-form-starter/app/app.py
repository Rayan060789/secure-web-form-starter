
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///submissions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
csrf = CSRFProtect(app)
limiter = Limiter(get_remote_address, app=app, default_limits=["5 per minute"])

class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    comment = db.Column(db.Text, nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/form", methods=["GET", "POST"])
@limiter.limit("5 per minute")
def form():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        comment = request.form.get("comment")

        if not name or not email or not password:
            flash("All fields except comment are required!", "danger")
            return redirect(url_for("form"))

        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
        new_sub = Submission(name=name, email=email, password_hash=hashed_pw, comment=comment)
        db.session.add(new_sub)
        db.session.commit()
        flash("Submission successful!", "success")
        return redirect(url_for("form"))
    return render_template("form.html")

@app.route("/admin")
def admin():
    subs = Submission.query.order_by(Submission.timestamp.desc()).all()
    return render_template("dashboard.html", submissions=subs)

if __name__ == "__main__":
    app.run(debug=True)
