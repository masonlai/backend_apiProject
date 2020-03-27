from flask import Flask, render_template
from flask_restful import Api
from .resources.data import Data, customerData, getData
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import sys, os, click

import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from flask_marshmallow import Marshmallow

app = Flask(__name__)
api = Api(app)
app.config['PROPAGATE_EXCEPTIONS'] = True

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', prefix + os.path.join(app.root_path, 'data.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)

db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')


# backend
api.add_resource(Data, '/data/')
api.add_resource(getData, '/getdata/')
api.add_resource(customerData, '/getalldata/')


@app.cli.command()
def initdb():
    db.drop_all()
    db.create_all()
    click.echo('Initialized database.')


if __name__ == "__main__":
    app.run()



from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class order(db.Model):
    __tablename__ = 'Order'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(40), nullable=False)
    order_date = db.Column(db.DateTime)

    comment = relationship("Items")

    def __init__(self, id, customer, address, order_date):
        self.id = id
        self.customer = customer
        self.address = address
        self.order_date = order_date


class items(db.Model):
    __tablename__ = 'Items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    order_id = db.Column(db.Integer, ForeignKey('Order.id'))

    def __init__(self, name, quantity, order_id):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.order_id = order_id