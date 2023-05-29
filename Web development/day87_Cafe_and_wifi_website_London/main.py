from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, URL
#from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#Bootstrap(app)
# db.init_app


#Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

#Creating Forms https://flask-wtf.readthedocs.io/en/1.0.x/quickstart/
class CafeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    map_url = StringField('Map url', validators=[DataRequired(), URL()])
    img_url = StringField('Image Url', validators=[DataRequired(), URL()])
    location = StringField('Location', validators=[DataRequired()])
    seats = StringField('How many seats?', validators=[DataRequired()])
    has_toilet = BooleanField('Does it have a toilet?')
    has_wifi = BooleanField('Does it have a wifi?')
    has_sockets = BooleanField('Does it have a socket?')
    can_take_calls = BooleanField('Can you take calls?')
    coffee_price = StringField('Price of cup of coffee?', validators=[DataRequired()])

class PriceForm(FlaskForm):
    coffee_price = StringField('New Price for a cup of coffee?', validators=[DataRequired()])


@app.route("/")
def home():
    all_cafes = db.session.execute(db.select(Cafe).order_by(Cafe.id)).all()
    return render_template("index.html", all_cafes=all_cafes)



#https://www.digitalocean.com/community/tutorials/how-to-use-and-validate-web-forms-with-flask-wtf
@app.route("/add", methods=["GET","POST"])
def add():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(name=request.form.get("name"),
                        map_url=request.form.get("map_url"),
                        img_url=request.form.get("img_url"),
                        location=request.form.get("location"),
                        seats=request.form.get("seats"),
                        has_toilet=bool(request.form.get("has_toilet")),
                        has_wifi= bool(request.form.get("has_wifi")),
                        has_sockets= bool(request.form.get("has_sockets")),
                        can_take_calls=bool(request.form.get("can_take_calls")),
                        coffee_price=request.form.get("coffee_price")
                        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect("/")
    return render_template('add.html', form = form)

@app.route("/report-closed/<int:cafe_id>", methods=["GET"])
def closed_cafe(cafe_id):
    cafe_to_delete = db.session.query(Cafe).get(cafe_id)
    if cafe_to_delete:
        return render_template('delete.html', msg="Should we remove this cafe from the DB?", cafe = cafe_to_delete)
    else:
        return render_template('delete.html', msg="Sorry, the cafe id was not found in the database", cafe = None)

@app.route("/delete/<int:cafe_id>", methods=["GET","DELETE"])
def delete(cafe_id):
    cafe_to_delete = db.session.query(Cafe).get(cafe_id)
    db.session.delete(cafe_to_delete)
    db.session.commit()
    return redirect("/")

@app.route("/update-price/<int:cafe_id>", methods=["GET", "POST"])
def update_price(cafe_id):
    form = PriceForm()
    cafe_to_update = db.session.query(Cafe).get(cafe_id)
    if form.validate_on_submit():
        db.session.query(Cafe).filter_by(id=cafe_id).update(dict(coffee_price=request.form.get('coffee_price')))
        db.session.commit()
        return redirect('/')
    return render_template('update_price.html', form=form, cafe = cafe_to_update)

if __name__ == "__main__":
    app.run(debug=True)
