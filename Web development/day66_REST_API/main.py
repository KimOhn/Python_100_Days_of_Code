from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random
##http status codes definitions
#https://www.webfx.com/web-development/glossary/http-status-codes/
##Testing and documenting your API - use postman:
# https://learning.postman.com/docs/publishing-your-api/documenting-your-api/
app = Flask(__name__)
app.app_context().push()
##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##Cafe TABLE Configuration
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

    def dict_b4_jsonify(self):
#This approach eliminates the error that can be introduced by hard coding a dictionary before jsonifying
        dict = {}
        for col in self.__table__.columns:
            dict[col.name] = getattr(self, col.name)
        return dict



@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random", methods = ["GET"])
def random_cafe():
    row_count = db.session.query(Cafe).count()
    # Generate a random number for skipping some records
    random_offset = random.randint(0, row_count-1)
    # Return the first record after skipping random_offset rows
    random_cafe = db.session.query(Cafe).offset(random_offset).first()
    #we have to turn our random_cafe SQLAlchemy Object into a JSON. This process is called serialization.
    return jsonify(cafe= random_cafe.dict_b4_jsonify())

@app.route("/all", methods = ["GET"])
def all_cafe():
    all_cafes = db.session.query(Cafe).all()
    return jsonify(cafes = [row.dict_b4_jsonify() for row in all_cafes])

#https://www.geeksforgeeks.org/using-request-args-for-a-variable-url-in-flask/
@app.route("/search", methods = ["GET"])
def nearby_cafe():
    query_location = request.args.get("loc").title()
    nearby_cafe = db.session.query(Cafe).filter_by(location = query_location).first()
    #try taking first object from query and checking if it is Null or not
    if nearby_cafe:
        return jsonify(cafe = nearby_cafe.dict_b4_jsonify()), 200
    else:
        return jsonify(error = {"Not Found": "Sorry, we don't have a cafe at that location."}), 404

## HTTP POST - Create Record
def str_to_bool(url_entry):
    if url_entry in ['True', ' true', 'T', 't', 'Yes', 'yes', 'y', '1']:
        return True
    else:
        return False

@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(name=request.args.get("name"),
                    map_url=request.args.get("map_url"),
                    img_url=request.args.get("img_url"),
                    location=request.args.get("location"),
                    seats=request.args.get("seats"),
                    has_toilet=str_to_bool(request.args.get("has_toilet")),
                    has_wifi=str_to_bool(request.args.get("has_wifi")),
                    has_sockets=str_to_bool(request.args.get("has_sockets")),
                    can_take_calls=str_to_bool(request.args.get("can_take_calls")),
                    coffee_price=request.args.get("coffee_price")
                    )
    db.session.add(new_cafe)
    db.session.commit()

    return jsonify(response={"success": "Successfully added the new cafe"})


## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe_to_update = db.session.query(Cafe).get(cafe_id)
    if cafe_to_update:
        price =  request.args.get("new_price")
        cafe_to_update.coffee_price = price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price"}), 200
    else:
        return jsonify(error = {"Not Found": "Sorry, the cafe id was not found in the database"}), 404

## HTTP DELETE - Delete Record

@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def closed_cafe(cafe_id):

    api_key = request.args.get("api-key")
    if api_key == 'TopSecretAPIKey':
        cafe_to_delete = db.session.query(Cafe).get(cafe_id)
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the DB"}), 200
        else:
            return jsonify(error={"Not Found": "Sorry, the cafe id was not found in the database"}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403

if __name__ == '__main__':
    app.run(debug=True)
