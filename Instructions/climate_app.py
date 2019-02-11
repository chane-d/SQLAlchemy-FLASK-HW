from flask import Flask
from flask import jsonify

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect


engine = create_engine("sqlite:///Resources/hawaii.sqlite")
session = Session(bind=engine)


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)

@app.route("/")
def welcome():
    return (
        f"Welcome to the API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"to search by start date : /api/v1.0/yyyy-mm-dd<br/>"
        f"to search by date range, with start date first and end date second: /api/v1.0/yyyy-mm-dd/yyyy-mm-dd<br/>"
    )



